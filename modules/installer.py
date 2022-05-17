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

from faulthandler import disable
import os
import sys
import subprocess
import json

from sys import platform
from urllib.parse import urlparse
from time import sleep as sleep
from colours import colours
from display import clear_screen

disableInstaller = False            # Disable all install methods
disableSubprocesses = False         # Ghost run, does not affect the system
disableDependencyInstall = False    # Disable dependency check on all install methods
disableLogging = False              # Disable console logs

# Load configurations file
with open("./config/adams.conf") as configFile:
    lines = configFile.readlines()

for line in lines:
    if line.startswith("#") or line == "":
        pass
    else:
        config = line.split(":")
        i = 0

        for value in config:
            config[i] = value.strip().lower()
            i += 1

        if config[0] == "disablelogging":
            if config[1].lower() == "false":
                disableLogging = False
            else:
                disableLogging = True

            if disableLogging == False:
                print("Disable Logging: " + str(disableLogging))
                sleep(1)

        elif config[0] == "disablesubprocesses":
            if config[1].lower() == "false":
                disableSubprocesses = False
            else:
                disableSubprocesses = True
                
            if disableLogging == False:
                print("Disable Subprocesses: " + str(disableSubprocesses))
                sleep(1)

        elif config[0] == "disableinstallmethods":
            if config[1].lower() == "false":
                disableInstaller = False
            else:
                disableInstaller = True
                
            if disableLogging == False:
                print("Disable Install Methods: " + str(disableInstaller))
                sleep(1)

        elif config[0] == "disabledependencyinstall":
            if config[1].lower() == "false":
                disableDependencyInstall = False
            else:
                disableDependencyInstall = True
                
            if disableLogging == False:
                print("Disable Dependencies: " + str(disableDependencyInstall))
                sleep(1)

if platform == "linux":
    from getch import getch as getch
elif platform == "win32":
    from msvcrt import getch as getch

class install:
    NEED_RESTART = False
    PATH = os.getcwd()                                      # A.D.A.M.S. directory
    HSD_INSTALL_PATH = "/usr/local/sbin/"                   # HSD installation directory
    HSD_PATH = PATH + "/hsd/"                               # Handshake directory
    HSD_BIN_PATH = PATH + "/hsd/bin/hsd/"                   # Handshake binaries build directory
    HSD_SERVICE_SCRIPT = PATH + "/config/hsd.service"       # Premade Handshake daemon service script
    HSD_SYS_SERVICES_PATH = "/etc/systemd/system/"    # Location of system services
    SKYNET_PATH = PATH + "/skynet-webportal/"               # Skynet Webportal directory
    ANSIBLE_PLAYBOOKS_PATH = PATH + "/ansible-playbooks/"   # Ansible Playbooks directory
    ANSIBLE_PRIVATE_PATH = PATH + "/ansible-private/"       # Ansible Private directory
    POWERDNS_PATH = PATH + "/pdns/"                         # PowerDNS directory
    POWERDNS_CONF_PATH = "/etc/powerdns/pdns.conf"          # PowerDNS configuration file
    POWERDNS_CONF_FILE = PATH + "/config/pdns.conf"         # Premade PowerDNS configuration file

    def __init__(self, type):

        self.NEED_RESTART = False

        try:
            if type == "adams":
                print(colours.red(self, "\nInstalling A.D.A.M.S."))

                if disableDependencyInstall == False:
                    self.installDepends(self.getDependencies(sys.platform, "all"))

                self.handshake()
                self.powerdns()
                self.nginx()
                self.skynet_webportal()
                print(colours.prompt(self, "\n A.D.A.M.S. install complete! Press any key to continue."))
                getch()

            elif type == "skynet-webportal":
                print(colours.red(self, "\nInstalling Skynet Webportal"))

                if disableDependencyInstall == False:
                    self.installDepends(self.getDependencies(sys.platform, "skynet-webportal"))

                self.skynet_webportal()
                print(colours.prompt(self, "\n Skynet Webportal install complete! Press any key to continue."))
                getch()

            elif type == "handshake":
                print(colours.red(self, "\nInstalling Handshake Daemon"))

                if disableDependencyInstall == False:
                    self.installDepends(self.getDependencies(sys.platform, "handshake"))

                self.handshake()
                print(colours.prompt(self, "\n Handshake Daemon install complete! Press any key to continue."))
                getch()

            elif type == "powerdns":
                print(colours.red(self, "\nInstalling PowerDNS"))

                if disableDependencyInstall == False:
                    self.installDepends(self.getDependencies(sys.platform, "powerdns"))

                self.powerdns()
                print(colours.prompt(self, "\n PowerDNS install complete! Press any key to continue."))
                getch()

            elif type == "nginx":
                print(colours.red(self, "\nInstalling NGINX Webserver"))

                if disableDependencyInstall == False:
                    self.installDepends(self.getDependencies(sys.platform, "nginx"))

                self.nginx()
                print(colours.prompt(self, "\n NGINX install complete! Press any key to continue."))
                getch()

            if self.NEED_RESTART == True:
                print(colours.yellow(self, "\n [!]") + " RESTART NEEDED: Type 'yes' to reboot now, or 'no' to return to menu")
                userInput = cli.get_input(self, "\n\tWould you like to restart now? : ")
                if userInput.lower() == "yes":
                    if disableLogging == False:
                        print(colours.yellow(self, "\n [!] ") + "Reboot initiated...")
                        sleep(1)

                    if disableSubprocesses == False:
                        subprocess.run(["sudo", "reboot", "now"], check=True)
                    else:
                        print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")
        except KeyboardInterrupt:
            from main import main
            main()
    #################################################### END: __init__(self, type)

    def getDependencies(self, sysPlatform, depends):

        dependencies = {}

        if depends == "":
            depends = "all"

        sysPlatform = sysPlatform.lower()
        depends = depends.lower()

        # Parse DEPENDS.json
        with open("DEPENDS.json") as depends_json:
            data = json.load(depends_json)
            for platform in data:

                # Get Windows dependencies
                if platform.lower() == "windows" and sysPlatform == "win32":
                    for packageType in data[platform]:
                        if packageType == "exec":
                            for package in packageType:
                                try:
                                    dependencies["exec"].append(package)
                                except KeyError:
                                    dependencies["exec"] == []
                                    dependencies["exec"].append(package)

                # Get Linux dependencies
                elif platform.lower() == "linux" and sysPlatform == "linux":
                    for packageType in data[platform]:
                        for packages in packageType:
                            for package in packageType[packages]:
                                try:
                                    dependencies[packages].append(package)
                                except KeyError:
                                    dependencies[packages] = []
                                    dependencies[packages].append(package)

                # Get Skynet Webportal dependencies
                elif platform.lower() == "skynet-webportal":
                    if depends == "all" or depends == "skynet-webportal":
                        for packageType in data[platform]:
                            for packages in packageType:
                                for package in packageType[packages]:
                                    exists = False
                                    try:
                                        if packages in dependencies[packages]:
                                            exists = True

                                        if exists == False:
                                                dependencies[packages].append(package)
                                    except KeyError:
                                        dependencies[packages] = []
                                        dependencies[packages].append(package)

                # Get Handshake dependencies
                elif platform.lower() == "handshake":
                    if depends == "all" or depends == "handshake":
                        for packageType in data[platform]:
                            for packages in packageType:
                                for package in packageType[packages]:
                                    exists = False
                                    try:
                                        if package in dependencies[packages]:
                                            exists = True

                                        if exists == False:
                                                dependencies[packages].append(package)
                                    except KeyError:
                                        dependencies[packages] = []
                                        dependencies[packages].append(package)

                # Get PowerDNS dependencies
                elif platform.lower() == "powerdns":
                    if depends == "all" or depends == "powerdns":
                        for packageType in data[platform]:
                            for packages in packageType:
                                for package in packageType[packages]:                                
                                    exists = False
                                    try:
                                        if package in dependencies[packages]:
                                            exists = True

                                        if exists == False:
                                                dependencies[packages].append(package)
                                    except KeyError:
                                        dependencies[packages] = []
                                        dependencies[packages].append(package)

                # Get NGINX dependencies
                elif platform.lower() == "nginx":
                    if depends == "all" or depends == "nginx":
                        for packageType in data[platform]:
                            for packages in packageType:
                                for package in packageType[packages]:                                
                                    exists = False
                                    try:
                                        if package in dependencies[packages]:
                                            exists = True

                                        if exists == False:
                                                dependencies[packages].append(package)
                                    except KeyError:
                                        dependencies[packages] = []
                                        dependencies[packages].append(package)

        # Discard un-needed dependencies for platform
        if sysPlatform == "win32":
            try:
                del dependencies["apt"]
            except KeyError:
                pass
        elif sysPlatform == "linux":
            try:
                del dependencies["exe"]
            except KeyError:
                pass

        return dependencies
    #################################################### END: getDependencies(self, sysPlatform, depends)

    def printDepends(self, depends):
        clear_screen()
        print(colours.yellow(self, " [!]") + " The following dependencies will be installed:")

        columns = 0
        packages = ""

        for packageType in depends:
            if packageType == "exe":
                print(colours.green(self, "\n  -- Windows Executable --"))

            elif packageType == "apt":
                print(colours.green(self, "\n  -- Linux APT Package --"))

            elif packageType == "pip":
                print(colours.green(self, "\n  -- Python Package --"))

            elif packageType == "git":
                print(colours.green(self, "\n  -- Github Repository --"))

            elif packageType == "npm":
                print(colours.green(self, "\n  -- Node Package --"))

            elif packageType == "wget":
                print(colours.green(self, "\n  -- WGET (HTTPS) --"))

            count = len(depends[packageType])

            for package in depends[packageType]:
                if len(package.strip()) <= 26:
                    while len(package) < 27:
                        package += " "

                packages += package

                columns += 1
                count -= 1

                if count == 0 or len(package) > 30:
                    print("\t" + packages)
                    packages = ""
                    columns = 0
                elif columns == 4:
                    print("\t" + packages)
                    columns = 0
                    packages = ""
        
        print()
        print(colours.prompt(self, "Press any key to continue, or 'ctrl+c' to return to main menu."))
        getch()
    #################################################### END: printDepends(self, depends)

    def installDepends(self, depends):
        self.printDepends(depends)

        # If installing PowerDNS check for APT sources
        if "pdns-server" in depends["apt"]:
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

            # If PowerDNS APT sources do not exists, create them
            if hasRepo is False:
                print(colours.green(self, "\n [+] ") + "Adding PowerDNS sources...")
                addSource = "echo 'deb [arch=amd64] http://repo.powerdns.com/ubuntu focal-auth-46 main' > /etc/apt/sources.list.d/pdns.list"
                if disableSubprocesses == False:
                    subprocess.run(["sudo", "sh", "-c", addSource], cwd=self.PATH, check=True)
                else:
                    print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")
                print()
            else:
                print(colours.yellow(self, "\n [!] ") + "Existing PowerDNS sources found")

            if hasPackage is False:
                addSource = "echo 'Package: pdns-*\nPin: origin repo.powerdns.com\nPin-Priority: 600' > /etc/apt/preferences.d/pdns"
                if disableSubprocesses == False:
                    subprocess.run(["sudo", "sh", "-c", addSource], cwd=self.PATH, check=True)
                else:
                    print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")
            else:
                print(colours.yellow(self, "\n [+] ") + "Existing PowerDNS sources found...")


            if hasRepo is False or hasPackage is False:    
                # Downloaded and add PowerDNS APT Key
                print(colours.green(self, "\n [+] ") + "Adding APT-KEY...")
                if disableSubprocesses == False:
                    subprocess.run(["wget", "https://repo.powerdns.com/FD380FBB-pub.asc"], cwd=self.PATH, check=True)
                    subprocess.run(["sudo", "apt-key", "add", "FD380FBB-pub.asc"], cwd=self.PATH, check=True)
                    subprocess.run(["rm", "-fr", "FD380FBB-pub.asc"], cwd=self.PATH, check=True)
                    subprocess.run(["sudo", "apt", "update"], cwd=self.PATH, check=True)
                    print()
                else:
                    print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")

        for packageType in depends:
            # Install Windows Executable
            if packageType == "exe":
                print(colours.red(self, "\n\n  -- Installing Windows Executables --"))
                for package in depends[packageType]:
                    package = str(package).strip()
                    print(colours.green(self, "\n [+] ") + "Installing '" + package + "'...")
                    pass

            # Install Linux APT Package
            elif packageType == "apt":
                print(colours.red(self, "\n\n  -- Installing Linux APT Packages --"))
                for package in depends[packageType]:
                    package = str(package).strip()
                    print(colours.green(self, "\n [+] ") + "Installing '" + package + "'...")
                    if disableSubprocesses == False:
                        subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
                    else:
                        print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")

            # Install Python Packages
            elif packageType == "pip":
                print(colours.red(self, "\n\n  -- Installing Python Packages --"))
                for package in depends[packageType]:
                    package = str(package).strip()
                    print(colours.green(self, "\n [+] ") + "Installing '" + package + "'...")
                    if disableSubprocesses == False:
                        subprocess.run(["pip", "install", package], check=True)
                    else:
                        print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")

            # Clone Github Repository
            elif packageType == "git":
                print(colours.red(self, "\n\n  -- Cloning Github Repositories --"))
                for package in depends[packageType]:
                    packageName = self.parseURL(package)
                    if os.path.exists(self.PATH + "/" + packageName[:-4]) == False:
                        print(colours.green(self, "\n [+] ") + "Cloning '" + str(package) + "'...")
                        if disableSubprocesses == False:
                            subprocess.run(["git", "clone", package], cwd=self.PATH, check=True)
                        else:
                            print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")
                    else:
                        print(colours.yellow(self, "\n [+] ") + "Existing '" + packageName + "' repository found")

            # Install Node Package
            elif packageType == "npm":
                print(colours.red(self, "\n\n  -- Installing Node Packages --"))
                for package in depends[packageType]:
                    package = str(package).strip()
                    print(colours.green(self, "\n [+] ") + "Installing '" + package + "'...")
                    if disableSubprocesses == False:
                        subprocess.run(["npm", "install", package], cwd=self.PATH, check=True)
                    else:
                        print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")

            # Download/Install WGET Package
            elif packageType == "wget":
                print(colours.red(self, "\n\n  -- Installing WGET Packages --"))
                for package in depends[packageType]:
                    package = str(package).strip()
                    packageName = self.parseURL(package)
                    if os.path.isfile(self.PATH + "/" + packageName) == False:
                        print(colours.green(self, "\n [+] ") + "Downloading '" + str(packageName) + "'...")
                        if disableSubprocesses == False:
                            subprocess.run(["wget", package], cwd=self.PATH, check=True)
                        else:
                            print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")
                    else:
                        print(colours.yellow(self, "\n [+] ") + "Existing '" + packageName + "' package found")

                    if str(package).endswith("tar.gz"):
                        
                        if os.path.isfile(self.PATH + "/" + packageName) == True and os.path.isdir(self.PATH + "/" + packageName[-6:]) == False:
                            print("\t Unpacking '" + str(packageName) + "'...")
                            if disableSubprocesses == False:
                                subprocess.run(["tar", "-xvf", packageName], cwd=self.PATH, check=True)
                            else:
                                print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")
                            print("\t Cleaning up '" + str(packageName) + "'...")
                            if disableSubprocesses == False:
                                subprocess.run(["rm", "-fr", packageName], cwd=self.PATH, check=True)
                            else:
                                print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")
                        else:
                            print(colours.yellow(self, "\n [+] ") + "Existing '" + packageName[:-6] + "' directory found")
    #################################################### END: installDepends(self, depends)

    def skynet_webportal(self):
        print(colours.error(self, "skynet_webportal() method not yet complete."))
        sleep(1)

        """ print(colours.green(self, " [+] ") + "Installing Yarn")
        if disableSubprocesses == False:
            subprocess.run(["npm", "install", "yarn"], cwd=(self.SKYNET_PATH + "/packages/website"))
        else:
            print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")

        print(colours.green(self, " [+] ") + "Building Skynet Portal Page")
        if disableSubprocesses == False:
            subprocess.run(["yarn", "build"], cwd=(self.SKYNET_PATH + "/packages/website"))
        else:
            print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")
        print() """
    #################################################### END: skynet_webportal(self)

    def handshake(self):
        print(colours.green(self, "\n [+] ") + "Installing Handshake Daemon")

        if disableSubprocesses == False:
            # Build HSD binaries
            subprocess.run(["npm", "install", "--production"], cwd=self.HSD_PATH, check=True)

            # Copy HSD binaries to '/usr/local/bin'
            subprocess.run(["sudo", "cp", "*", self.HSD_INSTALL_PATH], cwd=self.HSD_BIN_PATH, check=True)

            # Create HSD system service
            subprocess.run(["sudo", "cp", self.HSD_SERVICE_SCRIPT, self.HSD_SYS_SERVICES_PATH], check=True)

            # Set 'hsd.service' owner
            subprocess.run(["sudo", "chown", "root:root", self.HSD_SYS_SERVICES_PATH], check=True)

            # Set 'hsd.service' permissions
            subprocess.run(["sudo", "chmod", "777", self.HSD_SYS_SERVICES_PATH])

            # Enable 'hsd.service'
            subprocess.run(["sudo", "systemctl", "enable", "hsd"])
        else:
            print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")
        print()
    #################################################### END: hsd(self)

    def powerdns(self):
        files = os.listdir(self.PATH)
        checkFor = "pdnsmanager"

        print(colours.green(self, "\n [+] ") + "Configuring PowerDNS")
        print(colours.green(self, "\n [+] ") + "Installing PowerDNS Manager")

        for file in files:
            if checkFor in file:
                if disableSubprocesses == False:
                    subprocess.run(["mv", file, "pdnsmanager/"], cwd=self.PATH, check=True)
                else:
                    print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")

        # Check and disable existing stub resolver
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
        print(colours.green(self, "\n [+] ") + "Disabling Stub Resolver...")
        if dnsExists == False or stubListenterExists == False:
            addLine = "echo '# PowerDNS Configurations' >> /etc/systemd/resolved.conf"
            if disableSubprocesses == False:
                subprocess.run(["sudo", "sh", "-c", addLine], check=True)
            else:
                print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")

        if dnsExists == False:
            addLine = "echo 'DNS=1.1.1.1' >> /etc/systemd/resolved.conf"
            if disableSubprocesses == False:
                subprocess.run(["sudo", "sh", "-c", addLine], check=True)
            else:
                print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")

        if stubListenterExists == False:
            addLine = "echo 'DNSStubListener=no' >> /etc/systemd/resolved.conf"
            if disableSubprocesses == False:
                subprocess.run(["sudo", "sh", "-c", addLine], check=True)
            else:
                print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")
            print()

        # Create Symlink
        print(colours.green(self, "\n [+] ") + "Creating Symlink")
        if disableSubprocesses == False:
            subprocess.run(["sudo", "ln", "-sf", "/run/systemd/resolve/resolv.conf", "/etc/resolv.conf"], check=True)
        else:
            print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")

        # Configure pdns.conf file
        print(colours.green(self, "\n [+] ") + "Configuring '" + self.POWERDNS_CONF_PATH + "'")
        if disableSubprocesses == False:
            subprocess.run(["sudo", "rm", "-fr", self.POWERDNS_CONF_PATH], check=True)
            subprocess.run(["sudo", "cp", self.POWERDNS_CONF_FILE, self.POWERDNS_CONF_PATH], check=True)
        else:
            print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")
        
        # Set pdns.conf file permissions
        if disableSubprocesses == False:
            subprocess.run(["sudo", "chmod", "640", self.POWERDNS_CONF_PATH], check=True)
            subprocess.run(["sudo", "chown", "-R", "root:pdns", self.POWERDNS_CONF_PATH], check=True)
        else:
            print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")


        # Initialize the sqlite database with schema
        if disableSubprocesses == False:
            os.system("sudo sqlite3 /var/lib/powerdns/pdns.sqlite3 < /usr/share/doc/pdns-backend-sqlite3/schema.sqlite3.sql")

        # Change ownership of the directory to the `pdns` user and group
        if disableSubprocesses == False:
            subprocess.run(["sudo", "chown", "-R", "pdns:pdns", "/var/lib/powerdns"], check=True)
        else:
            print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")

        self.NEED_RESTART = True


    #################################################### END: pdns(self)

    def nginx(self):
        print(colours.error(self, "nginx() method not yet complete."))
        sleep(1)
    #################################################### END: nginx(self)

    def parseURL(self, url):
        url = str(url).strip()
        charPos = 0
        count = 0
        nameLength = len(url)

        for character in url:
            if character == "/":
                charPos = count
            count += 1

        return url[(charPos + 1) - nameLength:]
    
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
                    if disableInstaller == False:
                        install("adams")
                    else:
                        print(colours.error(self, "adams() method not yet complete."))
                        sleep(1)

                elif user_input.upper() == "2": # Install Skynet Webportal
                    if disableInstaller == False:
                        install("skynet-webportal")
                    else:
                        print(colours.error(self, "skynet_webportal() method not yet complete."))
                        sleep(1)

                elif user_input.upper() == "3": # Install Handshake Daemon
                    if disableInstaller == False:
                        install("handshake")
                    else:
                        print(colours.error(self, "handshake() method not yet complete."))
                        sleep(1)

                elif user_input.upper() == "4": # Install PowerDNS
                    if disableInstaller == False:
                        install("powerdns")
                    else:
                        print(colours.error(self, "powerdns() method not yet complete."))
                        sleep(1)

                elif user_input.upper() == "5": # Install NGINX Webserver
                    if disableInstaller == False:
                        install("nginx")
                    else:
                        print(colours.error(self, "nginx() method not yet complete."))
                        sleep(1)
                    
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
    cli()
#################################################### END: __main__
