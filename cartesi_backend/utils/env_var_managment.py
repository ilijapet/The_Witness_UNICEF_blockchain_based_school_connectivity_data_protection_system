import os

from dotenv import load_dotenv

load_dotenv()


class GetVar:
    @staticmethod
    def get_env_var(index):
        private_key = os.environ.get(f"PRIVATE_KEY_{index}").encode()
        public_key = os.environ.get(f"PUBLIC_KEY_{index}").encode()
        return private_key, public_key
