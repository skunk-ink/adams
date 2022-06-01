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
import os
import sys

from sys import platform
from time import sleep as sleep
from colours import colours
from display import clear_screen

USER_DIR = os.path.expanduser('~')                  # User home directory
ADAMS_PATH = os.getcwd()                            # A.D.A.M.S. directory
ADAMS_CONFIG = ADAMS_PATH + '/config/adams.conf'    # Location of A.D.A.M.S. config

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
        
class cli:
    menu_title = ''
    menu_options = ''

    def __init__(self, _type:str=None):
        clear_screen()

        if _type == None or _type.upper() == "MAIN": 
            self.main_menu()
        elif _type.upper() == "SKYNET-WEBPORTAL" or _type.upper() == "SKYNET": 
            import skymanager
            skymanager.cli()
        elif _type.upper() == "HSD" or _type.upper() == "HANDSHAKE":
            import hsmanager
            hsmanager.cli()
        elif _type.upper() == "PDNS" or _type.upper() == "POWERDNS": 
            import pdnsmanager
            pdnsmanager.cli()
        elif _type.upper() == "NGINX":
            import nginxmanager
            nginxmanager.cli()
        
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
        
        if menu_id.upper() == 'MAIN':       # Main Menu Options
            menu_title = ['ADAMS_MANAGMENT',
                          'A.D.A.M.S. Management']
                          
            menu_options = [colours().cyan('1') + ': Skynet Webportal',
                            colours().cyan('2') + ': Handshake Daemon',
                            colours().cyan('3') + ': PowerDNS',
                            colours().cyan('4') + ': NGINX Webserver',
                            '',
                            colours().cyan('B') + ': Back to A.D.A.M.S.',
                            colours().cyan('Q') + ': Quit A.D.A.M.S.']

    #################################################### END: set_menu(menu_id)
    ### START: main_menu()

    def main_menu(self):
        self.set_menu('MAIN')    # Initialize A.D.A.M.S. Configuration Menu
        
        try:
            while True: # Display A.D.A.M.S. Configuration Menu
                self.print_header()
                self.print_options()
                
                user_input = self.get_input('\n\tWhat would you like to do? : ')
                
                if user_input.upper() == '1':   # Skynet Webportal Management
                    if ENABLE_SKYNET == True:
                        import skymanager
                        skymanager.cli()
                    else:
                        print(colours.error(self, 'Skynet Webportal management has been disabled. See `config/adams.conf`'))
                        sleep(3)

                elif user_input.upper() == '2': # Handshake Daemon Management
                    if ENABLE_HANDSHAKE == True:
                        import hsmanager
                        hsmanager.cli()
                    else:
                        print(colours.error(self, 'Handshake node management has been disabled. See `config/adams.conf`'))
                        sleep(3)

                elif user_input.upper() == '3': # PowerDNS Management
                    if ENABLE_POWERDNS == True:
                        import pdnsmanager
                        pdnsmanager.cli()
                    else:
                        print(colours.error(self, 'PowerDNS server management has been disabled. See `config/adams.conf`'))
                        sleep(3)

                elif user_input.upper() == '4': # NGINX Management
                    if ENABLE_NGINX == True:
                        import nginxmanager
                        nginxmanager.cli()
                    else:
                        print(colours.error(self, 'NGINX webserver management has been disabled. See `config/adams.conf`'))
                        sleep(3)
                    
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
