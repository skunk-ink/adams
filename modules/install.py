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
from colours import colours as colours

class run():
    NEED_RESTART = False
    PATH = os.getcwd()
    DATA_PATH = PATH + '/data/'      # Data Directory Path
    HSD_PATH = PATH + '/hsd/'
    SKYNET_PATH = PATH + '/skynet-webportal/'
    ANSIBLE_PLAYBOOKS_PATH = PATH + '/ansible-playbooks/'
    ANSIBLE_PRIVATE_PATH = PATH + '/ansible-private/'
    POWERDNS_PATH = PATH + '/pdns/'
    LOG_FILE = DATA_PATH + "install.log"

    def __init__(self):

        DEPENDS = open("./DEPENDS", "r")
        setInstall = False
        addWinPackage = False
        addLinuxPackage = False
        addPythonPackage = False
        addSkynetPackage = False
        addHNSPackage = False
        addPDNSPackage = False

        self.clear_screen()

        # Install packages for Linux
        if platform == "linux":
            #logging.basicConfig(filename=self.LOG_FILE, level=logging.DEBUG)
            
            setInstall = True

            # Install Dependencies
            while(setInstall == True):
                package = DEPENDS.readline().replace("\n", "")

                if package.startswith("# WINDOWS"):
                    addWinPackage = False       # Toggle to install Windows Dependencies
                    addLinuxPackage = False
                    addPythonPackage = False
                    addSkynetPackage = False
                    addHNSPackage = False
                    addPDNSPackage = False

                elif package.startswith("# LINUX"):
                    addWinPackage = False
                    addLinuxPackage = False      # Toggle to install Linux Dependencies
                    addPythonPackage = False
                    addSkynetPackage = False
                    addHNSPackage = False
                    addPDNSPackage = False
                    print(colours.red(self, "Installing Linux Dependencies..."))

                elif package.startswith("# PYTHON"):
                    addWinPackage = False
                    addLinuxPackage = False
                    addPythonPackage = False     # Toggle to install Python Dependencies
                    addSkynetPackage = False
                    addHNSPackage = False
                    addPDNSPackage = False
                    print(colours.red(self, "\nInstalling Python Dependencies..."))
                    
                elif package.startswith("# SKYNET"):
                    addWinPackage = False
                    addLinuxPackage = False
                    addPythonPackage = False
                    addSkynetPackage = False     # Toggle to install Skynet-Webportal and Dependencies
                    addHNSPackage = False
                    addPDNSPackage = False
                    print(colours.red(self, "\nInstalling Skynet-Webportal..."))
                    
                elif package.startswith("# HNS"):
                    addWinPackage = False
                    addLinuxPackage = False
                    addPythonPackage = False
                    addSkynetPackage = False
                    addHNSPackage = False        # Toggle to install HNS Node and Dependencies
                    addPDNSPackage = False
                    print(colours.red(self, "\nInstalling HNS Node..."))
                    
                elif package.startswith("# PDNS"):
                    addWinPackage = False
                    addLinuxPackage = False
                    addPythonPackage = False
                    addSkynetPackage = False
                    addHNSPackage = False
                    addPDNSPackage = True       # Toggle to install PowerDNS and Dependencies
                    print(colours.red(self, "\nInstalling PowerDNS..."))

                    self.addPDNSSources()
                    self.checkResolver()

                elif package.startswith("# EOF"):
                    setInstall = False

                elif addWinPackage == True:
                    break

                elif addLinuxPackage == True:

                    if package != "":
                        print(colours.green(self, " [+] ") + "Installing " + str(package))
                        subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
                        print()
            # Install Python Packages
                elif addPythonPackage == True:

                    if package != "":
                        print(colours.green(self, " [+] ") + "Installing " + str(package))
                        subprocess.run(["pip", "install", package], check=True)
                        print()

            # Install Skynet Webportal
                elif addSkynetPackage == True:

                    if package != "":
                        if package.endswith("skynet-webportal.git"):
                            if os.path.isdir(self.SKYNET_PATH) == False:
                                print(colours.green(self, " [+] ") + "Installing Skynet Webportal")
                                subprocess.run(["git", "clone", package], cwd=self.PATH, check=True)
                                subprocess.run(["npm", "install", "yarn"], cwd=(self.SKYNET_PATH + "/packages/website"))
                                subprocess.run(["yarn", "build"], cwd=(self.SKYNET_PATH + "/packages/website"))
                                print()
                            else:
                                print(colours.yellow(self, " [!] ") + "Skynet Webportal Installation Detected!")

                        elif package.endswith("ansible-playbooks.git"):
                            if os.path.isdir(self.ANSIBLE_PLAYBOOKS_PATH) == False:
                                print(colours.green(self, " [+] ") + "Installing Ansible-Playbooks")
                                subprocess.run(["git", "clone", package], cwd=self.PATH, check=True)
                                print()
                            else:
                                print(colours.yellow(self, " [!] ") + "Ansible-Playbooks Installation Detected!")
                                
                        elif package.endswith("ansible-private-sample.git"):
                            if os.path.isdir(self.ANSIBLE_PRIVATE_PATH) == False:
                                print(colours.green(self, " [+] ") + "Installing Ansible-Private")
                                subprocess.run(["git", "clone", package, "ansible-private"], cwd=self.PATH, check=True)
                                print()
                            else:
                                print(colours.yellow(self, " [!] ") + "Ansible-Private Installation Detected!")
            # Install Handshake Daemon
                elif addHNSPackage == True:
                    if package != "":
                        if package.endswith("hsd.git"):
                            if os.path.isdir(self.HSD_PATH) == False:
                                print(colours.green(self, " [+] ") + "Installing Handshake Daemon")
                                subprocess.run(["git", "clone", package], cwd=self.PATH, check=True)
                                subprocess.run(["npm", "install", "--production"], cwd=self.HSD_PATH)
                                print()
                            else:
                                print(colours.yellow(self, " [!] ") + "Handshake Daemon Installation Detected!")

                elif addPDNSPackage == True:
                    if package != "":
                        print(colours.green(self, " [+] ") + "Installing " + str(package))
                        subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
                        print()
                                
        # Install packages for Windows
        elif platform == "win32":
            #logging.basicConfig(filename=self.LOG_FILE, level=logging.DEBUG)
            
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
        
        print(colours.red("\n[!] ") + "Please restart device to apply final changes.")
        print("\nPress any key to continue...")
        getch()
#################################################### END: __init__(self)

    def addPDNSSources(self):
        # Check for existing PowerDNS APT sources
        if not os.path.exists("/etc/apt/sources.list.d/pdns.list"):
            with open('/etc/apt/sources.list.d/pdns.list') as sourceFile:
                sources = sourceFile.readlines()

            for line in sources:
                # If PowerDNS APT source does not exist, add it to /etc/apt/sources.list.d/pdns.list
                if 'http://repo.powerdns.com/ubuntu' not in line:
                    addSource = "echo 'deb [arch=amd64] http://repo.powerdns.com/ubuntu focal-auth-46 main' > /etc/apt/sources.list.d/pdns.list"
                    subprocess.run(["sudo", "sh", "-c", addSource], cwd=self.PATH, check=True)
                    addSource = "echo 'Package: pdns-*\nPin: origin repo.powerdns.com\nPin-Priority: 600' > /etc/apt/preferences.d/pdns"
                    subprocess.run(["sudo", "sh", "-c", addSource], cwd=self.PATH, check=True)
                    subprocess.run(["wget", "https://repo.powerdns.com/FD380FBB-pub.asc"], cwd=self.PATH, check=True)
                    subprocess.run(["sudo", "apt-key", "add", "FD380FBB-pub.asc"], cwd=self.PATH, check=True)
                    subprocess.run(["rm", "-fr", "FD380FBB-pub.asc"], cwd=self.PATH, check=True)
                    subprocess.run(["sudo", "apt", "update"], cwd=self.PATH, check=True)
#################################################### END: addPDNSSources(self)

    def checkResolver(self):
        dnsExists = False
        stubListenterExists = False

        # Check resolved.conf for configuration
        with open('/etc/systemd/resolved.conf') as resolveFile:
            lines = resolveFile.readlines()

        for line in lines:
            if line == "DNS=1.1.1.1":
                dnsExists = True

            if line == "DNSStubListener=no":
                stubListenterExists = True

        # Add configurations to resolved.conf
        if dnsExists == False or stubListenterExists == False:
            addLine = "# A.D.A.M.S. PowerDNS Configurations"
            subprocess.run(["sudo", "sh", "-c", addLine], check=True)
            NEED_RESTART = True

        if dnsExists == False:
            addLine = "echo 'DNS=1.1.1.1' >> /etc/systemd/resolved.conf"
            subprocess.run(["sudo", "sh", "-c", addLine], check=True)

        if stubListenterExists == False:
            addLine = "echo 'DNSStubListener=no' >> /etc/systemd/resolved.conf"
            subprocess.run(["sudo", "sh", "-c", addLine], check=True)

        # Create Symlink
        subprocess.run(["sudo", "ln", "-sf", "/run/systemd/resolve/resolv.conf", "/etc/resolv.conf"], check=True)
#################################################### END: checkResolver(self)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
#################################################### END: clear_screen()
