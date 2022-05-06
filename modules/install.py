"""               _                                    
     __ _      __| |     __ _      _ _ _      ____     
    / _` |    / _` |    / _` |    | ` ` |    / __/     
   | (_| |   | (_| |   | (_| |    | | | |    \__ \     
    \__,_| ⍟ \__,_|▄⍟▄\__,_|█⍟▄|_|_|_| ⍟ /___/ ⍟  
                   ███           ███                   
                 ███               ███                 
                ██                   ██                
                         ▄▄█▄▄                         
               ▄       ███───███       ▄               
              ███     ███──█──███     ███              
               ▀       ██──▄──██       ▀               
                         ▀▀█▀▀                         
                ██                   ██                
                 ███               ███                 
    Automated Decentralization And Management System   
                    ▀▀▀█████████▀▀▀                    
"""

import os
import logging
import subprocess

from sys import platform
from time import sleep as sleep
from getch import getch as getch
from modules.colours import colours as colours

class run():
    def __init__(self):
        PATH = os.getcwd()
        DATA_PATH = PATH + '/data/'      # Data Directory Path
        HSD_PATH = PATH + '/hsd/'
        SKYNET_PATH = PATH + '/skynet-webportal/'
        LOG_FILE = DATA_PATH + "install.log"

        DEPENDS = open("DEPENDS", "r")
        setInstall = False
        addWinPackage = False
        addLinuxPackage = False
        addPythonPackage = False
        addAdamsPackage = False

        self.clear_screen()

        # Install packages for Linux
        if platform == "linux":
            logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)
            
            setInstall = True

            # Install Dependencies
            while(setInstall == True):
                package = DEPENDS.readline().replace("\n", "")

                if package.startswith("# LINUX"):
                    addWinPackage = False
                    addLinuxPackage = True
                    addPythonPackage = False
                    addAdamsPackage = False
                    print(colours.red(self, "\nInstalling Linux Dependencies..."))

                elif package.startswith("# WINDOWS"):
                    addWinPackage = False
                    addLinuxPackage = False
                    addPythonPackage = False
                    addAdamsPackage = False

                elif package.startswith("# PYTHON"):
                    addWinPackage = False
                    addLinuxPackage = False
                    addPythonPackage = True
                    addAdamsPackage = False
                    print(colours.red(self, "\nInstalling Python Dependencies..."))
                    
                elif package.startswith("# ADAMS"):
                    addWinPackage = False
                    addLinuxPackage = False
                    addPythonPackage = False
                    addAdamsPackage = True
                    print(colours.red(self, "\nInstalling A.D.A.M.S Dependencies..."))
                    
                elif package.startswith("# EOF"):
                    setInstall = False

                elif addWinPackage == True:
                    break

                elif addLinuxPackage == True:

                    if package != "":
                        print(colours.green(self, " [+] ") + "Installing APT Dependency: " + str(package))
                        subprocess.run(["sudo", "apt", "-qqq", "install", "-y", package], check=True)

                elif addPythonPackage == True:

                    if package != "":
                        print(colours.green(self, " [+] ") + "Installing PIP Dependency: " + str(package))
                        subprocess.run(["pip", "-q", "install", package], check=True)

                elif addAdamsPackage == True:

                    if package != "":
                        if package.endswith("skynet-webportal.git"):
                            if os.path.isdir(SKYNET_PATH) == False:
                                print(colours.green(self, " [+] ") + "Installing A.D.A.M.S Dependency: " + str(package))
                                subprocess.run(["git", "clone", package], check=True)
                                print()
                            else:
                                print(colours.red(self, " [-] ") + "Skynet Portal Installation Detected!")
                                

                        elif package.endswith("hsd.git"):
                            if os.path.isdir(HSD_PATH) == False:
                                print(colours.green(self, " [+] ") + "Installing A.D.A.M.S Dependency: " + str(package))
                                subprocess.run(["git", "clone", package], check=True)
                                subprocess.run(["npm", "install"], cwd=HSD_PATH)
                                print()
                            else:
                                print(colours.red(self, " [-] ") + "HSD Installation Detected!")
                            
                
        # Install packages for Windows
        elif platform == "win32":
            logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)
            
            setInstall = True

            # Install Dependencies
            while(setInstall == True):
                package = DEPENDS.readline().replace("\n", "")

                if package.startswith("# LINUX"):
                    addWinPackage = False
                    addLinuxPackage = False
                    addPythonPackage = False
                    print(colours.red(self, "\nInstalling Windows Dependencies..."))

                elif package.startswith("# WINDOWS"):
                    addWinPackage = True
                    addLinuxPackage = False
                    addPythonPackage = False

                elif package.startswith("# PYTHON"):
                    addWinPackage = False
                    addLinuxPackage = False
                    addPythonPackage = True
                    print(colours.red(self, "\nInstalling Python Dependencies..."))
                    
                elif package.startswith("# ADAMS"):
                    addWinPackage = False
                    addLinuxPackage = False
                    addPythonPackage = True
                    print(colours.red(self, "\nInstalling Python Dependencies..."))
                    
                elif package.startswith("# EOF"):
                    setInstall = False

                elif addWinPackage == True:
                    if package != "":
                        print(colours.green(" [+] ") + "Installing Windows Dependency: ", str(package))
                        # Install Windows Dependencies
                        print()

                elif addLinuxPackage == True:
                    break

                elif addPythonPackage == True:
                    break

                elif addLinuxPackage == True:
                    break
                
        print("\nPress any key to continue...")
        getch()
    #################################################### END: __init__(self)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    #################################################### END: clear_screen()
