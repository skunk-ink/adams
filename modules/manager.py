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
import sys as platform

from main import main as main
from time import sleep as sleep
from colours import colours as colours

class cli:
    coinbase_connection = ""
    menu_title = ""
    menu_options = ""

    def __init__(self):
        self.clear_screen
        self.set_menu("MAIN")
        self.main_menu()
        sleep(1)
    #################################################### END: __init__(self)

    def get_input(self, prompt):
        user_input = input(colours().prompt(prompt))
        return user_input         
    #################################################### END: get_input(prompt)

    def print_header(self):
        self.clear_screen()  # Clear console window
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
            menu_title = ["ADAMS_MANAGMENT",
                          "A.D.A.M.S. Management"]
                          
            menu_options = [colours().cyan("1") + ": Skynet Webportal",
                            colours().cyan("2") + ": Handshake Daemon",
                            colours().cyan("3") + ": NGINX Webserver",
                            colours().cyan("4") + ": PowerDNS",
                            "",
                            colours().cyan("B") + ": Back to A.D.A.M.S.",
                            colours().cyan("Q") + ": Quit A.D.A.M.S."]
                   
        elif menu_id.upper() == "SKYNET":   # Skynet Webportal Menu Options
            menu_title = ["SKYNET_PORTAL",
                          "Skynet Webportal Management"]
                          
            menu_options = [colours().cyan("1") + ": Wallet",
                            colours().cyan("2") + ": Contracts",
                            colours().cyan("3") + ": Blocklists",
                            "",
                            colours().cyan("B") + ": Back to Management",
                            colours().cyan("Q") + ": Quit A.D.A.M.S."]

        elif menu_id.upper() == "HSD":      # Handshake Daemon Menu Options
            menu_title = ["HANDSHAKE_DAEMON",
                          "Handshake Daemon Management"]
                          
            menu_options = [colours().cyan("1") + ": Wallet",
                            colours().cyan("2") + ": Consensus",
                            "",
                            colours().cyan("B") + ": Back to Management",
                            colours().cyan("Q") + ": Quit A.D.A.M.S."]
            
        elif menu_id.upper() == "NGINX":    # NGINX Menu Options
            menu_title = ["NGINX",
                         "NGINX Management"]
                          
            menu_options = [colours().cyan("1") + ": NGINX Configuration",
                            "",
                            colours().cyan("B") + ": Back to Management",
                            colours().cyan("Q") + ": Quit A.D.A.M.S."]
            
        elif menu_id.upper() == "PDNS":    # PowerDNS Menu Options
            menu_title = ["PDNS",
                         "PowerDNS Management"]
                          
            menu_options = [colours().cyan("1") + ": PDNS Configuration",
                            colours().cyan("2") + ": Manage Records",
                            "",
                            colours().cyan("B") + ": Back to Management",
                            colours().cyan("Q") + ": Quit A.D.A.M.S."]

    #################################################### END: set_menu(menu_id)
    ### START: main_menu()

    def main_menu(self):
        self.set_menu("MAIN")    # Initialize A.D.A.M.S. Configuration Menu
        
        try:
            while True: # Display A.D.A.M.S. Configuration Menu
                self.print_header()
                self.print_options()
                
                user_input = self.get_input("\n\tWhat would you like to do? : ")
                
                if user_input.upper() == "1":   # Skynet Webportal Management
                    self.skynetManager()
                    print(colours().error("skynetManager()) method not found."))
                    sleep(1)

                elif user_input.upper() == "2": # Handshake Daemon Management
                    self.hsdManager()
                    print(colours().error("hsdManager() method not found."))
                    sleep(1)

                elif user_input.upper() == "3": # NGINX Management
                    self.nginxManager()
                    print(colours().error("nginxManager() method not found."))
                    sleep(1)

                elif user_input.upper() == "4": # PowerDNS Management
                    self.pdnsManager()
                    print(colours().error("pdnsManager() method not found."))
                    sleep(1)
                    
                elif user_input.upper() == "B":
                    main()

                elif user_input.upper() == "EXIT" or user_input.upper() == "Q" or user_input.upper() == "QUIT":
                    self.clear_screen()    # Clear console window
                    platform.exit(0)

        except AttributeError as e:
            print(colours().error(str(e)))
            sleep(2)
            self.main_menu()
        except KeyboardInterrupt:
            main()
    #################################################### END: main_menu()

    def skynetManager(self):
        global menu_title
        
        self.set_menu("SKYNET")  # Initialize Skynet Portal Management Menu

        try:
            while True:  # Display Skynet Portal Management Menu
                self.print_header()
                self.print_options()
                
                user_input = self.get_input("\n\tWhat would you like to do? : ")
                
                if user_input.upper() == "1":
                    #self.skynetWallet()
                    print(colours().error("skynetWallet() method not found."))
                    sleep(1)

                elif user_input.upper() == "2":
                    #self.skynetContracts()
                    print(colours().error("skynetContracts() method not found."))
                    sleep(1)

                elif user_input.upper() == "3":
                    #self.skynetBlocklists()
                    print(colours().error("skynetBlocklists() method not found."))
                    sleep(1)

                elif user_input.upper() == "B":
                    self.main_menu()

                elif user_input.upper() == "EXIT" or user_input.upper() == "Q" or user_input.upper() == "QUIT":
                    self.clear_screen()    # Clear console window
                    platform.exit(0)    
        except KeyboardInterrupt:
            self.main_menu()
            pass
    #################################################### END: skynetManager()

    def hsdManager(self):
        global menu_title
        
        self.set_menu("HSD")    # Initialize Handshake Daemon Management Menu

        try:
            while True:  # Display Handshake Daemon Management Menu
                self.print_header()
                self.print_options()
                
                user_input = self.get_input("\n\tWhat would you like to do? : ")
                
                if user_input.upper() == "1":   # Handshake Wallet
                    #self.hsdWallet()
                    print(colours().error("hsdWallet() method not found."))
                    sleep(1)

                elif user_input.upper() == "2": # View Consensus
                    #self.hsdConsensus()
                    print(colours().error("hsdConsensus() method not found."))
                    sleep(1)

                elif user_input.upper() == "B":
                    self.main_menu()

                elif user_input.upper() == "EXIT" or user_input.upper() == "Q" or user_input.upper() == "QUIT":
                    self.clear_screen()    # Clear console window
                    platform.exit(0)

        except KeyboardInterrupt:
            self.main_menu()
            pass
    #################################################### END: hsdManager()

    def nginxManager(self):
        global menu_title
        
        self.set_menu("NGINX")  # Initialize NGINX Management Menu

        try:
            while True:  # Display NGINX Management Menu
                self.print_header()
                self.print_options()
                
                user_input = self.get_input("\n\tWhat would you like to do? : ")
                
                if user_input.upper() == "1":   # NGINX Configuration
                    #self.nginxConfiguration()
                    print(colours().error("nginxConfiguration() method not found."))
                    sleep(1)

                elif user_input.upper() == "B":
                    self.main_menu()

                elif user_input.upper() == "EXIT" or user_input.upper() == "Q" or user_input.upper() == "QUIT":
                    self.clear_screen()    # Clear console window
                    platform.exit(0) 
        except KeyboardInterrupt:
            self.main_menu()
            pass
    #################################################### END: nginxManager()

    def pdnsManager(self):
        global menu_title
        
        self.set_menu("PDNS")   # Initialize PowerDNS Management Menu

        try:
            while True:  # Display PowerDNS Management Menu
                self.print_header()
                self.print_options()
                
                user_input = self.get_input("\n\tWhat would you like to do? : ")
                
                if user_input.upper() == "1":   # PowerDNS Configuration
                    #self.pdnsConfiguration()
                    print(colours().error("pdnsConfiguration() method not found."))
                    sleep(1)

                elif user_input.upper() == "2": # PowerDNS Records
                    #self.pdnsRecords()
                    print(colours().error("pdnsRecords() method not found."))
                    sleep(1)

                elif user_input.upper() == "B":
                    self.main_menu()

                elif user_input.upper() == "EXIT" or user_input.upper() == "Q" or user_input.upper() == "QUIT":
                    self.clear_screen()    # Clear console window
                    platform.exit(0)   
        except KeyboardInterrupt:
            self.main_menu()
            pass
    #################################################### END: hsdManager()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    #################################################### END: clear_screen()

if __name__ == '__main__':
    os.system('cls')
    print(colours.error("config.py not yet complete."))
    cli()
    sleep(1)
