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

class run:
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
        runInstall = False
        winPackage = False
        linuxPackage = False
        macOSPackage = False
        pythonPackage = False
        skynetPackage = False
        hsdPackage = False
        pdnsPackage = False

        self.clear_screen()

        # Install packages for Linux
        if platform is "linux":
            #logging.basicConfig(filename=self.LOG_FILE, level=logging.DEBUG)
            
            runInstall = True

            # Install Dependencies
            while(runInstall is True):
                package = DEPENDS.readline().replace("\n", "")

                if package.startswith("# WINDOWS"):
                    winPackage = False       # Toggle to install Windows Dependencies
                    linuxPackage = False
                    macOSPackage = False
                    pythonPackage = False
                    skynetPackage = False
                    hsdPackage = False
                    pdnsPackage = False

                elif package.startswith("# LINUX"):
                    winPackage = False
                    linuxPackage = False      # Toggle to install Linux Dependencies
                    macOSPackage = False
                    pythonPackage = False
                    skynetPackage = False
                    hsdPackage = False
                    pdnsPackage = False
                    print(colours.red(self, "Installing Linux Dependencies..."))

                elif package.startswith("# MACOS"):
                    winPackage = False
                    linuxPackage = False
                    macOSPackage = False      # Toggle to install Linux Dependencies
                    pythonPackage = False
                    skynetPackage = False
                    hsdPackage = False
                    pdnsPackage = False
                    print(colours.red(self, "Installing MacOS Dependencies..."))

                elif package.startswith("# PYTHON"):
                    winPackage = False
                    linuxPackage = False
                    macOSPackage = False
                    pythonPackage = False     # Toggle to install Python Dependencies
                    skynetPackage = False
                    hsdPackage = False
                    pdnsPackage = False
                    print(colours.red(self, "\nInstalling Python Dependencies..."))
                    
                elif package.startswith("# SKYNET"):
                    winPackage = False
                    linuxPackage = False
                    macOSPackage = False
                    pythonPackage = False
                    skynetPackage = False     # Toggle to install Skynet-Webportal and Dependencies
                    hsdPackage = False
                    pdnsPackage = False
                    print(colours.red(self, "\nInstalling Skynet-Webportal..."))
                    
                elif package.startswith("# HSD"):
                    winPackage = False
                    linuxPackage = False
                    pythonPackage = False
                    skynetPackage = False
                    hsdPackage = False        # Toggle to install HNS Node and Dependencies
                    pdnsPackage = False
                    print(colours.red(self, "\nInstalling Handshake Daemon..."))
                    
                elif package.startswith("# PDNS"):
                    winPackage = False
                    linuxPackage = False
                    macOSPackage = False
                    pythonPackage = False
                    skynetPackage = False
                    hsdPackage = False
                    pdnsPackage = True       # Toggle to install PowerDNS and Dependencies
                    print(colours.red(self, "\nInstalling PowerDNS..."))

                    self.addPDNSSources()
                    self.checkResolver()

                elif package.startswith("# EOF"):
                    runInstall = False

                elif winPackage is True:
                    break

                elif linuxPackage is True:

                    if package is not "":
                        print(colours.green(self, " [+] ") + "Installing " + str(package))
                        subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
                        print()
            # Install Python Packages
                elif pythonPackage is True:

                    if package is not "":
                        print(colours.green(self, " [+] ") + "Installing " + str(package))
                        subprocess.run(["pip", "install", package], check=True)
                        print()

            # Install Skynet Webportal
                elif skynetPackage is True:

                    if package is not "":
                        if package.endswith("skynet-webportal.git"):
                            if os.path.isdir(self.SKYNET_PATH) is False:
                                print(colours.green(self, " [+] ") + "Installing Skynet Webportal")
                                subprocess.run(["git", "clone", package], cwd=self.PATH, check=True)
                                subprocess.run(["npm", "install", "yarn"], cwd=(self.SKYNET_PATH + "/packages/website"))
                                subprocess.run(["yarn", "build"], cwd=(self.SKYNET_PATH + "/packages/website"))
                                print()
                            else:
                                print(colours.yellow(self, " [!] ") + "Skynet Webportal Installation Detected!")

                        elif package.endswith("ansible-playbooks.git"):
                            if os.path.isdir(self.ANSIBLE_PLAYBOOKS_PATH) is False:
                                print(colours.green(self, " [+] ") + "Installing Ansible-Playbooks")
                                subprocess.run(["git", "clone", package], cwd=self.PATH, check=True)
                                print()
                            else:
                                print(colours.yellow(self, " [!] ") + "Ansible-Playbooks Installation Detected!")
                                
                        elif package.endswith("ansible-private-sample.git"):
                            if os.path.isdir(self.ANSIBLE_PRIVATE_PATH) is False:
                                print(colours.green(self, " [+] ") + "Installing Ansible-Private")
                                subprocess.run(["git", "clone", package, "ansible-private"], cwd=self.PATH, check=True)
                                print()
                            else:
                                print(colours.yellow(self, " [!] ") + "Ansible-Private Installation Detected!")
            # Install Handshake Daemon
                elif hsdPackage is True:
                    if package is not "":
                        if package.endswith("hsd.git"):
                            if os.path.isdir(self.HSD_PATH) is False:
                                print(colours.green(self, " [+] ") + "Installing Handshake Daemon")
                                subprocess.run(["git", "clone", package], cwd=self.PATH, check=True)
                                subprocess.run(["npm", "install", "--production"], cwd=self.HSD_PATH)
                                print()
                            else:
                                print(colours.yellow(self, " [!] ") + "Handshake Daemon Installation Detected!")

                elif pdnsPackage is True:
                    if package is not "":
                        print(colours.green(self, " [+] ") + "Installing " + str(package))
                        subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
                        print()
                                
        # Install packages for Windows
        elif platform is "win32":
            #logging.basicConfig(filename=self.LOG_FILE, level=logging.DEBUG)
            
            runInstall = True

            # Install Dependencies
            while(runInstall is True):
                package = DEPENDS.readline().replace("\n", "")

                if package.startswith("# WINDOWS"):
                    winPackage = True       # Toggle to install Windows Dependencies
                    linuxPackage = False
                    macOSPackage = False
                    pythonPackage = False
                    skynetPackage = False
                    hsdPackage = False
                    pdnsPackage = False

                elif package.startswith("# LINUX"):
                    winPackage = False
                    linuxPackage = False      # Toggle to install Linux Dependencies
                    macOSPackage = False
                    pythonPackage = False
                    skynetPackage = False
                    hsdPackage = False
                    pdnsPackage = False
                    print(colours.red(self, "Installing Linux Dependencies..."))

                elif package.startswith("# MACOS"):
                    winPackage = False
                    linuxPackage = False
                    macOSPackage = False      # Toggle to install Linux Dependencies
                    pythonPackage = False
                    skynetPackage = False
                    hsdPackage = False
                    pdnsPackage = False
                    print(colours.red(self, "Installing MacOS Dependencies..."))

                elif package.startswith("# PYTHON"):
                    winPackage = False
                    linuxPackage = False
                    macOSPackage = False
                    pythonPackage = True     # Toggle to install Python Dependencies
                    skynetPackage = False
                    hsdPackage = False
                    pdnsPackage = False
                    print(colours.red(self, "\nInstalling Python Dependencies..."))
                    
                elif package.startswith("# SKYNET"):
                    winPackage = False
                    linuxPackage = False
                    macOSPackage = False
                    pythonPackage = False
                    skynetPackage = True     # Toggle to install Skynet-Webportal and Dependencies
                    hsdPackage = False
                    pdnsPackage = False
                    print(colours.red(self, "\nInstalling Skynet-Webportal..."))
                    runInstall
                elif package.startswith("# HSD"):
                    winPackage = False
                    linuxPackage = False
                    pythonPackage = False
                    skynetPackage = False
                    hsdPackage = True        # Toggle to install HNS Node and Dependencies
                    pdnsPackage = False
                    print(colours.red(self, "\nInstalling Handshake Daemon..."))
                    
                elif package.startswith("# PDNS"):
                    winPackage = False
                    linuxPackage = False
                    macOSPackage = False
                    pythonPackage = False
                    skynetPackage = False
                    hsdPackage = False
                    pdnsPackage = True       # Toggle to install PowerDNS and Dependencies
                    print(colours.red(self, "\nInstalling PowerDNS..."))

                    self.addPDNSSources()
                    self.checkResolver()

                elif package.startswith("# EOF"):
                    runInstall = False

                elif winPackage is True:
                    if package is not "":
                        print(colours.green(" [+] ") + "Installing Windows Dependency: ", str(package))
                        # Install Windows Dependencies
                        print()

                elif linuxPackage is True:
                    break

                elif macOSPackage is True:
                    break

                elif linuxPackage is True:
                    break
        
        print(colours.red("\n[!] ") + "Please restart device to apply final changes.")
        print("\nPress any key to continue...")
        getch()
#################################################### END: __init__(self)

    def addPDNSSources(self):
        # Check for existing PowerDNS APT sources
        hasSource = False

        if os.path.exists("/etc/apt/sources.list.d/pdns.list"):
           
            with open('/etc/apt/sources.list.d/pdns.list') as sourceFile:
                sources = sourceFile.readlines()

            for line in sources:
                # If PowerDNS APT source does not exist, add it to /etc/apt/sources.list.d/pdns.list
                if 'http://repo.powerdns.com/ubuntu' in line:
                    hasSource = True

        if hasSource is False:
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
            if line is "DNS=1.1.1.1":
                dnsExists = True

            if line is "DNSStubListener=no":
                stubListenterExists = True

        # Add configurations to resolved.conf
        if dnsExists is False or stubListenterExists is False:
            addLine = "# A.D.A.M.S. PowerDNS Configurations"
            subprocess.run(["sudo", "sh", "-c", addLine], check=True)
            NEED_RESTART = True

        if dnsExists is False:
            addLine = "echo 'DNS=1.1.1.1' >> /etc/systemd/resolved.conf"
            subprocess.run(["sudo", "sh", "-c", addLine], check=True)

        if stubListenterExists is False:
            addLine = "echo 'DNSStubListener=no' >> /etc/systemd/resolved.conf"
            subprocess.run(["sudo", "sh", "-c", addLine], check=True)

        # Create Symlink
        subprocess.run(["sudo", "ln", "-sf", "/run/systemd/resolve/resolv.conf", "/etc/resolv.conf"], check=True)
#################################################### END: checkResolver(self)

    def clear_screen(self):
        os.system('cls' if os.name is 'nt' else 'clear')
#################################################### END: clear_screen()
