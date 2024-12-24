import json
import logging
import os
from typing import Dict

from django.conf import settings
from eth_account.signers.local import LocalAccount
from web3 import Web3


class BaseContract:

    def __init__(
        self,
    ):
        self.abi_path: str = settings.ABI_PATH
        self.inputbox_address: "address" = Web3.to_checksum_address(  # noqa: F821
            settings.INPUTBOX_ADDRESS
        )
        self.dapp_address: "address" = Web3.to_checksum_address(  # noqa: F821
            settings.DAPP_ADDRESS
        )  # noqa: 821
        self.default_url: str = settings.DEFAULT_URL
        try:
            self.w3 = Web3(Web3.HTTPProvider(self.default_url))
            self.account = self.w3.eth.account.from_key(settings.PRIVATE_KEY_FOUNDRY)
        except Exception as e:
            logging.error(f"Error initializing BaseContract: {e}")

        self.private_keys = settings.PRIVATE_KEY_FOUNDRY


class ContractInstatiator(BaseContract):

    def __init__(self):
        super().__init__()
        self.contract: "Contract" = self.contract_instance(
            self.abi_path, self.inputbox_address
        )  # noqa: 821

    # Return contract instance
    def contract_instance(self, abi_path: str, address: str) -> "Contract":  # noqa: 821
        try:
            abi = ContractUtilities.load_abi(abi_path)
            contract = self.w3.eth.contract(address, abi=abi)  # type: ignore
            return contract
        except Exception as e:
            logging.error(f"Error initializing contract_instance: {e}")
            raise e


class ContractUtilities:

    @staticmethod
    def load_abi(abi_path: str) -> Dict | None:
        try:
            cwd = os.getcwd()
            abi_path = os.path.join(cwd, abi_path)
            if not os.path.exists(abi_path):
                components = abi_path.split(os.sep)
                index = components.index("device_data_integrity_system")
                components.insert(index + 1, "backend")
                abi_path = os.sep + os.path.join(*components)
            with open(abi_path) as f:
                abi = json.load(f)
                abi = abi["abi"]
                assert abi, f"ABI file {abi_path} is empty"
                return abi
        except Exception as e:
            logging.error(f"Error loading ABI: {e}")
            return None

    @staticmethod
    def generate_hex(value: dict) -> str:
        inputBytes = json.dumps(value)
        hex_s = "0x" + inputBytes.encode("utf-8").hex()
        return hex_s


class SCInterface(ContractUtilities, ContractInstatiator):

    account: LocalAccount

    # General setup
    def __init__(self):
        super().__init__()

    def sendInput(self, value: dict):

        # Generating hex from value
        hex_s: str = ContractUtilities.generate_hex(value)

        # Creating and sending transaction
        nonce = self.w3.eth.get_transaction_count(self.account.address)
        stored_transaction = self.contract.functions.addInput(
            self.dapp_address, hex_s
        ).build_transaction({"from": self.account.address, "nonce": nonce})
        signed_tx = self.w3.eth.account.sign_transaction(
            stored_transaction, private_key=self.private_keys
        )
        transaction_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(transaction_hash)
        # print(tx_receipt)
        return transaction_hash

    # def sendInput(self, value: dict) -> dict:
    #     hex_s: str = ContractUtilities.generate_hex(value)
    #     tx_hash: Dict = self.contract.functions.addInput(self.dapp_address, hex_s).transact(
    #         {"from": self.account.address}
    #     )
    #     return tx_hash


# Contract instance setup:
# Get private key
# Get abi path and load abi
# Get default url (infura or alchemy)
# Get inputbox address

# Tx arguments:
# Get dapp address
# Get value and generate hex

# Transaction setup and execution:
# Get contract instance
# Get nonce
# Build transaction
# Sign transaction
# Send raw transaction
# Wait for transaction receipt
# Return transaction
