import os
import sys


def push_reboot():
    if sys.platform == "nt":
        os.system("shutdown /r /t 0")
    else:
        try:
            os.system("reboot")
        except:
            os.system("sudo reboot")
