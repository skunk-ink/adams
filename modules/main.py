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

from sys import platform
from time import sleep
from display import clear_screen
from colours import colours
from splash import splash
    
PATH = os.getcwd()      # A.D.A.M.S. Directory

if platform == "linux":
    from getch import getch as getch
    DATA_PATH = os.getcwd() + '/data/'      # Linux directory format
elif platform == "win32":
    from msvcrt import getch as getch
    DATA_PATH = os.getcwd() + '\data\\'     # Windows directory format

class main:

    menu_title = ""     # Initialize string: menu_title
    menu_options = {}   # Initialize array: menu_options
    menu_prompt = ""    # Initialize string: menu_prompt
    
    def __init__(self, _moduleName:list=['none']):
        """
            Description:

                    A.D.A.M.S. initializations.

            PARAMS:
                [*] Denotes required argument

                [ ] _moduleName : Name of module to import.
        """
        if len(_moduleName) > 1:
            if _moduleName[1].lower() == 'install' or _moduleName[1].lower() == '--install' or _moduleName[1] == '-i':
                import installer
                if len(_moduleName) > 2:
                    if _moduleName[2].lower() == 'adams':
                        installer.install('adams')
                    elif _moduleName[2].lower() == 'skynet-webportal' or _moduleName[2].lower() == 'skynet':
                        installer.install('skynet-webportal')
                    elif _moduleName[2].lower() == 'handshake' or _moduleName[2].lower() == 'hsd':
                        installer.install('handshake')
                    elif _moduleName[2].lower() == 'powerdns' or _moduleName[2].lower() == 'pdns':
                        installer.install('powerdns')
                    elif _moduleName[2].lower() == 'nginx':
                        installer.install('nginx')
                    else:
                        print("`" + str(_moduleName[2]) + "` is an invalid `" + str(_moduleName[1]) + "` command.")
                else:
                    installer.cli()
            elif _moduleName[1].lower() == 'manage' or _moduleName[1].lower() == 'manager' or _moduleName[1].lower() == '--manager' or _moduleName[1] == '-m':
                if len(_moduleName) > 2:
                    if _moduleName[2].lower() == 'skynet-webportal' or _moduleName[2].lower() == 'skynet':
                        import skymanager
                        skymanager.cli()
                    elif _moduleName[2].lower() == 'handshake' or _moduleName[2].lower() == 'hsd':
                        import hsmanager
                        hsmanager.cli()
                    elif _moduleName[2].lower() == 'powerdns' or _moduleName[2].lower() == 'pdns':
                        import pdnsmanager
                        pdnsmanager.cli()
                    elif _moduleName[2].lower() == 'nginx':
                        import nginxmanager
                        nginxmanager.cli()
                    else:
                        print("`" + str(_moduleName[2]) + "` is an invalid `" + str(_moduleName[1]) + "` command.")
                else:
                    import manager
                    manager.cli()
            elif _moduleName[1].lower() == 'main':
                clear_screen()
                self.set_menu("MAIN")
                self.main_menu()
            else:
                print("No module named `" + str(_moduleName[1] + "` found."))
        else:
            splash()
            clear_screen()
            self.set_menu("MAIN")
            self.main_menu()
    #################################################### END: __init__()

    def get_input(self, prompt):
        user_input = input(colours().prompt(prompt))
        return user_input         
    #################################################### END: get_input(prompt)

    def print_header(self):
        clear_screen()  # Clear console window
        print(colours().title("\n\t" + self.menu_title[1] + "\n\n"))   # Print menu title
    #################################################### END: print_header()

    def print_options(self):
        for key, value in self.menu_options.items():
            if str(key) == 'SPACE':
                print()
            else:
                print("\t    " + colours().cyan(str(key)) + ": " + str(value))
        print()
    #################################################### END: print_options()

    def set_menu(self, menu_id):
        global menu_title
        global menu_options
        
        if menu_id.upper() == "MAIN":   # If Main menu requested do the following
            self.menu_title = ["MAIN", 
                          "A.D.A.M.S."]
                          
            self.menu_options = {"1" : "Management",
                            "2" : "Install", 
                            "SPACE" : "", 
                            "Q" : "Quit"}
    #################################################### END: set_menu(menu_id)

    def main_menu(self):
        self.set_menu("MAIN")
        
        try:
            while True:
                self.print_header()
                self.print_options()
                
                user_input = self.get_input("\n\tWhat would you like to do? : ")
                
                if user_input.upper() == "1" or user_input.upper() == "M":
                    import manager
                    manager.cli()
                elif user_input.upper() == "2" or user_input.upper() == "I":
                    import installer
                    installer.cli()
                elif user_input.upper() == "EXIT" or user_input.upper() == "Q" or user_input.upper() == "QUIT":
                    clear_screen()    # Clear console window
                    sys.exit(0)
        except AttributeError as e:
            print(colours().error(str(e)))
            sleep(2)
            self.main_menu()
        except KeyboardInterrupt:
            self.main_menu()
    #################################################### END: main_menu()

    def management(self):
        self.set_menu("MANAGEMENT")
        
        # Initialize A.D.A.M.S. Configuration Menu
        
        try:
            while True: # Display A.D.A.M.S. Configuration Menu
                self.print_header()
                self.print_options()
                
                user_input = self.get_input('\n\tWhat would you like to do? : ')
                
                if user_input.upper() == '1':   # Skynet Webportal Management
                    import skymanager
                    skymanager.cli()
                    print(colours().error('skynetManagerCli()) method not found.'))
                    sleep(1)

                elif user_input.upper() == '2': # Handshake Daemon Management
                    try:
                        import hsmanager
                        hsmanager.cli()
                    except ImportError:
                        # print(colours().error('Handshake node not detected! Please install.'))
                        print(colours().error('Import of `hsmanager` failed. Please restart A.D.A.M.S.'))
                        sleep(2)
                        clear_screen()

                elif user_input.upper() == '3': # PowerDNS Management
                    import pdnsmanager
                    pdnsmanager.cli()
                    print(colours().error('pdnsManagerCli() method not found.'))
                    sleep(1)

                elif user_input.upper() == '4': # NGINX Management
                    import nginxmanager
                    nginxmanager.cli()
                    print(colours().error('nginxManagerCli() method not found.'))
                    sleep(1)
                    
                elif user_input.upper() == 'B':
                    self.main_menu()

                elif user_input.upper() == 'EXIT' or user_input.upper() == 'Q' or user_input.upper() == 'QUIT':
                    clear_screen()    # Clear console window
                    sys.exit(0)

        except AttributeError as e:
            print(colours().error(str(e)))
            sleep(2)
            self.main_menu()
        except KeyboardInterrupt:
            self.main_menu()
    #################################################### END: management(self)

if __name__ == '__main__':
    main(sys.argv)  
#################################################### END: __main__