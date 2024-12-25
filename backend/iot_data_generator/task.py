import base64
import datetime
import hashlib
import json
import random

import requests
from dotenv import load_dotenv

from utils.env_var_managment import GetVar
from utils.protocol import WitnessProtocol

load_dotenv()


class IotDataGenerator:
    def __init__(self):
        super().__init__()
        self.public_key_iot = None
        self.private_key_iot = None

    @staticmethod
    def hash_public_key(public_key):
        hash_obj = hashlib.sha256()
        hash_obj.update(public_key)
        hash_hex = hash_obj.hexdigest()
        
        return hash_hex

    def generate_random_device_data(self):
        env_index = random.randint(1, 1)
        self.private_key_iot, self.public_key_iot = GetVar.get_env_var(env_index)
        data = {
            "school_id": 1,
            "download_speed": random.uniform(0, 100),
            "upload_speed": random.uniform(0, 100),
            "latency": random.uniform(1, 100),
            "timestamp": datetime.datetime.now().isoformat(),
        }
        return json.dumps(data)

    def iot_data_generator(self, job=None):
        private_key_iot, public_key_iot = GetVar.get_env_var(1)
        data = self.generate_random_device_data()
        digital_signature = WitnessProtocol.sign_message(data.encode(), private_key_iot)
        body = {
            "data": data.encode(),
            "signature": digital_signature,
            "public_key": public_key_iot,
        }
        for key, value in body.items():
            body[key] = base64.b64encode(value).decode()
        requests.post("http://localhost:8005/api/v1/bridge", json=body)
