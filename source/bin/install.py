import winreg
import os
import sys


class Installer:
    def __init__(self, os_family):
        """
        Install malware in system
        :param os_family:
        """
        if os_family == "win32":
            self.install_winnt()
        if os_family == "darwin":
            self.install_osx()
        else:
            self.install_linux()

    def install_winnt(self):
        pass

    def install_osx(self):
        pass

    def install_linux(self):
        pass


class KeeperCheck:
    def __init__(self, os_family):
        """
        Check installation
        :param os_family:
        """
        if os_family == "win32":
            self.check_winnt()
        else:
            self.check_unix()

    def check_winnt(self):
        pass

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