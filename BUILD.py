import os
import sys


def build_me(name):
    os.system(f"pyinstaller .\\source\\pyhell_manager.py -F -n{name} -c -i .\\yabr.ico")


if __name__ == "__main__":

    print("You can use\n"
          "`python build.py \"AppName\" \"AppIcon\"`")
    if len(sys.argv) == 1:

        name = input("Enter application name >>> ")
        build_me(name)

    else:
        os.system(f"pyinstaller .\\source\\pyhell_manager.py -F -n{sys.argv[1]} -c -i .\\{sys.argv[2]}")

