import os
import sys

import bin.install
from bin import themes



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

    else:
        pass

