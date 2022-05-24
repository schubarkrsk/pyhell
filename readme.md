# PyHELL Malware
### Python multiplatform rootkit malware. 
### Author not like if you will use it in crime. All files created ONLY FOR EDUCATION!

---
### Lifecycle
* Malware downloaded and first-run at user device
* Malware move itself copy to Application Data directory or Temp directory
  * C:\Users\Foo\AppData\Roaming\Microsoft\Bar.exe (Windows 10/7)
  * C:\Users\Foo\Application Data\Local\Temp\Bar.exe (Windows XP)
  * ~linux in dev state~
* Malware add it into WINREG Autorun branch or UNIX LaunchDaemons
  * HKLM\Software\Microsoft\Windows\CurrentVersion\Run
* Change desktop wallpaper (soruce/wp.png)
* ASYNC Encrypt/Hide all user files in Documents / Downloads / Desktop / Other disks
* (IN PLANS) Add backdoor vnc and keyloger
* Create UNLOCK.exe on desktop 

---

### Medkit
* Run UNLOCK.exe on desktop
* Enter passcode 
  * located into source/main.py/UNLOCK_PASSCODE
  * if passcode incorrect system reboot immidiatly to protect BRUTFORCE
* After correct passcode it delete all autorun keys and start decrypt/unhiding files
* After finish decrypt system reboot

---

## DOCUMENTATION FOR DEVELOPER AND AV MANUFACTURE

### Encryptor module
WARNING >> Always keep backup of your machine and before first run generate key file. If you're lost it all you data lost!

Directories where key file located
* Windows >> C:\User\Foo\Local\Temp\Bar.com (where "Bar" is Name of your malware from bin.configuration.Settings)
* UNIX >> /opt/temp.com

How to create test key?
* in source directory run command 
  * `python pyhell_manager.py --dbg --get-key` for Windows
  * `python3 pyhell_manager.py --dbg --get-key` for UNIX