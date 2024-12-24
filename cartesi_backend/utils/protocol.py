import logging

from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from dotenv import load_dotenv

from .env_var_managment import GetVar

load_dotenv()


private_key_cartesi, public_key_cartesi = GetVar.get_env_var("CARTESI")


class WitnessProtocol:
    # Generate RSA key pair
    @staticmethod
    def generate_key_pair():
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        return private_key, public_key

    # Sign a message with private key
    @staticmethod
    def sign_message(message, private_key):
        try:
            private_key = private_key.replace(b"\\n", b"\n")
            key = RSA.import_key(private_key)
            h = SHA256.new(message)
            signer = PKCS1_v1_5.new(key)
            signature = signer.sign(h)
            return signature
        except Exception as e:
            logging.info(f"Signing Message Error:{e}")

    # Encrypt a message with public key
    @staticmethod
    def encrypt_message(message, public_key):
        try:
            public_key = public_key.decode("utf-8").replace("\\n", "\n")
            key = RSA.import_key(public_key.encode())
            cipher = PKCS1_OAEP.new(key)
            message_bytes = message.encode("utf-8")
            encrypted_message = cipher.encrypt(message_bytes)
            return encrypted_message
        except Exception as e:
            logging.info(f"Encrypting Message Error:{e}")

    # Decrypt a message with private key
    @staticmethod
    def decrypt_message(encrypted_message, private_key):
        private_key = private_key.replace(b"\\n", b"\n")
        key = RSA.import_key(private_key)
        cipher = PKCS1_OAEP.new(key)
        decrypted_message = cipher.decrypt(encrypted_message)
        return decrypted_message

    @staticmethod
    def verify_signature(message, signature, public_key):
        public_key = public_key.decode("utf-8").replace("\\n", "\n").encode("utf-8")
        key = RSA.import_key(public_key)
        h = SHA256.new(message)
        verifier = PKCS1_v1_5.new(key)
        if verifier.verify(h, signature):
            return True
        else:
            return False

    # Main function to simulate the protocol
    @staticmethod
    def encrypt_sign(message, public_key_cartesi, private_key_iot, public_key_iot):
        encrypted_message = WitnessProtocol.encrypt_message(message, public_key_cartesi)
        signature_a = WitnessProtocol.sign_message(encrypted_message, private_key_iot)
        return encrypted_message, signature_a, public_key_iot

    @staticmethod
    def decrypt_verifay(received_encrypted_message, received_signature_a, public_key_iot):
        is_signature_valid_a = WitnessProtocol.verify_signature(
            received_encrypted_message, received_signature_a, public_key_iot
        )
        if is_signature_valid_a:
            decrypted_message = WitnessProtocol.decrypt_message(
                received_encrypted_message, private_key_cartesi
            )
            print(
                "Message from IoT device to Cartrsi backend via Django server:",
                decrypted_message.decode(),
            )
            print("Signature verification from node A): Valid")
            return decrypted_message
        else:
            print("Signature verification (Node A): Invalid")
