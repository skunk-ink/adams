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
import sys
import subprocess

from sys import platform
from time import sleep as sleep
from colours import colours
from display import clear_screen

if platform == "linux":
    from getch import getch as getch
elif platform == "win32":
    from msvcrt import getch as getch

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
        self.adams()
    #################################################### END: __init__(self)

    def adams(self):

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
                        sleep(1)

                    elif package.startswith("# PYTHON"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = True        # Toggle to install Python Dependencies
                        addSkynetPackage = False
                        addHNSPackage = False
                        addNGINXPackage = False
                        addPDNSPackage = False
                        print(colours.red(self, "\nInstalling Python Dependencies..."))
                        sleep(1)
                        
                    elif package.startswith("# HNS"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = False
                        addHNSPackage = True           # Toggle to install Handshake Daemon
                        addNGINXPackage = False
                        addPDNSPackage = False
                        print(colours.red(self, "\nInstalling HNS Node..."))
                        sleep(1)
                        
                    elif package.startswith("# PDNS"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = False
                        addHNSPackage = False
                        addNGINXPackage = False
                        addPDNSPackage = True           # Toggle to install PowerDNS
                        print(colours.red(self, "\nInstalling PowerDNS..."))
                        self.checkResolver()
                        self.addPDNSSources()
                        sleep(1)
                        
                    elif package.startswith("# NGINX"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = False
                        addHNSPackage = False
                        addNGINXPackage = False           # Toggle to install NGINX
                        addPDNSPackage = False
                        print(colours.red(self, "\nInstalling NGINX..."))
                        sleep(1)
                        
                    elif package.startswith("# SKYNET"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = False        # Toggle to install Skynet Webportal
                        addHNSPackage = False
                        addNGINXPackage = False
                        addPDNSPackage = False
                        print(colours.red(self, "\nInstalling Skynet-Webportal..."))
                        sleep(1)

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

                # Install Handshake Daemon
                    elif addHNSPackage == True:
                        if package != "":
                            if package.endswith("hsd.git"):
                                if os.path.isdir(self.HSD_PATH) == False:
                                    print(colours.green(self, " [+] ") + "Downloading Handshake Daemon")
                                    subprocess.run(["git", "clone", package], cwd=self.PATH, check=True)

                                    print(colours.green(self, " [+] ") + "Installing Handshake Daemon")
                                    subprocess.run(["npm", "install", "--production"], cwd=self.HSD_PATH)
                                    print()
                                else:
                                    print(colours.yellow(self, " [!] ") + "Handshake Daemon Installation Detected!")

                # Install PowerDNS
                    elif addPDNSPackage == True:

                        if package != "":
                            if package.endswith("tar.gz"):

                                if os.path.exists("./pdnsmanager") == False and os.path.exists("./" + package) == False:
                                    print(colours.green(self, " [+] ") + "Downloading PowerDNS Manager" + str(package))
                                    subprocess.run(["wget", "https://dl.pdnsmanager.org/" + package], cwd=self.PATH, check=True)

                                if os.path.exists("./pdnsmanager") == False and os.path.exists("./" + package) == True:
                                    print(colours.green(self, " [+] ") + "Extracting PowerDNS Manager " + str(package))
                                    subprocess.run(["tar", "-xvf", package], cwd=self.PATH, check=True)
                                    subprocess.run(["mv", package[0:17], "pdnsmanager/"], cwd=self.PATH, check=True)
                                    subprocess.run(["rm", "-fr", package], cwd=self.PATH, check=True)
                                
                                if os.path.exists("./pdnsmanager") == True:
                                    print(colours.green(self, " [+] ") + "Configuring PowerDNS Manager")
                             
                                print()
                            else:
                                print(colours.green(self, " [+] ") + "Installing " + str(package))
                                subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
                                print()

                # Install NGINX
                    elif addNGINXPackage == True:
                        if package != "":
                            print(colours.green(self, " [+] ") + "Installing " + str(package))
                            #subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
                            print()
                            
                # Install Skynet Webportal
                    elif addSkynetPackage == True:
                        if package != "":
                            if package.endswith("skynet-webportal.git"):
                                if os.path.isdir(self.SKYNET_PATH) == False:
                                    print(colours.green(self, " [+] ") + "Downloading Skynet Webportal")
                                    subprocess.run(["git", "clone", package], cwd=self.PATH, check=True)

                                    print(colours.green(self, " [+] ") + "Installing Yarn")
                                    subprocess.run(["npm", "install", "yarn"], cwd=(self.SKYNET_PATH + "/packages/website"))

                                    print(colours.green(self, " [+] ") + "Building Skynet Portal Page")
                                    subprocess.run(["yarn", "build"], cwd=(self.SKYNET_PATH + "/packages/website"))
                                    print()
                                else:
                                    print(colours.yellow(self, " [!] ") + "Skynet Webportal Installation Detected!")

                            elif package.endswith("ansible-playbooks.git"):
                                if os.path.isdir(self.ANSIBLE_PLAYBOOKS_PATH) == False:
                                    print(colours.green(self, " [+] ") + "Downloading Ansible-Playbooks")
                                    subprocess.run(["git", "clone", package], cwd=self.PATH, check=True)
                                    print()
                                else:
                                    print(colours.yellow(self, " [!] ") + "Ansible-Playbooks Installation Detected!")
                                    
                            elif package.endswith("ansible-private-sample.git"):
                                if os.path.isdir(self.ANSIBLE_PRIVATE_PATH) == False:
                                    print(colours.green(self, " [+] ") + "Downloading Ansible-Private")
                                    subprocess.run(["git", "clone", package, "ansible-private"], cwd=self.PATH, check=True)
                                    print()
                                else:
                                    print(colours.yellow(self, " [!] ") + "Ansible-Private Installation Detected!")

                            
            # Install packages for Windows
            elif platform == "win32":
                
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
                        
                    elif package.startswith("# HNS"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = False
                        addHNSPackage = True           # Toggle to install Handshake Daemon
                        addNGINXPackage = False
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
                        
                    elif package.startswith("# NGINX"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = False
                        addHNSPackage = False
                        addNGINXPackage = True           # Toggle to install NGINX
                        addPDNSPackage = False
                        print(colours.red(self, "\nInstalling HNS Node..."))
                        
                    elif package.startswith("# SKYNET"):
                        addWinPackage = False
                        addLinuxPackage = False
                        addPythonPackage = False
                        addSkynetPackage = True        # Toggle to install Skynet Webportal
                        addHNSPackage = False
                        addNGINXPackage = False
                        addPDNSPackage = False
                        print(colours.red(self, "\nInstalling Skynet-Webportal..."))

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

                # Install Handshake Daemon
                    elif addHNSPackage == True:
                        if package != "":
                            # Install Windows Handshake Daemon
                            if package.endswith("hsd.git"):
                                if os.path.isdir(self.HSD_PATH) == False:
                                    print(colours.green(self, " [+] ") + "Downloading Handshake Daemon")
                                    subprocess.run(["git", "clone", package], cwd=self.PATH, check=True)
                                    
                                    print(colours.green(self, " [+] ") + "Downloading Handshake Daemon")
                                    subprocess.run(["npm", "install", "--production"], cwd=self.HSD_PATH)
                                    print()
                                else:
                                    print(colours.yellow(self, " [!] ") + "Handshake Daemon Installation Detected!")

                # Install PowerDNS
                    elif addPDNSPackage == True:
                        if package != "":
                            print(colours.green(self, " [+] ") + "Installing " + str(package))
                            # Install Windows PowerDNS
                            print()

                # Install NGINX
                    elif addNGINXPackage == True:
                        if package != "":
                            # Install Windows NGINX
                            print()

                # Install Skynet Webportal
                    elif addSkynetPackage == True:

                        if package != "":
                            # Install Windows Skynet Webportal
                            if package.endswith("skynet-webportal.git"):
                                if os.path.isdir(self.SKYNET_PATH) == False:
                                    print(colours.green(self, " [+] ") + "Downloading Skynet Webportal")
                                    subprocess.run(["git", "clone", package], cwd=self.PATH, check=True)
                                    print(colours.green(self, " [+] ") + "Installing Yarn")
                                    subprocess.run(["npm", "install", "yarn"], cwd=(self.SKYNET_PATH + "/packages/website"))
                                    print(colours.green(self, " [+] ") + "Building Skynet Portal Page")
                                    subprocess.run(["yarn", "build"], cwd=(self.SKYNET_PATH + "/packages/website"))
                                    print()
                                else:
                                    print(colours.yellow(self, " [!] ") + "Skynet Webportal Installation Detected!")

                            elif package.endswith("ansible-playbooks.git"):
                                if os.path.isdir(self.ANSIBLE_PLAYBOOKS_PATH) == False:
                                    print(colours.green(self, " [+] ") + "Downloading Ansible-Playbooks")
                                    subprocess.run(["git", "clone", package], cwd=self.PATH, check=True)
                                    print()
                                else:
                                    print(colours.yellow(self, " [!] ") + "Ansible-Playbooks Installation Detected!")
                                    
                            elif package.endswith("ansible-private-sample.git"):
                                if os.path.isdir(self.ANSIBLE_PRIVATE_PATH) == False:
                                    print(colours.green(self, " [+] ") + "Downloading Ansible-Private")
                                    subprocess.run(["git", "clone", package, "ansible-private"], cwd=self.PATH, check=True)
                                    print()
                                else:
                                    print(colours.yellow(self, " [!] ") + "Ansible-Private Installation Detected!")

            print(colours.red(self, " [!] ") + "Please restart device to apply final changes.")
            print("\nPress any key to continue...")
            getch()
        except AttributeError as e:
            print(colours().error(str(e)))
            sleep(2)
            self.main_menu()
        except KeyboardInterrupt:
            from main import main as main
            cli()
    #################################################### END: adams(self)

    def addPDNSSources(self):
        hasRepo = False
        hasPackage = False

        # Check for existing PowerDNS APT sources
        if os.path.exists("/etc/apt/sources.list.d/pdns.list"):

            with open('/etc/apt/sources.list.d/pdns.list') as sourceFile:
                sources = sourceFile.readlines()

            for line in sources:
                if 'http://repo.powerdns.com/ubuntu' in line:
                    hasRepo = True

                if 'Package: pdns-*\nPin: origin repo.powerdns.com\nPin-Priority: 600' in line:
                    hasPackage = True

        if hasRepo is False:
            print(colours.green(self, " [+] ") + "Adding PowerDNS Sources...")
            addSource = "echo 'deb [arch=amd64] http://repo.powerdns.com/ubuntu focal-auth-46 main' > /etc/apt/sources.list.d/pdns.list"
            subprocess.run(["sudo", "sh", "-c", addSource], cwd=self.PATH, check=True)
            print()

        if hasPackage is False:
            addSource = "echo 'Package: pdns-*\nPin: origin repo.powerdns.com\nPin-Priority: 600' > /etc/apt/preferences.d/pdns"
            subprocess.run(["sudo", "sh", "-c", addSource], cwd=self.PATH, check=True)
            
        print(colours.green(self, " [+] ") + "Adding APT-KEY...")
        subprocess.run(["wget", "https://repo.powerdns.com/FD380FBB-pub.asc"], cwd=self.PATH, check=True)
        subprocess.run(["sudo", "apt-key", "add", "FD380FBB-pub.asc"], cwd=self.PATH, check=True)
        subprocess.run(["rm", "-fr", "FD380FBB-pub.asc"], cwd=self.PATH, check=True)
        subprocess.run(["sudo", "apt", "update"], cwd=self.PATH, check=True)
        print()
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
        print(colours.green(self, " [+] ") + "Disabling Stub Resolver...")
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
        print()
        # Create Symlink
        print(colours.green(self, " [+] ") + "Creating Symlink")
        subprocess.run(["sudo", "ln", "-sf", "/run/systemd/resolve/resolv.conf", "/etc/resolv.conf"], check=True)
    #################################################### END: checkResolver(self)

    def reinstall(self):
        print(colours.error(self, "reinstall() method not yet complete."))
        sleep(1)
    #################################################### END: reinstall(self)

    def skynet_webportal(self):
        print(colours.error(self, "skynet_webportal() method not yet complete."))
        sleep(1)
    #################################################### END: skynet_webportal(self)

    def hsd(self):
        print(colours.error(self, "hsd() method not yet complete."))
        sleep(1)
    #################################################### END: hsd(self)

    def pdns(self):
        print(colours.error(self, "pdns() method not yet complete."))
        sleep(1)
    #################################################### END: pdns(self)

    def nginx(self):
        print(colours.error(self, "nginx() method not yet complete."))
        sleep(1)
    #################################################### END: nginx(self)

class cli:
    menu_title = ""
    menu_options = ""

    def __init__(self):
        clear_screen()
        self.set_menu("MAIN")
        self.main_menu()
        sleep(1)
    #################################################### END: __init__(self)

    def get_input(self, prompt):
        user_input = input(colours().prompt(prompt))
        return user_input         
    #################################################### END: get_input(prompt)

    def print_header(self):
        clear_screen()  # Clear console window
        print(colours().title("\n\t" + menu_title[1] + "\n\n"))   # Print menu title
    #################################################### END: print_header()

    def print_options(self):
        for option in menu_options:     # Print menu options to screen
            print("\t    " + option)
        print()
    #################################################### END: print_options()

    def set_menu(self, menu_id):
        global menu_title
        global menu_options
        
        if menu_id.upper() == "MAIN":       # Main Menu Options
            menu_title = ["ADAMS_INSTALLER",
                          "A.D.A.M.S. Installer"]
                          
            menu_options = [colours().cyan("1") + ": Install A.D.A.M.S.",
                            colours().cyan("2") + ": Install Skynet Webportal",
                            colours().cyan("3") + ": Install Handshake Daemon",
                            colours().cyan("4") + ": Install PowerDNS",
                            colours().cyan("5") + ": Install NGINX Webserver",
                            "",
                            colours().cyan("B") + ": Back to A.D.A.M.S.",
                            colours().cyan("Q") + ": Quit A.D.A.M.S."]
    #################################################### END: set_menu(menu_id)

    def main_menu(self):
        self.set_menu("MAIN")    # Initialize A.D.A.M.S. Installer Menu
        
        try:
            while True: # Display A.D.A.M.S. Installer Menu
                self.print_header()
                self.print_options()
                
                user_input = self.get_input("\n\tWhat would you like to do? : ")
                
                if user_input.upper() == "1":   # Install A.D.A.M.S.
                    install.adams(self)

                elif user_input.upper() == "2": # Install Skynet Webportal
                    install.skynet_webportal(self)

                elif user_input.upper() == "3": # Install Handshake Daemon
                    install.hsd(self)

                elif user_input.upper() == "4": # Install PowerDNS
                    install.pdns(self)

                elif user_input.upper() == "5": # Install NGINX Webserver
                    install.nginx(self)
                    
                elif user_input.upper() == "B":
                    from main import main as main
                    main()

                elif user_input.upper() == "EXIT" or user_input.upper() == "Q" or user_input.upper() == "QUIT":
                    clear_screen()    # Clear console window
                    sys.exit(0)

        except AttributeError as e:
            print(colours().error(str(e)))
            sleep(2)
            self.main_menu()
        except KeyboardInterrupt:
            from main import main as main
            main()
    #################################################### END: main_menu()

if __name__ == '__main__':
    os.system('cls')
    print(colours.error("installer.py not yet complete."))
    cli()
    sleep(1)
#################################################### END: __main__
