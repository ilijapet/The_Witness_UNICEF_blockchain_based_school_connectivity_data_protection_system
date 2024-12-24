import base64
import datetime
import hashlib
import json
import logging
import traceback
from os import environ

import requests
from utils.data_processing import Database, engine
from utils.protocol import WitnessProtocol

database = Database(engine)

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

rollup_server = environ["ROLLUP_HTTP_SERVER_URL"]
logger.info(f"HTTP rollup_server url is {rollup_server}")


def hex2str(hex):
    """
    Decodes a hex string into a regular string
    """
    logger.info("Hex")
    result = bytes.fromhex(hex[2:]).decode("utf-8")
    return json.loads(result)


def str2hex(str):
    """
    Encodes a string as a hex string
    """
    return "0x" + str.encode("utf-8").hex()


def hash_public_key(public_key):
    """
    Hashes a public key
    """
    logger.info(f"Adding report {public_key}")
    hash_obj = hashlib.sha256()
    hash_obj.update(public_key)
    hash_hex = hash_obj.hexdigest()
    return hash_hex


def add_report(output=""):
    """
    Adds a report to the rollup server
    """
    logger.info("Adding report " + output)
    report = {"payload": str2hex(output)}
    response = requests.post(rollup_server + "/report", json=report)
    logger.info(f"Received report status {response.status_code}")


def get_user_data(data):
    """
    Gets user data from the database
    """
    user_data = database.get_data(1)
    if not user_data:
        return "reject"
    add_report(user_data)
    return "accept"


def add_iot_device(data):
    """
    Adds an IoT device to the database
    """
    try:
        public_key = data["iot_public_key"].decode("utf-8").replace("\n", "\\n").encode("utf-8")
        digest = {"uuid": hash_public_key(public_key)}
        database.insert_data(digest)
        logger.info("New school device ID inserted")
        add_report(f"New id added {digest}")
        return "accept"
    except Exception as e:
        msg = f"Error {e} processing data\n{traceback.format_exc()}"
        logger.error(msg)
        response = requests.post(rollup_server + "/report", json={"payload": str2hex(msg)})
        logger.info(f"Received report status {response.status_code} body {response.content}")
        return "reject"


def update_data(data):
    """
    Updates data for an existing device
    """
    result = WitnessProtocol.verify_signature(data["data"], data["signature"], data["public_key"])
    if result:
        status = "accept"
        logger.info("Signature verification confirmed")
        public_key = data["public_key"].decode("utf-8").replace("\n", "\\n").encode("utf-8")
        digest = hash_public_key(public_key)
        logger.info(f"Digest {digest}")
        # device = database.get_data(digest)
        # if device:
        data_dict = json.loads(data["data"])
        print(data_dict, "ovde si")
        database.update_data(data_dict)
        add_report("Data updated")
    else:
        status = "reject"
        logger.info("Signature not valid")
        add_report("Signature verification failed")
    return status


def handle_advance(data):
    """
    Handles an advance request
    """
    logger.info(f"Received advance request data {data}")
    status = "accept"
    try:
        input_data = hex2str(data["payload"])
        logger.info(f"Received input: {input_data}")
        for key, value in input_data.items():
            data[key] = base64.b64decode(value)
        if "iot_public_key" in data:
            logger.info("Adding new IoT device")
            add_iot_device(data)
        elif "public_key" in data:
            logger.info("Updating data for existing device")
            update_data(data)
            logger.info(f"Adding notice with payload: '{input_data}'")
            response = requests.post(
                rollup_server + "/notice", json={"payload": str2hex(str(input_data))}
            )
            logger.info(f"Received notice status {response.status_code} body {response.content}")
    except Exception as e:
        status = "reject"
        msg = f"Error {e} processing data  {data}\n{traceback.format_exc()}"
        logger.error(msg)
        response = requests.post(rollup_server + "/report", json={"payload": str2hex(msg)})
        logger.info(f"Received report status {response.status_code} body {response.content}")
    return status


def handle_inspect(data):
    """
    Handles an inspect request
    """
    try:
        payload = hex2str(data["payload"])
    except Exception as e:
        logger.error(f"Error {e} decoding payload {data['payload']}")
        return "reject"
    method = payload.get("method")
    logger.info(f"Received inspect request data {method}")
    handler = inspect_method_handlers.get(method)
    if not handler:
        return "reject"
    return handler(method)


inspect_method_handlers = {"get_user_data": get_user_data}

finish = {"status": "accept"}

handlers = {
    "advance_state": handle_advance,
    "inspect_state": handle_inspect,
}


while True:
    logger.info("Sending finish")
    response = requests.post(rollup_server + "/finish", json=finish)
    logger.info(f"Received finish status {response.status_code}")
    logger.info("Time:" + str(datetime.datetime.now()))
    if response.status_code == 202:
        logger.info("No pending rollup request, trying again")
    else:
        rollup_request = response.json()
        logger.info(f"Request type {rollup_request['request_type']}")
        data = rollup_request["data"]
        logger.info(f"Data {data}")

        handler = handlers[rollup_request["request_type"]]
        finish["status"] = handler(rollup_request["data"])
