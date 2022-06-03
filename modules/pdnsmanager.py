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

from getpass import getpass
import subprocess
import os
import sys

from sys import platform
from hsmanager import hsmanager
from time import sleep as sleep
from colours import colours
from display import clear_screen

ADAMS_PATH = os.getcwd()                                # A.D.A.M.S. directory
USER_DIR = os.path.expanduser('~')                      # User home directory
ADAMS_CONFIG = ADAMS_PATH + '/config/adams.conf'        # Location of A.D.A.M.S. config
POWERDNS_PATH = ADAMS_PATH + '/pdnsmanager'             # PowerDNS directory
POWERDNS_CONF_PATH = '/etc/powerdns/pdns.conf'          # PowerDNS configuration file

# A.D.A.M.S. configuration variables
ENABLE_SUBPROCESSES = True         # Ghost run, does not affect the system
ENABLE_LOGGING = False             # Disable console logs

if platform == 'linux':
    from getch import getch as getch
elif platform == 'win32':
    from msvcrt import getch as getch

if os.path.exists(POWERDNS_PATH) == False and os.path.exists(POWERDNS_CONF_PATH) == False:
    try:
        print('\033[41m\033[97m\n\t PowerDNS not detected! Please install. \033[0m\033[0m')
        print('\033[93m\033[1m\n\tPress any key to install now, or use \033[96m`ctrl+c`\033[93m to return.\033[0m\033[0m')
        getch()
        from main import main
        main(['adams', 'install', 'powerdns'])
    except KeyboardInterrupt:
        clear_screen()
        sys.exit(0)

elif os.path.exists(POWERDNS_PATH) == False or os.path.exists(POWERDNS_CONF_PATH) == False:
    try:
        print('\033[41m\033[97m\n\t PowerDNS misconfigured! Please reinstall. \033[0m\033[0m')
        print('\033[93m\033[1m\n\tPress any key to install now, or use \033[96m`ctrl+c`\033[93m to return.\033[0m\033[0m')
        getch()
        from main import main
        main(['adams', 'install', 'powerdns'])
    except KeyboardInterrupt:
        clear_screen()
        sys.exit(0)

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

        if config[0] == 'enablelogging':
            if config[1].lower() == 'true':
                ENABLE_LOGGING = True
            else:
                ENABLE_LOGGING = False

            if ENABLE_LOGGING == True:
                print('Disable Logging: ' + str(ENABLE_LOGGING))
                sleep(1)

        elif config[0] == 'enablesubprocesses':
            if config[1].lower() == 'true':
                ENABLE_SUBPROCESSES = True
            else:
                ENABLE_SUBPROCESSES = False
                
            if ENABLE_LOGGING == True:
                print('Disable Subprocesses: ' + str(ENABLE_SUBPROCESSES))
                sleep(1)

class pdnsManager:
    def createZone(self, _domainName):

        if _domainName == '':
            _domainName = cli.get_input(self, '\n\tDomain Name : ')

        # Create a new zone
        if ENABLE_SUBPROCESSES == True:
            subprocess.run(['sudo', '-u', 'pdns', 'pdnsutil', 'create-zone', _domainName , 'ns1.' + _domainName], check=True)
        else:
            print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')

        print(colours.green(self, '\n [+] ') + 'Zone created')
        sleep(2)     
    #################################################### END: createZone(self)

    def secureZone(self, _domainName):
        
        if _domainName == '':
            _domainName = cli.get_input(self, '\n\tEnter zone name to secure : ')

        # Secure an existing zone
        if ENABLE_SUBPROCESSES == True:
            subprocess.run(['sudo', '-u', 'pdns', 'pdnsutil', 'secure-zone', _domainName], check=True)
        else:
            print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')

        print(colours.green(self, '\n [+] ') + 'Zone secured')
        sleep(2)
    #################################################### END: secureZone(self)

    def createRecord(self, _domainName, record_name, record_type, record_value):

        if _domainName == '':
            _domainName = cli.get_input(self, '\n\tDomain Name : ')

        if record_type == '':
            record_type = str(cli.get_input(self, '\n\tRecord Type : ')).upper()

        if record_name == '':
            record_name = cli.get_input(self, '\n\tRecord Name : ')

        if record_value == '':
            record_value = cli.get_input(self, '\n\tRecord Value : ')

        # Update PowerDNS Record
        if ENABLE_SUBPROCESSES == True:
            subprocess.run(['sudo', '-u', 'pdns', 'pdnsutil', 'add-record', _domainName + '.', record_name, record_type, record_value], check=True)
        else:
            print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')

        print(colours.green(self, '\n [+] ') + 'Record created')
        sleep(2)

        updateHNS = cli.get_input(self, '\n\tUpdate handshake records (Y/N)? [default = N] : ')
        if updateHNS.lower() == 'y':
            if ENABLE_LOGGING == True: print('pdnsManager: var _domainName = ' + _domainName) # Log output
            hsmanager.createRecord(self, _domainName, record_type, record_value)   
    #################################################### END: createRecord(self, _domainName, record_name, record_type, record_value)
        
class cli:
    menu_title = ''
    menu_options = ''

    def __init__(self, _type:str=None):
        clear_screen()

        if _type == None or _type.upper() == "MAIN": 
            self.main_menu()
        
        self.main_menu()
    #################################################### END: __init__(self)

    def get_input(self, prompt):
        user_input = input(colours().prompt(prompt))
        return user_input         
    #################################################### END: get_input(prompt)

    def get_input_pass(self, prompt):
        user_input = getpass(colours().prompt(prompt))
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
        
        if menu_id.upper() == 'MAIN':    # PowerDNS Main Menu Options
            menu_title = ['PDNS',
                         'PowerDNS Management']
                          
            menu_options = [colours().cyan('1') + ': New zone',
                            colours().cyan('2') + ': Secure zone',
                            colours().cyan('3') + ': Create record',
                            '',
                            colours().cyan('B') + ': Back to Management',
                            colours().cyan('Q') + ': Quit A.D.A.M.S.']

    #################################################### END: set_menu(menu_id)
    ### START: main_menu()

    def main_menu(self):
        self.set_menu('MAIN')    # Initialize A.D.A.M.S. Configuration Menu
        
        try:
            while True:  # Display PowerDNS Management Menu
                self.print_header()
                self.print_options()
                
                user_input = self.get_input('\n\tWhat would you like to do? : ')
                
                if user_input.upper() == '1':   # Create new zone
                    pdnsManager.createZone(self, '')

                elif user_input.upper() == '2': # Secure existing zone
                    pdnsManager.secureZone(self, '')

                elif user_input.upper() == '3': # Create new record
                    pdnsManager.createRecord(self, '', '', '', '')

                elif user_input.upper() == 'B':
                    from main import main
                    main(['adams', 'manager'])

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
    #################################################### END: pdnsManagerCli()

if __name__ == "__main__":
    clear_screen()
    cli()
#################################################### END: __main__
