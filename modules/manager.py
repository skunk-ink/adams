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

from handshake import api
from sys import platform
from time import sleep as sleep
from colours import colours
from display import clear_screen

enableSubprocesses = True         # Ghost run, does not affect the system
enableLogging = False             # Disable console logs

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

        if config[0] == "enablelogging":
            if config[1].lower() == "false":
                enableLogging = True
            else:
                enableLogging = False

            if enableLogging == True:
                print("Disable Logging: " + str(enableLogging))
                sleep(1)

        elif config[0] == "enablesubprocesses":
            if config[1].lower() == "false":
                enableSubprocesses = True
            else:
                enableSubprocesses = False
                
            if enableLogging == True:
                print("Disable Subprocesses: " + str(enableSubprocesses))
                sleep(1)

if platform == "linux":
    from getch import getch as getch
elif platform == "win32":
    from msvcrt import getch as getch

class hsdManager:
    HSD_API_KEY = ''
    HSW_API_KEY = ''

    hsd = api.hsd(HSD_API_KEY)
    hsw = api.hsw(HSW_API_KEY)

    def createRecord(self, namespace):
        if namespace == "":
            namespace = cli.get_input(self, "\n\tDomain Name : ")

        record = {"records": [{"type": "NS", "ns": "ns1." + namespace + "."}]}

        if enableSubprocesses == True:
            subprocess.run(["hsw-cli", "rpc", "sendupdate", namespace, record], check=True)
        else:
            print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")

        print(colours.green(self, "\n [+] ") + "Record created, press any key to continue")
        sleep(2)

class pdnsManager:
    def createZone(self, namespace):

        if namespace == "":
            namespace = cli.get_input(self, "\n\tDomain Name : ")

        # Create a new zone
        if enableSubprocesses == True:
            subprocess.run(["sudo", "-u", "pdns", "pdnsutil", "create-zone", namespace , "ns1." + namespace], check=True)
        else:
            print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")

        print(colours.green(self, "\n [+] ") + "Zone created, press any key to continue")
        sleep(2)

        updateHNS = cli.get_input(self, "\n\tUpdate handshake records (Y/N)? [default = N] : ")
        if updateHNS.lower() == "y":
            if enableLogging == True: print("pdnsManager: var namespace = " + namespace) # Log output
            hsdManager.createRecord(self, namespace)

        
    #################################################### END: createZone(self)

    def secureZone(self, namespace):
        
        if namespace == "":
            namespace = cli.get_input(self, "\n\tEnter zone name to secure : ")

        # Secure an existing zone
        if enableSubprocesses == True:
            subprocess.run(["sudo", "-u", "pdns", "pdnsutil", "secure-zone", namespace], check=True)
        else:
            print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")

        print(colours.green(self, "\n [+] ") + "Zone secured, press any key to continue")
        sleep(2)
                

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

        # Update PowerDNS Record
        if enableSubprocesses == True:
            subprocess.run(["sudo", "-u", "pdns", "pdnsutil", "add-record", namespace + ".", record_name, record_type, record_value], check=True)
        else:
            print(colours.yellow(self, "\n [!] ") + "Subprocess disabled")

        print(colours.green(self, "\n [+] ") + "Record created, press any key to continue")
        sleep(2)
    #################################################### END: createRecord(self)

        
class cli:
    menu_title = ""
    menu_options = ""

    def __init__(self, _type:str=None):
        clear_screen()

        if _type == None or _type.upper() == 'MAIN': 
            self.main_menu()
        elif _type.upper() == 'SKYNET-WEBPORTAL' or _type.upper() == 'SKYNET': 
            self.skynetManagerCli()
        elif _type.upper() == 'HSD' or _type.upper() == 'HANDSHAKE': 
            self.hsdManagerCli()
        elif _type.upper() == 'PDNS' or _type.upper() == 'POWERDNS': 
            self.pdnsManagerCli()
        elif _type.upper() == 'NGINX':
            self.nginxManagerCli()
        
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
                            colours().cyan("3") + ": PowerDNS",
                            colours().cyan("4") + ": NGINX Webserver",
                            "",
                            colours().cyan("B") + ": Back to A.D.A.M.S.",
                            colours().cyan("Q") + ": Quit A.D.A.M.S."]
                   
        elif menu_id.upper() == "SKYNET":   # Skynet Webportal Menu Options
            menu_title = ["SKYNET_WEBPORTAL",
                          "Skynet Webportal Management"]
                          
            menu_options = [colours().cyan("1") + ": Wallet",
                            colours().cyan("2") + ": Contracts",
                            colours().cyan("3") + ": Blocklists",
                            "",
                            colours().cyan("B") + ": Back to Management",
                            colours().cyan("Q") + ": Quit A.D.A.M.S."]

        elif menu_id.upper() == "HSD":      # Handshake Daemon Menu Options
            menu_title = ["HANDSHAKE_NODE",
                          "Handshake Node Management"]
                          
            menu_options = [colours().cyan("1") + ": Wallet",
                            colours().cyan("2") + ": Consensus",
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
            
        elif menu_id.upper() == "NGINX":    # NGINX Menu Options
            menu_title = ["NGINX",
                         "NGINX Webserver Management"]
                          
            menu_options = [colours().cyan("1") + ": NGINX Configuration",
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
                    self.skynetManagerCli()
                    print(colours().error("skynetManagerCli()) method not found."))
                    sleep(1)

                elif user_input.upper() == "2": # Handshake Daemon Management
                    self.hsdManagerCli()
                    print(colours().error("hsdManagerCli() method not found."))
                    sleep(1)

                elif user_input.upper() == "3": # PowerDNS Management
                    self.pdnsManagerCli()
                    print(colours().error("pdnsManagerCli() method not found."))
                    sleep(1)

                elif user_input.upper() == "4": # NGINX Management
                    self.nginxManagerCli()
                    print(colours().error("nginxManagerCli() method not found."))
                    sleep(1)
                    
                elif user_input.upper() == "B":
                    from main import main
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

    def skynetManagerCli(self):
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
    #################################################### END: skynetManagerCli()

    def hsdManagerCli(self):
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
    #################################################### END: hsdManagerCli()

    def pdnsManagerCli(self):
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
    #################################################### END: pdnsManagerCli()

    def nginxManagerCli(self):
        global menu_title
        
        self.set_menu("NGINX")  # Initialize NGINX Management Menu

        try:
            while True:  # Display NGINX Management Menu
                self.print_header()
                self.print_options()
                
                user_input = self.get_input("\n\tWhat would you like to do? : ")
                
                if user_input.upper() == "1":   # NGINX Configuration
                    #self.nginxConfiguration()
                    print(colours().error("nginxManager class not found."))
                    sleep(1)

                elif user_input.upper() == "B":
                    self.main_menu()

                elif user_input.upper() == "EXIT" or user_input.upper() == "Q" or user_input.upper() == "QUIT":
                    clear_screen()    # Clear console window
                    sys.exit(0) 
        except KeyboardInterrupt:
            self.main_menu()
            pass
    #################################################### END: nginxManagerCli()

if __name__ == '__main__':
    os.system('cls')
    cli()
#################################################### END: __main__
