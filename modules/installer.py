'''               _                                    
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
'''

import os
import sys
import subprocess
import json

from sys import platform
from time import sleep as sleep
from colours import colours
from display import clear_screen

USER_DIR = os.path.expanduser('~')                  # User home directory
ADAMS_PATH = os.getcwd()                            # A.D.A.M.S. directory
ADAMS_CONFIG = ADAMS_PATH + '/config/adams.conf'    # Location of A.D.A.M.S. config

ENABLE_SUBPROCESSES = True                          # Ghost run, does not affect the system
ENABLE_DEPENDS = True                               # Enable dependency check on all install methods
ENABLE_LOGGING = False                              # Enable console logs

ENABLE_ADAMS = True                                 # Enable A.D.A.M.S. Installer
ENABLE_SKYNET = True                                # Enable Skynet Webportal Installer
ENABLE_HANDSHAKE = True                             # Enable Handshake Node Installer
ENABLE_POWERDNS = True                              # Enable PowerDNS Installer
ENABLE_NGINX = True                                 # Enable NGINX Installer

# Load configurations file
with open(ADAMS_CONFIG) as configFile:
    lines = configFile.readlines()

for line in lines:
    if line.startswith('#') or line == '':
        pass
    else:
        config = line.split(':')
        i = 0

        for value in config:
            config[i] = value.strip().lower()
            i += 1

        if config[0].lower() == 'enablelogging':
            if config[1].lower() == 'true':
                ENABLE_LOGGING = True
            else:
                ENABLE_LOGGING = False

            if ENABLE_LOGGING == True:
                print('Logging Enabled = : ' + str(ENABLE_LOGGING))
                sleep(1)

        elif config[0].lower() == 'enablesubprocesses':
            if config[1].lower() == 'true':
                ENABLE_SUBPROCESSES = True
            else:
                ENABLE_SUBPROCESSES = False
                
            if ENABLE_LOGGING == True:
                print('Subprocesses Enabled =  ' + str(ENABLE_SUBPROCESSES))
                sleep(1)

        elif config[0].lower() == 'enableadams':
            if config[1].lower() == 'true':
                ENABLE_ADAMS = True
            else:
                ENABLE_ADAMS = False
                
            if ENABLE_LOGGING == True:
                print('A.D.A.M.S. Enabled = ' + str(ENABLE_ADAMS))
                sleep(1)

        elif config[0].lower() == 'enableskynet':
            if config[1].lower() == 'true':
                ENABLE_SKYNET = True
            else:
                ENABLE_SKYNET = False
                
            if ENABLE_LOGGING == True:
                print('Skynet Webportal Enabled = ' + str(ENABLE_SKYNET))
                sleep(1)

        elif config[0].lower() == 'enablehandshake':
            if config[1].lower() == 'true':
                ENABLE_HANDSHAKE = True
            else:
                ENABLE_HANDSHAKE = False
                
            if ENABLE_LOGGING == True:
                print('Handshake Node Enabled = ' + str(ENABLE_HANDSHAKE))
                sleep(1)

        elif config[0].lower() == 'enablepowerdns':
            if config[1].lower() == 'true':
                ENABLE_POWERDNS = True
            else:
                ENABLE_POWERDNS = False
                
            if ENABLE_LOGGING == True:
                print('PowerDNS Enabled = ' + str(ENABLE_POWERDNS))
                sleep(1)

        elif config[0].lower() == 'enablenginx':
            if config[1].lower() == 'true':
                ENABLE_NGINX = True
            else:
                ENABLE_NGINX = False
                
            if ENABLE_LOGGING == True:
                print('NGINX Enabled = ' + str(ENABLE_NGINX))
                sleep(1)

        elif config[0].lower() == 'enabledependencyinstall':
            if config[1].lower() == 'true':
                ENABLE_DEPENDS = True
            else:
                ENABLE_DEPENDS = False
                
            if ENABLE_LOGGING == True:
                print('Disable Dependencies: ' + str(ENABLE_DEPENDS))
                sleep(1)

if platform == 'linux':
    from getch import getch as getch
elif platform == 'win32':
    from msvcrt import getch as getch

class install:
    """ NEED_RESTART = False
    ADAMS_PATH = os.getcwd()                                        # A.D.A.M.S. directory
    USER_DIR = os.path.expanduser('~')                              # User home directory """
    HSD_INSTALL_PATH = USER_DIR + '/.hsd'                           # HSD installation directory
    HSD_PATH = ADAMS_PATH + '/hsd'                                  # Handshake directory
    HSD_BIN_PATH = ADAMS_PATH + '/hsd/bin'                          # Handshake binaries build directory
    HSD_SERVICE_SCRIPT = ADAMS_PATH + '/config/hsd.service'         # Premade Handshake Node service script
    HSD_SYS_SERVICES_PATH = '/etc/systemd/system'                   # Location of system services
    HSD_CONFIG = ADAMS_PATH + '/config/hsd.conf'                    # Location of HSD node config
    HSW_CONFIG = ADAMS_PATH + '/config/hsw.conf'                    # Location of HSD wallet config
    SKYNET_PATH = ADAMS_PATH + '/skynet-webportal'                  # Skynet Webportal directory
    ANSIBLE_PLAYBOOKS_PATH = ADAMS_PATH + '/ansible-playbooks'      # Ansible Playbooks directory
    ANSIBLE_PRIVATE_PATH = ADAMS_PATH + '/ansible-private'          # Ansible Private directory
    POWERDNS_PATH = ADAMS_PATH + '/pdns'                            # PowerDNS directory
    POWERDNS_CONF_PATH = '/etc/powerdns/pdns.conf'                  # PowerDNS configuration file
    POWERDNS_CONF_FILE = ADAMS_PATH + '/config/pdns.conf'           # Premade PowerDNS configuration file

    def __init__(self, type):

        self.NEED_RESTART = False

        try:
            if type == 'adams':
                if ENABLE_ADAMS == True:
                    print(colours.red(self, '\nInstalling A.D.A.M.S.'))

                    self.installDepends(self.getDependencies(sys.platform, 'all'))

                    self.handshake()
                    self.powerdns()
                    self.nginx()
                    self.skynet_webportal()
                    print(colours.prompt(self, '\n A.D.A.M.S. install complete! Press any key to continue.'))
                    getch()
                else:
                    print(colours.error(self, 'A.D.A.M.S. installer has been disabled. See `config/adams.conf`'))
                    sleep(3)

            elif type == 'skynet-webportal':
                if ENABLE_SKYNET == True:
                    print(colours.red(self, '\nInstalling Skynet Webportal'))

                    self.installDepends(self.getDependencies(sys.platform, 'skynet-webportal'))

                    self.skynet_webportal()
                    print(colours.prompt(self, '\n Skynet Webportal install complete! Press any key to continue.'))
                    getch()
                else:
                    print(colours.error(self, 'Skynet Webportal installer has been disabled. See `config/adams.conf`'))
                    sleep(3)

            elif type == 'handshake':
                if ENABLE_HANDSHAKE == True:
                    print(colours.red(self, '\nInstalling Handshake Node'))

                    self.installDepends(self.getDependencies(sys.platform, 'handshake'))

                    self.handshake()
                    print(colours.prompt(self, '\n Handshake Node install complete! Press any key to continue.'))
                    getch()
                    from main import main
                    main(['adams', 'manage', 'handshake'])
                else:
                    print(colours.error(self, 'Handshake Node installer has been disabled. See `config/adams.conf`'))
                    sleep(3)

            elif type == 'powerdns':
                if ENABLE_POWERDNS == True:
                    print(colours.red(self, '\nInstalling PowerDNS'))

                    self.installDepends(self.getDependencies(sys.platform, 'powerdns'))

                    self.powerdns()
                    print(colours.prompt(self, '\n PowerDNS install complete! Press any key to continue.'))
                    getch()
                else:
                    print(colours.error(self, 'PowerDNS installer has been disabled. See `config/adams.conf`'))
                    sleep(3)

            elif type == 'nginx':
                if ENABLE_NGINX == True:
                    print(colours.red(self, '\nInstalling NGINX Webserver'))

                    self.installDepends(self.getDependencies(sys.platform, 'nginx'))

                    self.nginx()
                    print(colours.prompt(self, '\n NGINX install complete! Press any key to continue.'))
                    getch()
                else:
                    print(colours.error(self, 'NGINX installer has been disabled. See `config/adams.conf`'))
                    sleep(3)

            if self.NEED_RESTART == True:
                print(colours.yellow(self, '\n [!]') + ' RESTART NEEDED: Type "yes" to reboot now, or "no" to return to menu')
                userInput = cli.get_input(self, '\n\tWould you like to restart now? : ')
                if userInput.lower() == 'yes':
                    if ENABLE_LOGGING == True:
                        print(colours.yellow(self, '\n [!] ') + 'Reboot initiated...')
                        sleep(1)

                    if ENABLE_SUBPROCESSES == True:
                        subprocess.run(['sudo', 'reboot', 'now'], check=True)
                    else:
                        print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')
        except KeyboardInterrupt:
            import main
            main.main(['adams','main'])
    #################################################### END: __init__(self, type)

    def getDependencies(self, sysPlatform, depends):
        dependencies = {}

        if depends == '':
            depends = 'all'

        sysPlatform = sysPlatform.lower()
        depends = depends.lower()

        # Parse DEPENDS.json
        with open('DEPENDS.json') as depends_json:
            data = json.load(depends_json)
            for platform in data:

                # Get Windows dependencies
                if platform.lower() == 'windows' and sysPlatform == 'win32':
                    for packageType in data[platform]:
                        if packageType == 'exec':
                            for package in packageType:
                                try:
                                    dependencies['exec'].append(package)
                                except KeyError:
                                    dependencies['exec'] == []
                                    dependencies['exec'].append(package)

                # Get Linux dependencies
                elif platform.lower() == 'linux' and sysPlatform == 'linux':
                    for packageType in data[platform]:
                        for packages in packageType:
                            for package in packageType[packages]:
                                try:
                                    dependencies[packages].append(package)
                                except KeyError:
                                    dependencies[packages] = []
                                    dependencies[packages].append(package)

                # Get Skynet Webportal dependencies
                elif platform.lower() == 'skynet-webportal':
                    if depends == 'all' or depends == 'skynet-webportal':
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
                elif platform.lower() == 'handshake':
                    if depends == 'all' or depends == 'handshake':
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
                elif platform.lower() == 'powerdns':
                    if depends == 'all' or depends == 'powerdns':
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
                elif platform.lower() == 'nginx':
                    if depends == 'all' or depends == 'nginx':
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
        if sysPlatform == 'win32':
            try:
                del dependencies['apt']
            except KeyError:
                pass
        elif sysPlatform == 'linux':
            try:
                del dependencies['exe']
            except KeyError:
                pass

        return dependencies
    #################################################### END: getDependencies(self, sysPlatform, depends)

    def printDepends(self, depends):
        clear_screen()
        print(colours.yellow(self, ' [!]') + ' The following dependencies will be installed:')

        columns = 0
        packages = ''

        for packageType in depends:
            if packageType == 'exe':
                print(colours.green(self, '\n  -- Windows Executable --'))

            elif packageType == 'apt':
                print(colours.green(self, '\n  -- Linux APT Package --'))

            elif packageType == 'pip':
                print(colours.green(self, '\n  -- Python Package --'))

            elif packageType == 'git':
                print(colours.green(self, '\n  -- Github Repository --'))

            elif packageType == 'npm':
                print(colours.green(self, '\n  -- Node Package --'))

            elif packageType == 'wget':
                print(colours.green(self, '\n  -- WGET (HTTPS) --'))

            count = len(depends[packageType])

            for package in depends[packageType]:
                if len(package.strip()) <= 26:
                    while len(package) < 27:
                        package += ' '

                packages += package

                columns += 1
                count -= 1

                if count == 0 or len(package) > 30:
                    print('\t' + packages)
                    packages = ''
                    columns = 0
                elif columns == 4:
                    print('\t' + packages)
                    columns = 0
                    packages = ''
        
        print()
        print(colours.prompt(self, 'Press any key to continue, or use ' + colours.cyan(self, '`ctrl+c`') + colours.prompt(self, ' cancel install.')))
        getch()
    #################################################### END: printDepends(self, depends)

    def installDepends(self, depends):
        try:
            if ENABLE_DEPENDS == True:
                self.printDepends(depends)

                # If installing PowerDNS check for APT sources
                if 'pdns-server' in depends['apt']:
                    hasRepo = False
                    hasPackage = False

                    # Check for existing PowerDNS APT sources
                    if os.path.exists('/etc/apt/sources.list.d/pdns.list'):

                        with open("/etc/apt/sources.list.d/pdns.list") as sourceFile:
                            sources = sourceFile.readlines()

                        for line in sources:
                            if "http://repo.powerdns.com/ubuntu" in line:
                                hasRepo = True

                            if "Package: pdns-*\nPin: origin repo.powerdns.com\nPin-Priority: 600" in line:
                                hasPackage = True

                    # If PowerDNS APT sources do not exists, create them
                    if hasRepo is False:
                        print(colours.green(self, '\n [+] ') + 'Adding PowerDNS sources...')
                        addSource = 'echo "deb [arch=amd64] http://repo.powerdns.com/ubuntu focal-auth-46 main" > /etc/apt/sources.list.d/pdns.list'
                        if ENABLE_SUBPROCESSES == True:
                            subprocess.run(['sudo', 'sh', '-c', addSource], cwd=self.ADAMS_PATH, check=True)
                        else:
                            print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')
                        print()
                    else:
                        print(colours.yellow(self, '\n [!] ') + 'Existing PowerDNS sources found')

                    if hasPackage is False:
                        addSource = 'echo "Package: pdns-*\nPin: origin repo.powerdns.com\nPin-Priority: 600" > /etc/apt/preferences.d/pdns'
                        if ENABLE_SUBPROCESSES == True:
                            subprocess.run(['sudo', 'sh', '-c', addSource], cwd=self.ADAMS_PATH, check=True)
                        else:
                            print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')
                    else:
                        print(colours.yellow(self, '\n [+] ') + 'Existing PowerDNS sources found...')


                    if hasRepo is False or hasPackage is False:    
                        # Downloaded and add PowerDNS APT Key
                        print(colours.green(self, '\n [+] ') + 'Adding APT-KEY...')
                        if ENABLE_SUBPROCESSES == True:
                            subprocess.run(['wget', 'https://repo.powerdns.com/FD380FBB-pub.asc'], cwd=self.ADAMS_PATH, check=True)
                            subprocess.run(['sudo', 'apt-key', 'add', 'FD380FBB-pub.asc'], cwd=self.ADAMS_PATH, check=True)
                            subprocess.run(['rm', '-fr', 'FD380FBB-pub.asc'], cwd=self.ADAMS_PATH, check=True)
                            subprocess.run(['sudo', 'apt', 'update'], cwd=self.ADAMS_PATH, check=True)
                            print()
                        else:
                            print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')

                for packageType in depends:
                    # Install Windows Executable
                    if packageType == 'exe':
                        print(colours.red(self, '\n\n  -- Installing Windows Executables --'))
                        for package in depends[packageType]:
                            package = str(package).strip()
                            print(colours.green(self, '\n [+] ') + 'Installing "' + package + '"...')
                            pass

                    # Install Linux APT Package
                    elif packageType == 'apt':
                        print(colours.red(self, '\n\n  -- Installing Linux APT Packages --'))
                        for package in depends[packageType]:
                            package = str(package).strip()
                            print(colours.green(self, '\n [+] ') + 'Installing "' + package + '"...')
                            if ENABLE_SUBPROCESSES == True:
                                subprocess.run(['sudo', 'apt', 'install', '-y', package], check=True)

                                if package == 'npm':
                                    if os.path.exists(self.USER_DIR + '/.npm-global') == False:
                                        subprocess.run(['mkdir', self.USER_DIR + '/.npm-global'], check=True)

                                    subprocess.run(['npm', 'config', 'set', 'prefix', '"~/.npm-global"'], check=True)

                                    line = 'export ADAMS_PATH=~/.npm-global/bin:$ADAMS_PATH'
                                    subprocess.run(['echo', line, '>>', '~/.profile'], check=True)
                            else:
                                print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')

                    # Install Python Packages
                    elif packageType == 'pip':
                        print(colours.red(self, '\n\n  -- Installing Python Packages --'))
                        for package in depends[packageType]:
                            package = str(package).strip()
                            print(colours.green(self, '\n [+] ') + 'Installing "' + package + '"...')
                            if ENABLE_SUBPROCESSES == True:
                                subprocess.run(['pip', 'install', package], check=True)
                            else:
                                print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')

                    # Clone Github Repository
                    elif packageType == 'git':
                        print(colours.red(self, '\n\n  -- Cloning Github Repositories --'))
                        for package in depends[packageType]:
                            packageName = self.parseURL(package)
                            if os.path.exists(self.ADAMS_PATH + '/' + packageName[:-4]) == False:
                                print(colours.green(self, '\n [+] ') + 'Cloning "' + str(package) + '"...')
                                if ENABLE_SUBPROCESSES == True:
                                    subprocess.run(['git', 'clone', package], cwd=self.ADAMS_PATH, check=True)
                                else:
                                    print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')
                            else:
                                print(colours.yellow(self, '\n [+] ') + 'Existing "' + packageName + '" repository found')

                    # Install Node Package
                    elif packageType == 'npm':
                        print(colours.red(self, '\n\n  -- Installing Node Packages --'))
                        for package in depends[packageType]:
                            package = str(package).strip()
                            print(colours.green(self, '\n [+] ') + 'Installing "' + package + '"...')
                            if ENABLE_SUBPROCESSES == True:
                                subprocess.run(['npm', 'install', package], cwd=self.ADAMS_PATH, check=True)
                            else:
                                print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')

                    # Download/Install WGET Package
                    elif packageType == 'wget':
                        print(colours.red(self, '\n\n  -- Installing WGET Packages --'))
                        for package in depends[packageType]:
                            package = str(package).strip()
                            packageName = self.parseURL(package)
                            if os.path.isfile(self.ADAMS_PATH + '/' + packageName) == False:
                                print(colours.green(self, '\n [+] ') + 'Downloading "' + str(packageName) + '"...')
                                if ENABLE_SUBPROCESSES == True:
                                    subprocess.run(['wget', package], cwd=self.ADAMS_PATH, check=True)
                                else:
                                    print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')
                            else:
                                print(colours.yellow(self, '\n [+] ') + 'Existing "' + packageName + '" package found')

                            if str(package).endswith('tar.gz'):
                                
                                if os.path.isfile(self.ADAMS_PATH + '/' + packageName) == True and os.path.isdir(self.ADAMS_PATH + '/' + packageName[-6:]) == False:
                                    print('\t Unpacking "' + str(packageName) + '"...')
                                    if ENABLE_SUBPROCESSES == True:
                                        subprocess.run(['tar', '-xvf', packageName], cwd=self.ADAMS_PATH, check=True)
                                    else:
                                        print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')
                                    print('\t Cleaning up "' + str(packageName) + '"...')
                                    if ENABLE_SUBPROCESSES == True:
                                        subprocess.run(['rm', '-fr', packageName], cwd=self.ADAMS_PATH, check=True)
                                    else:
                                        print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')
                                else:
                                    print(colours.yellow(self, '\n [+] ') + 'Existing "' + packageName[:-6] + '" directory found')
            else:
                print(colours.error(self, 'Dependencies installer has been disabled. See `config/adams.conf`'))
                sleep(3)
        except KeyboardInterrupt:
            clear_screen()
            sys.exit(0)
    #################################################### END: installDepends(self, depends)

    def skynet_webportal(self):
        print(colours.error(self, 'skynet_webportal() method not yet complete.'))
        sleep(1)

        ''' print(colours.green(self, ' [+] ') + 'Installing Yarn')
        if ENABLE_SUBPROCESSES == True:
            subprocess.run(['npm', 'install', 'yarn'], cwd=(self.SKYNET_PATH + '/packages/website'))
        else:
            print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')

        print(colours.green(self, ' [+] ') + 'Building Skynet Portal Page')
        if ENABLE_SUBPROCESSES == True:
            subprocess.run(['yarn', 'build'], cwd=(self.SKYNET_PATH + '/packages/website'))
        else:
            print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')
        print() '''
    #################################################### END: skynet_webportal(self)

    def handshake(self):
        print(colours.green(self, '\n [+] ') + 'Installing Handshake Node')

        if ENABLE_SUBPROCESSES == True:
            # Build HSD binaries
            subprocess.run(['npm', 'install', '-g', '--production'], cwd=self.HSD_PATH, check=True)

            # Read default 'hsd.service' file
            with open(self.HSD_SERVICE_SCRIPT, 'r') as script:
                hsdServiceScript = script.readlines()

            lnCount = 0
            username = self.USER_DIR.split('/')
            iName = len(username) - 1

            # Set the 'hsd.service' variables 'ExecStart' and 'User'
            for line in hsdServiceScript:
                if line.startswith('ExecStart='):
                    hsdServiceScript[lnCount] = 'ExecStart=' + self.USER_DIR + '/.npm-global/bin/hsd\n'

                if line.startswith('User='):
                    hsdServiceScript[lnCount] = 'User=' + str(username[iName]) + '\n'

                lnCount += 1

            # Write new 'hsd.service' file
            with open(self.HSD_SERVICE_SCRIPT, 'w') as script:
                script.writelines(hsdServiceScript)
                
            # Create HSD system service 'hsd.service'
            subprocess.run(['sudo', 'cp', self.HSD_SERVICE_SCRIPT, self.HSD_SYS_SERVICES_PATH], check=True)

            # Set "hsd.service" owner
            subprocess.run(['sudo', 'chown', 'root:root', self.HSD_SYS_SERVICES_PATH], check=True)

            # Set "hsd.service" permissions
            subprocess.run(['sudo', 'chmod', '777', self.HSD_SYS_SERVICES_PATH])

            # Enable "hsd.service"
            subprocess.run(['sudo', 'systemctl', 'enable', 'hsd'])

            # Generate new API key
            nodeString = 'bcrypto=require("bcrypto"); console.log(bcrypto.random.randomBytes(32).toString("hex"))'
            apiKey = str(subprocess.check_output(['node', '-e', nodeString], cwd=self.ADAMS_PATH + '/hsd', shell=False))
            apiKey = apiKey.strip("b'")
            apiKey = apiKey.strip("\\n'")

            # Read default 'hsd.conf' file
            with open(self.HSD_CONFIG, 'r') as script:
                hsdConfig = script.readlines()

            lnCount = 0

            # Replace 'api-key' in 'hsd.conf' with newly generated apiKey
            for line in hsdConfig:
                if line.startswith('api-key:'):
                    hsdConfig[lnCount] = 'api-key: ' + apiKey + '\n'

                lnCount += 1

            # Write new 'hsd.conf' file
            with open(self.HSD_CONFIG, 'w') as script:
                script.writelines(hsdConfig)

            # Read default 'hsw.conf' file
            with open(self.HSW_CONFIG, 'r') as script:
                hswConfig = script.readlines()

            lnCount = 0

            # Replace 'api-key' in 'hsw.conf' with newly generated apiKey
            for line in hswConfig:
                if line.startswith('api-key:'):
                    hswConfig[lnCount] = 'api-key: ' + apiKey + '\n'

                lnCount += 1

            # Write new 'hsw.conf' file
            with open(self.HSW_CONFIG, 'w') as script:
                script.writelines(hswConfig)

            # Create HSD node and wallet configuration files
            if os.path.isdir(self.HSD_INSTALL_PATH) == False:
                subprocess.run(['mkdir', self.HSD_INSTALL_PATH], check=True)

            # Create HSD node and wallet configuration files
            if os.path.isdir(self.HSD_INSTALL_PATH) == False:
                subprocess.run(['mkdir', self.HSD_INSTALL_PATH], check=True)

            subprocess.run(['cp', self.HSD_CONFIG, self.HSD_INSTALL_PATH], check=True)
            subprocess.run(['cp', self.HSW_CONFIG, self.HSD_INSTALL_PATH], check=True)

            # Enable and start 'hsd' service
            subprocess.run(['sudo', 'systemctl', 'enable', 'hsd.service'], check=True)
            subprocess.run(['sudo', 'systemctl', 'start', 'hsd.service'], check=True)

        else:
            print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')
        print()
    #################################################### END: handshake(self)

    def powerdns(self):
        files = os.listdir(self.ADAMS_PATH)
        checkFor = 'pdnsmanager'

        print(colours.green(self, '\n [+] ') + 'Configuring PowerDNS')
        print(colours.green(self, '\n [+] ') + 'Installing PowerDNS Manager')

        for file in files:
            if checkFor in file:
                if ENABLE_SUBPROCESSES == True:
                    subprocess.run(['mv', file, 'pdnsmanager/'], cwd=self.ADAMS_PATH, check=True)
                else:
                    print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')

        # Check and disable existing stub resolver
        dnsExists = False
        stubListenterExists = False

        # Check resolved.conf for configuration
        with open("/etc/systemd/resolved.conf") as resolveFile:
            lines = resolveFile.readlines()

        for line in lines:
            if line == 'DNS=1.1.1.1':
                dnsExists = True

            if line == 'DNSStubListener=no':
                stubListenterExists = True

        # Add configurations to resolved.conf
        print(colours.green(self, '\n [+] ') + 'Disabling Stub Resolver...')
        if dnsExists == False or stubListenterExists == False:
            addLine = 'echo "# PowerDNS Configurations" >> /etc/systemd/resolved.conf'
            if ENABLE_SUBPROCESSES == True:
                subprocess.run(['sudo', 'sh', '-c', addLine], check=True)
            else:
                print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')

        if dnsExists == False:
            addLine = 'echo "DNS=1.1.1.1" >> /etc/systemd/resolved.conf'
            if ENABLE_SUBPROCESSES == True:
                subprocess.run(['sudo', 'sh', '-c', addLine], check=True)
            else:
                print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')

        if stubListenterExists == False:
            addLine = 'echo "DNSStubListener=no" >> /etc/systemd/resolved.conf'
            if ENABLE_SUBPROCESSES == True:
                subprocess.run(['sudo', 'sh', '-c', addLine], check=True)
            else:
                print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')
            print()

        # Create Symlink
        print(colours.green(self, '\n [+] ') + 'Creating Symlink')
        if ENABLE_SUBPROCESSES == True:
            subprocess.run(['sudo', 'ln', '-sf', '/run/systemd/resolve/resolv.conf', '/etc/resolv.conf'], check=True)
        else:
            print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')

        # Configure pdns.conf file
        print(colours.green(self, '\n [+] ') + 'Configuring "' + self.POWERDNS_CONF_PATH + '"')
        if ENABLE_SUBPROCESSES == True:
            subprocess.run(['sudo', 'rm', '-fr', self.POWERDNS_CONF_PATH], check=True)
            subprocess.run(['sudo', 'cp', self.POWERDNS_CONF_FILE, self.POWERDNS_CONF_PATH], check=True)
        else:
            print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')
        
        # Set pdns.conf file permissions
        if ENABLE_SUBPROCESSES == True:
            subprocess.run(['sudo', 'chmod', '640', self.POWERDNS_CONF_PATH], check=True)
            subprocess.run(['sudo', 'chown', '-R', 'root:pdns', self.POWERDNS_CONF_PATH], check=True)
        else:
            print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')


        # Initialize the sqlite database with schema
        if ENABLE_SUBPROCESSES == True:
            os.system('sudo sqlite3 /var/lib/powerdns/pdns.sqlite3 < /usr/share/doc/pdns-backend-sqlite3/schema.sqlite3.sql')

        # Change ownership of the directory to the `pdns` user and group
        if ENABLE_SUBPROCESSES == True:
            subprocess.run(['sudo', 'chown', '-R', 'pdns:pdns', '/var/lib/powerdns'], check=True)
        else:
            print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')

        self.NEED_RESTART = True

    #################################################### END: pdns(self)

    def nginx(self):
        print(colours.error(self, 'nginx() method not yet complete.'))
        sleep(1)
    #################################################### END: nginx(self)

    def parseURL(self, url):
        url = str(url).strip()
        charPos = 0
        count = 0
        nameLength = len(url)

        for character in url:
            if character == '/':
                charPos = count
            count += 1

        return url[(charPos + 1) - nameLength:]
    
class cli:
    menu_title = ''
    menu_options = ''

    def __init__(self):
        clear_screen()
        self.set_menu('MAIN')
        self.main_menu()
        sleep(1)
    #################################################### END: __init__(self)

    def get_input(self, prompt):
        user_input = input(colours().prompt(prompt))
        return user_input         
    #################################################### END: get_input(prompt)

    def print_header(self):
        clear_screen()  # Clear console window
        print(colours().title('\n\t' + menu_title[1] + '\n\n'))   # Print menu title
    #################################################### END: print_header()

    def print_options(self):
        for option in menu_options:     # Print menu options to screen
            print('\t    ' + option)
        print()
    #################################################### END: print_options()

    def set_menu(self, menu_id):
        global menu_title
        global menu_options
        
        if menu_id.upper() == 'MAIN':       # Main Menu Options
            menu_title = ['ADAMS_INSTALLER',
                          'A.D.A.M.S. Installer']
                          
            menu_options = [colours().cyan('1') + ': Install A.D.A.M.S.',
                            colours().cyan('2') + ': Install Skynet Webportal',
                            colours().cyan('3') + ': Install Handshake Node',
                            colours().cyan('4') + ': Install PowerDNS',
                            colours().cyan('5') + ': Install NGINX Webserver',
                            '',
                            colours().cyan('B') + ': Back to A.D.A.M.S.',
                            colours().cyan('Q') + ': Quit A.D.A.M.S.']
    #################################################### END: set_menu(menu_id)

    def main_menu(self):
        self.set_menu('MAIN')    # Initialize A.D.A.M.S. Installer Menu
        
        try:
            while True: # Display A.D.A.M.S. Installer Menu
                self.print_header()
                self.print_options()
                
                user_input = self.get_input('\n\tWhat would you like to do? : ')
                
                if user_input.upper() == '1':   # Install A.D.A.M.S.
                    install('adams')

                elif user_input.upper() == '2': # Install Skynet Webportal
                    install('skynet-webportal')

                elif user_input.upper() == '3': # Install Handshake Node
                    install('handshake')

                elif user_input.upper() == '4': # Install PowerDNS
                    install('powerdns')

                elif user_input.upper() == '5': # Install NGINX Webserver
                    install('nginx')
                    
                elif user_input.upper() == 'B':
                    import main
                    main.main(['adams','main'])

                elif user_input.upper() == 'EXIT' or user_input.upper() == 'Q' or user_input.upper() == 'QUIT':
                    clear_screen()    # Clear console window
                    sys.exit(0)

        except AttributeError as e:
            print(colours().error(str(e)))
            sleep(2)
            self.main_menu()
            
        except KeyboardInterrupt:
            import main
            main.main(['adams','main'])
    #################################################### END: main_menu()

if __name__ == "__main__":
    os.system("cls")
    cli()
#################################################### END: __main__
