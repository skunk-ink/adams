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

import subprocess
import os
import sys

from sys import platform
from time import sleep as sleep
from colours import colours
from display import clear_screen

disableSubprocesses = False         # Ghost run, does not affect the system

if platform == "linux":
    from getch import getch as getch
elif platform == "win32":
    from msvcrt import getch as getch

class hsdManager:
    def createRecord(self, namespace):
        if namespace == "":
            namespace = cli.get_input(self, "\n\tDomain Name : ")

        record = {"records": [{"type": "NS", "ns": "ns1." + namespace + "."}]}

        try:
            if disableSubprocesses == False:
                subprocess.run(["hsw-cli", "rpc", "sendupdate", namespace, record], check=True)

            print(colours.green(self, "\n\t [+] ") + "Record created, press any key to continue")
            getch()
        except:
            print(colours.yellow(self, "\n\t [!] ") + "Handshake DNS Record Found, press any key to continue")
            getch()

class pdnsManager:
    def createZone(self, namespace):

        if namespace == "":
            namespace = cli.get_input(self, "\n\tDomain Name : ")

        try:
            if disableSubprocesses == False:
                subprocess.run(["sudo", "-u", "pdns", "pdnsutil", "create-zone", namespace , "ns1." + namespace], check=True)

            print(colours.green(self, "\n\t [+] ") + "Zone created, press any key to continue")
            getch()
        except:
            print(colours.yellow(self, "\n\t [! ") + "DNS Record Found, press any key to continue")
            getch()

        updateHNS = cli.get_input(self, "\n\tUpdate handshake records (Y/N)? [default = N] : ")
        if updateHNS.lower() == "y":
            hsdManager.createRecord(self, namespace)

        
    #################################################### END: createZone(self)

    def secureZone(self, namespace):
        
        if namespace == "":
            namespace = cli.get_input(self, "\n\tEnter zone name to secure : ")

        try:
            if disableSubprocesses == False:
                subprocess.run(["sudo", "-u", "pdns", "pdnsutil", "secure-zone", namespace], check=True)

            print(colours.green(self, "\n\t [+] ") + "Zone secured, press any key to continue")
            getch()
        except:
            print(colours.yellow(self, "\n\t [!] ") + "Zone already secured, press any key to continue")
            getch()
                

    #################################################### END: secureZone(self)

    def createRecord(self, namespace, record_name, record_type, record_value):

        if namespace == "":
            namespace = cli.get_input(self, "\n\tDomain Name : ")

        if record_name == "":
            record_name = cli.get_input(self, "\n\tRecord Name : ")

        if record_type == "":
            record_type = str(cli.get_input(self, "\n\tRecord Type : ")).upper()

        if record_value == "":
            record_value = cli.get_input(self, "\n\tRecord Value : ")

        try:
            if disableSubprocesses == False:
                subprocess.run(["sudo", "-u", "pdns", "pdnsutil", "add-record", namespace + ".", record_name, record_type, record_value], check=True)

            print(colours.green(self, "\n\t [+] ") + "Record created, press any key to continue")
            getch()
        except:
            print(colours.yellow(self, "\n\t [+] ") + "Record exists, press any key to continue")
            getch()
    #################################################### END: createRecord(self)

        
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
                         "NGINX Webserver Management"]
                          
            menu_options = [colours().cyan("1") + ": NGINX Configuration",
                            "",
                            colours().cyan("B") + ": Back to Management",
                            colours().cyan("Q") + ": Quit A.D.A.M.S."]
            
        elif menu_id.upper() == "PDNS":    # PowerDNS Menu Options
            menu_title = ["PDNS",
                         "PowerDNS Management"]
                          
            menu_options = [colours().cyan("1") + ": New zone",
                            colours().cyan("2") + ": Secure zone",
                            colours().cyan("3") + ": Create record",
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
                    clear_screen()    # Clear console window
                    sys.exit(0)

        except AttributeError as e:
            print(colours().error(str(e)))
            sleep(2)
            self.main_menu()
        except KeyboardInterrupt:
            from main import main
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
                    clear_screen()    # Clear console window
                    sys.exit(0)    
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
                    clear_screen()    # Clear console window
                    sys.exit(0)

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
                    clear_screen()    # Clear console window
                    sys.exit(0) 
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
                
                if user_input.upper() == "1":   # Create new zone
                    pdnsManager.createZone(self, "")

                elif user_input.upper() == "2": # Secure existing zone
                    pdnsManager.secureZone(self, "")

                elif user_input.upper() == "3": # Create new record
                    pdnsManager.createRecord(self, "", "", "", "")

                elif user_input.upper() == "B":
                    self.main_menu()

                elif user_input.upper() == "EXIT" or user_input.upper() == "Q" or user_input.upper() == "QUIT":
                    clear_screen()    # Clear console window
                    sys.exit(0)   
        except KeyboardInterrupt:
            self.main_menu()
            pass
    #################################################### END: hsdManager()

if __name__ == '__main__':
    os.system('cls')
    cli()
#################################################### END: __main__
