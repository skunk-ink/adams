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
from skunkworks_ui.cli import Menu
from skunkworks_ui.style import *

enableSubprocesses = True               # Ghost run, does not affect the system
enableDependencyInstall = True          # Enable dependency check on all install methods
enableLogging = False                   # Enable console logs

enableAdamsInstall = True               # Enable A.D.A.M.S. Installer
enableSkynetWebportalInstall = True     # Enable Skynet Webportal Installer
enableHandshakeInstall = True           # Enable Handshake Daemon Installer
enablePowerDnsInstall = True            # Enable PowerDNS Installer
enableNginxInstall = True               # Enable NGINX Installer

# Load configurations file
with open('./config/adams.conf') as configFile:
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

        if config[0] == 'enablelogging':
            if config[1].lower() == 'true':
                enableLogging = True
            else:
                enableLogging = False

            if enableLogging == True:
                print('Disable Logging: ' + str(enableLogging))
                Menu.wait(1)

        elif config[0] == 'enablesubprocesses':
            if config[1].lower() == 'true':
                enableSubprocesses = True
            else:
                enableSubprocesses = False
                
            if enableLogging == True:
                print('Disable Subprocesses: ' + str(enableSubprocesses))
                Menu.wait(1)

        elif config[0] == 'enableadamsinstall':
            if config[1].lower() == 'true':
                enableAdamsInstall = True
            else:
                enableAdamsInstall = False
                
            if enableLogging == True:
                print('Disable Install Methods: ' + str(enableAdamsInstall))
                Menu.wait(1)

        elif config[0] == 'enableskynetwebportalinstall':
            if config[1].lower() == 'true':
                enableSkynetWebportalInstall = True
            else:
                enableSkynetWebportalInstall = False
                
            if enableLogging == True:
                print('Disable Install Methods: ' + str(enableSkynetWebportalInstall))
                Menu.wait(1)

        elif config[0] == 'enablehandshakeinstall':
            if config[1].lower() == 'true':
                enableHandshakeInstall = True
            else:
                enableHandshakeInstall = False
                
            if enableLogging == True:
                print('Disable Install Methods: ' + str(enableHandshakeInstall))
                Menu.wait(1)

        elif config[0] == 'enablepowerdnsinstall':
            if config[1].lower() == 'true':
                enablePowerDnsInstall = True
            else:
                enablePowerDnsInstall = False
                
            if enableLogging == True:
                print('Disable Install Methods: ' + str(enablePowerDnsInstall))
                Menu.wait(1)

        elif config[0] == 'enablenginxinstall':
            if config[1].lower() == 'true':
                enableNginxInstall = True
            else:
                enableNginxInstall = False
                
            if enableLogging == True:
                print('Disable Install Methods: ' + str(enableNginxInstall))
                Menu.wait(1)

        elif config[0] == 'enabledependencyinstall':
            if config[1].lower() == 'true':
                enableDependencyInstall = True
            else:
                enableDependencyInstall = False
                
            if enableLogging == True:
                print('Disable Dependencies: ' + str(enableDependencyInstall))
                Menu.wait(1)

if platform == 'linux':
    from getch import getch as getch
elif platform == 'win32':
    from msvcrt import getch as getch

class Install(Menu):
    NEED_RESTART = False
    ADAMS_PATH = os.getcwd()                                      # A.D.A.M.S. directory
    USER_DIR = os.path.expanduser('~')                      # User home directory
    HSD_INSTALL_PATH = USER_DIR + '/.hsd'                   # HSD installation directory
    HSD_PATH = ADAMS_PATH + '/hsd'                                # Handshake directory
    HSD_BIN_PATH = ADAMS_PATH + '/hsd/bin'                        # Handshake binaries build directory
    HSD_SERVICE_SCRIPT = ADAMS_PATH + '/config/hsd.service'       # Premade Handshake daemon service script
    HSD_SYS_SERVICES_PATH = '/etc/systemd/system'           # Location of system services
    HSD_CONFIG = ADAMS_PATH + '/config/hsd.conf'                  # Location of HSD node config
    HSW_CONFIG = ADAMS_PATH + '/config/hsw.conf'                  # Location of HSD wallet config
    SKYNET_PATH = ADAMS_PATH + '/skynet-webportal'                # Skynet Webportal directory
    ANSIBLE_PLAYBOOKS_PATH = ADAMS_PATH + '/ansible-playbooks'    # Ansible Playbooks directory
    ANSIBLE_PRIVATE_PATH = ADAMS_PATH + '/ansible-private'        # Ansible Private directory
    POWERDNS_PATH = ADAMS_PATH + '/pdns'                          # PowerDNS directory
    POWERDNS_CONF_PATH = '/etc/powerdns/pdns.conf'          # PowerDNS configuration file
    POWERDNS_CONF_FILE = ADAMS_PATH + '/config/pdns.conf'         # Premade PowerDNS configuration file

    def __init__(self, type):

        self.NEED_RESTART = False

        try:
            if type == 'adams':
                if enableAdamsInstall == True:
                    print(red_font('\nInstalling A.D.A.M.S.'))

                    self.installDepends(self.getDependencies(sys.platform, 'all'))

                    self.handshake()
                    self.powerdns()
                    self.nginx()
                    self.skynet_webportal()
                    print(prompt_style('\n A.D.A.M.S. install complete! Press any key to continue.'))
                    self.pause()
                else:
                    print(error_style('A.D.A.M.S. installer has been disabled. See `config/adams.conf`'))
                    self.wait(3)

            elif type == 'skynet-webportal':
                if enableSkynetWebportalInstall == True:
                    print(red_font('\nInstalling Skynet Webportal'))

                    self.installDepends(self.getDependencies(sys.platform, 'skynet-webportal'))

                    self.skynet_webportal()
                    print(prompt_style('\n Skynet Webportal install complete! Press any key to continue.'))
                    self.pause()
                else:
                    print(error_style('Skynet Webportal installer has been disabled. See `config/adams.conf`'))
                    self.wait(3)

            elif type == 'handshake':
                if enableHandshakeInstall == True:
                    print(red_font('\nInstalling Handshake Daemon'))

                    self.installDepends(self.getDependencies(sys.platform, 'handshake'))

                    self.handshake()
                    print(prompt_style('\n Handshake Daemon install complete! Press any key to continue.'))
                    self.pause()
                else:
                    print(error_style('Handshake Node installer has been disabled. See `config/adams.conf`'))
                    self.wait(3)

            elif type == 'powerdns':
                if enablePowerDnsInstall == True:
                    print(red_font('\nInstalling PowerDNS'))

                    self.installDepends(self.getDependencies(sys.platform, 'powerdns'))

                    self.powerdns()
                    print(prompt_style('\n PowerDNS install complete! Press any key to continue.'))
                    self.pause()
                else:
                    print(error_style('PowerDNS installer has been disabled. See `config/adams.conf`'))
                    self.wait(3)

            elif type == 'nginx':
                if enableNginxInstall == True:
                    print(red_font('\nInstalling NGINX Webserver'))

                    self.installDepends(self.getDependencies(sys.platform, 'nginx'))

                    self.nginx()
                    print(prompt_style('\n NGINX install complete! Press any key to continue.'))
                    self.pause()
                else:
                    print(error_style('NGINX installer has been disabled. See `config/adams.conf`'))
                    self.wait(3)

            if self.NEED_RESTART == True:
                print(yellow_font('\n [!]') + ' RESTART NEEDED: Type "yes" to reboot now, or "no" to return to menu')
                userInput = self.get_input('\n\tWould you like to restart now? : ')
                if userInput.lower() == 'yes':
                    if enableLogging == True:
                        print(yellow_font('\n [!] ') + 'Reboot initiated...')
                        self.wait(1)

                    if enableSubprocesses == True:
                        subprocess.run(['sudo', 'reboot', 'now'], check=True)
                    else:
                        print(yellow_font('\n [!] ') + 'Subprocess disabled')
        except KeyboardInterrupt:
            return
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
        self.clear_screen()
        print(yellow_font(' [!]') + ' The following dependencies will be installed:')

        columns = 0
        packages = ''

        for packageType in depends:
            if packageType == 'exe':
                print(green_font('\n  -- Windows Executable --'))

            elif packageType == 'apt':
                print(green_font('\n  -- Linux APT Package --'))

            elif packageType == 'pip':
                print(green_font('\n  -- Python Package --'))

            elif packageType == 'git':
                print(green_font('\n  -- Github Repository --'))

            elif packageType == 'npm':
                print(green_font('\n  -- Node Package --'))

            elif packageType == 'wget':
                print(green_font('\n  -- WGET (HTTPS) --'))

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
        print(prompt_style('Press any key to continue, or "ctrl+c" to return to main menu.'))
        self.pause()
    #################################################### END: printDepends(self, depends)

    def installDepends(self, depends):
        if enableDependencyInstall == True:
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
                    print(green_font('\n [+] ') + 'Adding PowerDNS sources...')
                    addSource = 'echo "deb [arch=amd64] http://repo.powerdns.com/ubuntu focal-auth-46 main" > /etc/apt/sources.list.d/pdns.list'
                    if enableSubprocesses == True:
                        subprocess.run(['sudo', 'sh', '-c', addSource], cwd=self.ADAMS_PATH, check=True)
                    else:
                        print(yellow_font('\n [!] ') + 'Subprocess disabled')
                    print()
                else:
                    print(yellow_font('\n [!] ') + 'Existing PowerDNS sources found')

                if hasPackage is False:
                    addSource = 'echo "Package: pdns-*\nPin: origin repo.powerdns.com\nPin-Priority: 600" > /etc/apt/preferences.d/pdns'
                    if enableSubprocesses == True:
                        subprocess.run(['sudo', 'sh', '-c', addSource], cwd=self.ADAMS_PATH, check=True)
                    else:
                        print(yellow_font('\n [!] ') + 'Subprocess disabled')
                else:
                    print(yellow_font('\n [+] ') + 'Existing PowerDNS sources found...')


                if hasRepo is False or hasPackage is False:    
                    # Downloaded and add PowerDNS APT Key
                    print(green_font('\n [+] ') + 'Adding APT-KEY...')
                    if enableSubprocesses == True:
                        subprocess.run(['wget', 'https://repo.powerdns.com/FD380FBB-pub.asc'], cwd=self.ADAMS_PATH, check=True)
                        subprocess.run(['sudo', 'apt-key', 'add', 'FD380FBB-pub.asc'], cwd=self.ADAMS_PATH, check=True)
                        subprocess.run(['rm', '-fr', 'FD380FBB-pub.asc'], cwd=self.ADAMS_PATH, check=True)
                        subprocess.run(['sudo', 'apt', 'update'], cwd=self.ADAMS_PATH, check=True)
                        print()
                    else:
                        print(yellow_font('\n [!] ') + 'Subprocess disabled')

            for packageType in depends:
                # Install Windows Executable
                if packageType == 'exe':
                    print(red_font('\n\n  -- Installing Windows Executables --'))
                    for package in depends[packageType]:
                        package = str(package).strip()
                        print(green_font('\n [+] ') + 'Installing "' + package + '"...')
                        pass

                # Install Linux APT Package
                elif packageType == 'apt':
                    print(red_font('\n\n  -- Installing Linux APT Packages --'))
                    for package in depends[packageType]:
                        package = str(package).strip()
                        print(green_font('\n [+] ') + 'Installing "' + package + '"...')
                        if enableSubprocesses == True:
                            subprocess.run(['sudo', 'apt', 'install', '-y', package], check=True)

                            if package == 'npm':
                                if os.path.exists(self.USER_DIR + '/.npm-global') == False:
                                    subprocess.run(['mkdir', self.USER_DIR + '/.npm-global'], check=True)

                                subprocess.run(['npm', 'config', 'set', 'prefix', '"~/.npm-global"'], check=True)

                                line = 'export ADAMS_PATH=~/.npm-global/bin:$ADAMS_PATH'
                                subprocess.run(['echo', line, '>>', '~/.profile'], check=True)
                                # os.environ['NPM_CONFIG_PREFIX'] = '~/.npm-global'
                                # subprocess.run(['source', '~/.profile'], check=True)
                        else:
                            print(yellow_font('\n [!] ') + 'Subprocess disabled')

                # Install Python Packages
                elif packageType == 'pip':
                    print(red_font('\n\n  -- Installing Python Packages --'))
                    for package in depends[packageType]:
                        package = str(package).strip()
                        print(green_font('\n [+] ') + 'Installing "' + package + '"...')
                        if enableSubprocesses == True:
                            subprocess.run(['pip', 'install', package], check=True)
                        else:
                            print(yellow_font('\n [!] ') + 'Subprocess disabled')

                # Clone Github Repository
                elif packageType == 'git':
                    print(red_font('\n\n  -- Cloning Github Repositories --'))
                    for package in depends[packageType]:
                        packageName = self.parseURL(package)
                        if os.path.exists(self.ADAMS_PATH + '/' + packageName[:-4]) == False:
                            print(green_font('\n [+] ') + 'Cloning "' + str(package) + '"...')
                            if enableSubprocesses == True:
                                subprocess.run(['git', 'clone', package], cwd=self.ADAMS_PATH, check=True)
                            else:
                                print(yellow_font('\n [!] ') + 'Subprocess disabled')
                        else:
                            print(yellow_font('\n [+] ') + 'Existing "' + packageName + '" repository found')

                # Install Node Package
                elif packageType == 'npm':
                    print(red_font('\n\n  -- Installing Node Packages --'))
                    for package in depends[packageType]:
                        package = str(package).strip()
                        print(green_font('\n [+] ') + 'Installing "' + package + '"...')
                        if enableSubprocesses == True:
                            subprocess.run(['npm', 'install', package], cwd=self.ADAMS_PATH, check=True)
                        else:
                            print(yellow_font('\n [!] ') + 'Subprocess disabled')

                # Download/Install WGET Package
                elif packageType == 'wget':
                    print(red_font('\n\n  -- Installing WGET Packages --'))
                    for package in depends[packageType]:
                        package = str(package).strip()
                        packageName = self.parseURL(package)
                        if os.path.isfile(self.ADAMS_PATH + '/' + packageName) == False:
                            print(green_font('\n [+] ') + 'Downloading "' + str(packageName) + '"...')
                            if enableSubprocesses == True:
                                subprocess.run(['wget', package], cwd=self.ADAMS_PATH, check=True)
                            else:
                                print(yellow_font('\n [!] ') + 'Subprocess disabled')
                        else:
                            print(yellow_font('\n [+] ') + 'Existing "' + packageName + '" package found')

                        if str(package).endswith('tar.gz'):
                            
                            if os.path.isfile(self.ADAMS_PATH + '/' + packageName) == True and os.path.isdir(self.ADAMS_PATH + '/' + packageName[-6:]) == False:
                                print('\t Unpacking "' + str(packageName) + '"...')
                                if enableSubprocesses == True:
                                    subprocess.run(['tar', '-xvf', packageName], cwd=self.ADAMS_PATH, check=True)
                                else:
                                    print(yellow_font('\n [!] ') + 'Subprocess disabled')
                                print('\t Cleaning up "' + str(packageName) + '"...')
                                if enableSubprocesses == True:
                                    subprocess.run(['rm', '-fr', packageName], cwd=self.ADAMS_PATH, check=True)
                                else:
                                    print(yellow_font('\n [!] ') + 'Subprocess disabled')
                            else:
                                print(yellow_font('\n [+] ') + 'Existing "' + packageName[:-6] + '" directory found')
        else:
            print(error_style('Dependencies installer has been disabled. See `config/adams.conf`'))
            self.wait(3)
    #################################################### END: installDepends(self, depends)

    def skynet_webportal(self):
        print(error_style('skynet_webportal() method not yet complete.'))
        self.wait(1)

        ''' print(green_font(' [+] ') + 'Installing Yarn')
        if enableSubprocesses == True:
            subprocess.run(['npm', 'install', 'yarn'], cwd=(self.SKYNET_PATH + '/packages/website'))
        else:
            print(yellow_font('\n [!] ') + 'Subprocess disabled')

        print(green_font(' [+] ') + 'Building Skynet Portal Page')
        if enableSubprocesses == True:
            subprocess.run(['yarn', 'build'], cwd=(self.SKYNET_PATH + '/packages/website'))
        else:
            print(yellow_font('\n [!] ') + 'Subprocess disabled')
        print() '''
    #################################################### END: skynet_webportal(self)

    def handshake(self):
        print(green_font('\n [+] ') + 'Installing Handshake Node')

        if enableSubprocesses == True:
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
            apiKey = str(subprocess.check_output(['node', '-e', nodeString], cwd=self.HSD_PATH, shell=False))
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
            print(yellow_font('\n [!] ') + 'Subprocess disabled')
        print()
    #################################################### END: handshake(self)

    def powerdns(self):
        files = os.listdir(self.ADAMS_PATH)
        checkFor = 'pdnsmanager'

        print(green_font('\n [+] ') + 'Configuring PowerDNS')
        print(green_font('\n [+] ') + 'Installing PowerDNS Manager')

        for file in files:
            if checkFor in file:
                if enableSubprocesses == True:
                    subprocess.run(['mv', file, 'pdnsmanager/'], cwd=self.ADAMS_PATH, check=True)
                else:
                    print(yellow_font('\n [!] ') + 'Subprocess disabled')

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
        print(green_font('\n [+] ') + 'Disabling Stub Resolver...')
        if dnsExists == False or stubListenterExists == False:
            addLine = 'echo "# PowerDNS Configurations" >> /etc/systemd/resolved.conf'
            if enableSubprocesses == True:
                subprocess.run(['sudo', 'sh', '-c', addLine], check=True)
            else:
                print(yellow_font('\n [!] ') + 'Subprocess disabled')

        if dnsExists == False:
            addLine = 'echo "DNS=1.1.1.1" >> /etc/systemd/resolved.conf'
            if enableSubprocesses == True:
                subprocess.run(['sudo', 'sh', '-c', addLine], check=True)
            else:
                print(yellow_font('\n [!] ') + 'Subprocess disabled')

        if stubListenterExists == False:
            addLine = 'echo "DNSStubListener=no" >> /etc/systemd/resolved.conf'
            if enableSubprocesses == True:
                subprocess.run(['sudo', 'sh', '-c', addLine], check=True)
            else:
                print(yellow_font('\n [!] ') + 'Subprocess disabled')
            print()

        # Create Symlink
        print(green_font('\n [+] ') + 'Creating Symlink')
        if enableSubprocesses == True:
            subprocess.run(['sudo', 'ln', '-sf', '/run/systemd/resolve/resolv.conf', '/etc/resolv.conf'], check=True)
        else:
            print(yellow_font('\n [!] ') + 'Subprocess disabled')

        # Configure pdns.conf file
        print(green_font('\n [+] ') + 'Configuring "' + self.POWERDNS_CONF_PATH + '"')
        if enableSubprocesses == True:
            subprocess.run(['sudo', 'rm', '-fr', self.POWERDNS_CONF_PATH], check=True)
            subprocess.run(['sudo', 'cp', self.POWERDNS_CONF_FILE, self.POWERDNS_CONF_PATH], check=True)
        else:
            print(yellow_font('\n [!] ') + 'Subprocess disabled')
        
        # Set pdns.conf file permissions
        if enableSubprocesses == True:
            subprocess.run(['sudo', 'chmod', '640', self.POWERDNS_CONF_PATH], check=True)
            subprocess.run(['sudo', 'chown', '-R', 'root:pdns', self.POWERDNS_CONF_PATH], check=True)
        else:
            print(yellow_font('\n [!] ') + 'Subprocess disabled')


        # Initialize the sqlite database with schema
        if enableSubprocesses == True:
            os.system('sudo sqlite3 /var/lib/powerdns/pdns.sqlite3 < /usr/share/doc/pdns-backend-sqlite3/schema.sqlite3.sql')

        # Change ownership of the directory to the `pdns` user and group
        if enableSubprocesses == True:
            subprocess.run(['sudo', 'chown', '-R', 'pdns:pdns', '/var/lib/powerdns'], check=True)
        else:
            print(yellow_font('\n [!] ') + 'Subprocess disabled')

        self.NEED_RESTART = True
    #################################################### END: pdns(self)

    def nginx(self):
        print(error_style('nginx() method not yet complete.'))
        self.wait(1)
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