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
from time import sleep as sleep
from colours import colours
from display import clear_screen

USER_DIR = os.path.expanduser('~')                              # User home directory
ADAMS_PATH = os.getcwd()                                        # A.D.A.M.S. directory
ADAMS_CONFIG = ADAMS_PATH + '/config/adams.conf'                # Location of A.D.A.M.S. config
SKYNET_PATH = ADAMS_PATH + '/skynet-webportal'                  # Skynet Webportal directory
ANSIBLE_PLAYBOOKS_PATH = ADAMS_PATH + '/ansible-playbooks'      # Ansible Playbooks directory
ANSIBLE_PRIVATE_PATH = ADAMS_PATH + '/ansible-private'          # Ansible Private directory

# A.D.A.M.S. configuration variables
ENABLE_SUBPROCESSES = True         # Ghost run, does not affect the system
ENABLE_LOGGING = False             # Disable console logs

if platform == 'linux':
    from getch import getch as getch
elif platform == 'win32':
    from msvcrt import getch as getch

if os.path.exists(SKYNET_PATH) == False and os.path.exists(ANSIBLE_PLAYBOOKS_PATH) == False and os.path.exists(ANSIBLE_PRIVATE_PATH) == False:
    try:
        print('\033[41m\033[97m\n\t Skynet Webportal not detected! Please install. \033[0m\033[0m')
        print('\033[93m\033[1m\n\tPress any key to install now, or use \033[96m`ctrl+c`\033[93m to return.\033[0m\033[0m')
        getch()
        from main import main
        main(['adams', 'install', 'skynet-webportal'])
    except KeyboardInterrupt:
        clear_screen()
        sys.exit(0)

elif os.path.exists(SKYNET_PATH) == False or os.path.exists(ANSIBLE_PLAYBOOKS_PATH) == False or os.path.exists(ANSIBLE_PRIVATE_PATH) == False:
    try:
        print('\033[41m\033[97m\n\t Skynet Webportal misconfigured! Please reinstall. \033[0m\033[0m')
        print('\033[93m\033[1m\n\tPress any key to install now, or use \033[96m`ctrl+c`\033[93m to return.\033[0m\033[0m')
        getch()
        from main import main
        main(['adams', 'install', 'skynet-webportal'])
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
        
        if menu_id.upper() == 'MAIN':       # Skynet Webportal Menu Options
            menu_title = ['SKYNET_WEBPORTAL',
                          'Skynet Webportal Management']
                          
            menu_options = [colours().cyan('1') + ': Wallet',
                            colours().cyan('2') + ': Contracts',
                            colours().cyan('3') + ': Blocklists',
                            '',
                            colours().cyan('B') + ': Back to Management',
                            colours().cyan('Q') + ': Quit A.D.A.M.S.']

    #################################################### END: set_menu(menu_id)
    ### START: main_menu()

    def main_menu(self):
        self.set_menu('MAIN')    # Skynet Webportal Main Menu
        
        try:
            while True:  # Display Skynet Portal Management Menu
                self.print_header()
                self.print_options()
                
                user_input = self.get_input('\n\tWhat would you like to do? : ')
                
                if user_input.upper() == '1':
                    #self.skynetWallet()
                    print(colours().error('skynetWallet() method not found.'))
                    sleep(1)

                elif user_input.upper() == '2':
                    #self.skynetContracts()
                    print(colours().error('skynetContracts() method not found.'))
                    sleep(1)

                elif user_input.upper() == '3':
                    #self.skynetBlocklists()
                    print(colours().error('skynetBlocklists() method not found.'))
                    sleep(1)

                elif user_input.upper() == 'B':
                    import main
                    main.main(['adams', 'manager'])

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
