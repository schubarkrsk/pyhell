import os.path
import sys

from cryptography.fernet import Fernet
from bin.security.security_configuration import Settings


class PyHell_Cryptor:
    def __init__(self):
        self.key_home = ""
        if sys.platform == "win32":
            self.key_home = Settings.WINDOWS_KEY_LOCATION
        else:
            self.key_home = "/opt/temp.com"

        if not os.path.exists(self.key_home):
            self._gen_key()

        self.crypto_key = open(self.key_home, "r").read()

    def _gen_key(self):
        key = Fernet.generate_key()
        with open(self.key_home, "wb") as key_file:
            key_file.write(key)
