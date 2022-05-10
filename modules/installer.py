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
from display import clear_screen

class install:
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
        #print(colours().error("install() method not complete."))
        #sleep(1)
        self.run()

    def run(self):

        DEPENDS = open("./DEPENDS", "r")
        setInstall = False
        addWinPackage = False
        addLinuxPackage = False
        addPythonPackage = False
        addSkynetPackage = False
        addHNSPackage = False
        addNGINXPackage = False
        addPDNSPackage = False

        clear_screen()

        try:
            # Install packages for Linux
            if platform == "linux":
                #logging.basicConfig(filename=self.LOG_FILE, level=logging.DEBUG)
                
                setInstall = True

                # Install Dependencies
                while(setInstall == True):
                    package = DEPENDS.readline().replace("\n", "")

                    if package.startswith("# WINDOWS"):
                        addWinPackage = False           # Toggle to install Windows Dependencies
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = False
                        addHNSPackage = False
                        addNGINXPackage = False
                        addPDNSPackage = False

                    elif package.startswith("# LINUX"):
                        addWinPackage = False
                        addLinuxPackage = True         # Toggle to install Linux Dependencies
                        addPythonPackage = False
                        addSkynetPackage = False
                        addHNSPackage = False
                        addNGINXPackage = False
                        addPDNSPackage = False
                        print(colours.red(self, "Installing Linux Dependencies..."))

                    elif package.startswith("# PYTHON"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = True        # Toggle to install Python Dependencies
                        addSkynetPackage = False
                        addHNSPackage = False
                        addNGINXPackage = False
                        addPDNSPackage = False
                        print(colours.red(self, "\nInstalling Python Dependencies..."))
                        
                    elif package.startswith("# SKYNET"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = True        # Toggle to install Skynet Webportal
                        addHNSPackage = False
                        addNGINXPackage = False
                        addPDNSPackage = False
                        print(colours.red(self, "\nInstalling Skynet-Webportal..."))
                        
                    elif package.startswith("# HNS"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = False
                        addHNSPackage = True           # Toggle to install Handshake Daemon
                        addNGINXPackage = False
                        addPDNSPackage = False
                        print(colours.red(self, "\nInstalling HNS Node..."))
                        
                    elif package.startswith("# NGINX"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = False
                        addHNSPackage = False
                        addNGINXPackage = False           # Toggle to install NGINX
                        addPDNSPackage = False
                        print(colours.red(self, "\nInstalling NGINX..."))
                        
                    elif package.startswith("# PDNS"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = False
                        addHNSPackage = False
                        addNGINXPackage = False
                        addPDNSPackage = True           # Toggle to install PowerDNS
                        print(colours.red(self, "\nInstalling PowerDNS..."))

                        self.addPDNSSources()
                        self.checkResolver()

                    elif package.startswith("# EOF"):
                        setInstall = False

                # Install Windows Dependencies
                    elif addWinPackage == True:
                        break

                # Install Linux Dependencies
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

                # Install NGINX
                    elif addNGINXPackage == True:
                        if package != "":
                            print(colours.green(self, " [+] ") + "Installing " + str(package))
                            #subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
                            print()

                # Install PowerDNS
                    elif addPDNSPackage == True:
                        if package != "":
                            if package.endswith("tar.gz"):

                                if os.path.exists("./pdnsmanager") == False and os.path.exists("./" + package) == False:
                                    print(colours.green(self, " [+] ") + "Installing " + str(package))
                                    subprocess.run(["wget", "https://dl.pdnsmanager.org/" + package], cwd=self.PATH, check=True)

                                elif os.path.exists("./pdnsmanager") == False and os.path.exists("./" + package) == True:
                                    print(colours.green(self, " [+] ") + "Installing " + str(package))
                                    subprocess.run(["tar", "-xvf", package], cwd=self.PATH, check=True)
                                    subprocess.run(["mv", package[0:17], "pdnsmanager/"], cwd=self.PATH, check=True)
                                    subprocess.run(["rm", "-fr", package], cwd=self.PATH, check=True)
                                
                                else:
                                    print(colours.yellow(self, " [!] ") + "PowerDNS Manager Detected!")

                                print()
                            else:
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

                    if package.startswith("# WINDOWS"):
                        addWinPackage = True           # Toggle to install Windows Dependencies
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = False
                        addHNSPackage = False
                        addNGINXPackage = False
                        addPDNSPackage = False

                    elif package.startswith("# LINUX"):
                        addWinPackage = False
                        addLinuxPackage = False         # Toggle to install Linux Dependencies
                        addPythonPackage = False
                        addSkynetPackage = False
                        addHNSPackage = False
                        addNGINXPackage = False
                        addPDNSPackage = False
                        print(colours.red(self, "Installing Linux Dependencies..."))

                    elif package.startswith("# PYTHON"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = True        # Toggle to install Python Dependencies
                        addSkynetPackage = False
                        addHNSPackage = False
                        addNGINXPackage = False
                        addPDNSPackage = False
                        print(colours.red(self, "\nInstalling Python Dependencies..."))
                        
                    elif package.startswith("# SKYNET"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = True        # Toggle to install Skynet Webportal
                        addHNSPackage = False
                        addNGINXPackage = False
                        addPDNSPackage = False
                        print(colours.red(self, "\nInstalling Skynet-Webportal..."))
                        
                    elif package.startswith("# HNS"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = False
                        addHNSPackage = True           # Toggle to install Handshake Daemon
                        addNGINXPackage = False
                        addPDNSPackage = False
                        print(colours.red(self, "\nInstalling HNS Node..."))
                        
                    elif package.startswith("# NGINX"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = False
                        addHNSPackage = False
                        addNGINXPackage = True           # Toggle to install NGINX
                        addPDNSPackage = False
                        print(colours.red(self, "\nInstalling HNS Node..."))
                        
                    elif package.startswith("# PDNS"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = False
                        addHNSPackage = False
                        addNGINXPackage = False
                        addPDNSPackage = True           # Toggle to install PowerDNS
                        print(colours.red(self, "\nInstalling PowerDNS..."))

                        self.addPDNSSources()
                        self.checkResolver()

                    elif package.startswith("# EOF"):
                        setInstall = False

                # Install Windows Dependencies
                    elif addWinPackage == True:
                        
                        if package != "":
                            print(colours.green(self, " [+] ") + "Installing " + str(package))
                            # Install Windows Dependencies
                            print()

                # Install Linux Dependencies
                    elif addLinuxPackage == True:
                        break

                # Install Python Packages
                    elif addPythonPackage == True:

                        if package != "":
                            print(colours.green(self, " [+] ") + "Installing " + str(package))
                            # Install Windows Python Dependencies
                            print()

                # Install Skynet Webportal
                    elif addSkynetPackage == True:

                        if package != "":
                            # Install Windows Skynet Webportal
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
                            # Install Windows Handshake Daemon
                            if package.endswith("hsd.git"):
                                if os.path.isdir(self.HSD_PATH) == False:
                                    print(colours.green(self, " [+] ") + "Installing Handshake Daemon")
                                    subprocess.run(["git", "clone", package], cwd=self.PATH, check=True)
                                    subprocess.run(["npm", "install", "--production"], cwd=self.HSD_PATH)
                                    print()
                                else:
                                    print(colours.yellow(self, " [!] ") + "Handshake Daemon Installation Detected!")

                # Install NGINX
                    elif addNGINXPackage == True:
                        if package != "":
                            # Install Windows NGINX
                            print()

                # Install PowerDNS
                    elif addPDNSPackage == True:
                        if package != "":
                            print(colours.green(self, " [+] ") + "Installing " + str(package))
                            # Install Windows PowerDNS
                            print()

            print(colours.red(self, " [!] ") + "Please restart device to apply final changes.")
            print("\nPress any key to continue...")
            getch()
        except AttributeError as e:
            print(colours().error(str(e)))
            sleep(2)
            self.main_menu()
        except KeyboardInterrupt:
            from main import main as main
            main()
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

class reinstall:
    def __init__(self):
        print(colours.error(self, "reinstall method not yet complete."))
        sleep(1)
        from main import main as main
        main()
        
    def run(self):
        clear_screen()
        sleep(1)
    #################################################### END: __init__(self)