# Import
import sys
from splash import Splash
from install import Install as install
from skunkworks_ui.cli import Menu
from skunkworks_ui.style import *



    ############################################################
    ##                                                        ##
    ##                  A.D.A.M.S. Main Menu                  ##
    ##                                                        ##
    ############################################################

class Main(Menu):
    def __init__(self, menu:list = ['none']):
        """
            Description:

                    A.D.A.M.S. initializations.

            PARAMS:
                [*] Denotes required argument

                [ ] menu : Name of module to import.
        """
        if len(menu) > 1:
            if str(menu[1]).lower() == 'install' or str(menu[1]).lower() == '--install' or menu[1] == '-i':
                if len(menu) > 2:
                    if str(menu[2]).lower() == 'adams':
                        install('adams')
                    elif str(menu[2]).lower() == 'skynet-webportal' or str(menu[2]).lower() == 'skynet':
                        install('skynet-webportal')
                    elif str(menu[2]).lower() == 'handshake' or str(menu[2]).lower() == 'hsd':
                        install('handshake')
                    elif str(menu[2]).lower() == 'powerdns' or str(menu[2]).lower() == 'pdns':
                        install('powerdns')
                    elif str(menu[2]).lower() == 'nginx':
                        install('nginx')
                    else:
                        print("`" + str(menu[2]) + "` is an invalid `" + str(menu[1]) + "` command.")
                else:
                    install.cli()
            elif str(menu[1]).lower() == 'manage' or str(menu[1]).lower() == 'manager' or str(menu[1]).lower() == '--manager' or menu[1] == '-m':
                if len(menu) > 2:
                    if str(menu[2]).lower() == 'skynet-webportal' or str(menu[2]).lower() == 'skynet':
                        pass
                        # SkyManager()
                    elif str(menu[2]).lower() == 'handshake' or str(menu[2]).lower() == 'hsd':
                        HSDManager()
                    elif str(menu[2]).lower() == 'powerdns' or str(menu[2]).lower() == 'pdns':
                        PDNSManager()
                    elif str(menu[2]).lower() == 'nginx':
                        pass
                        # NGINXManager()
                    else:
                        print("`" + str(menu[2]) + "` is an invalid `" + str(menu[1]) + "` command.")
                else:
                    AdamsManager()
            elif str(menu[1]).lower() == 'main':
                self.clear_screen()
                self.main_menu()
            else:
                print("No module named `" + str(menu[1] + "` found."))
        else:
            Splash()
            self.clear_screen()
            self.main_menu()
    #################################################### END: __init__(self, menu:list = ['none'])

    def main_menu(self):
        self.title = green_font(title_style('Welcome to A.D.A.M.S.'))
        self.options = {
                            cyan_font('1'): 'Management',
                            cyan_font('2'): 'Installer',
                            'space': '',
                            cyan_font('Q'): 'Quit'
                        }

        try:
            while True: # Display A.D.A.M.S. Installer Menu
                self.display()
                
                user_input = self.get_input(prompt_style('What would you like to do? : '))
                
                if user_input.upper() == '1':   # Run management module
                    AdamsManager()

                elif user_input.upper() == '2': # Run installer module
                    Installer()

                elif user_input.upper() == 'EXIT' or user_input.upper() == 'Q' or user_input.upper() == 'QUIT':
                    self.clear_screen()    # Clear console window
                    sys.exit(0)

        except AttributeError as e:
            print(error_style(str(e)))
            self.wait(2)
            self.main_menu()
        except KeyboardInterrupt:
            return
    #################################################### END: main_menu()
## END CLASS: Main(Menu) ###############################


    ############################################################
    ##                                                        ##
    ##                      Install Menu                      ##
    ##                                                        ##
    ############################################################

class Installer(Menu):
    def __init__(self, module:str = None):
        """
            Description:

                    A.D.A.M.S. initializations.

            PARAMS:
                [*] Denotes required argument

                [ ] install : Name of module to import.
        """
        if module == None:
            self.main_menu()
        elif module.lower() == 'adams':
            install('adams')
        elif module.lower() == 'skynet-webportal' or module.lower() == 'skynet':
            install('skynet-webportal')
        elif module.lower() == 'handshake' or module.lower() == 'hsd':
            install('handshake')
        elif module.lower() == 'powerdns' or module.lower() == 'pdns':
            install('powerdns')
        elif module.lower() == 'nginx':
            install('nginx')
        else:
            print("`" + str(module) + "` is an invalid `install` command.")
    #################################################### END: __init__(self, install:str = None)

    def main_menu(self):
        self.title = green_font(title_style('A.D.A.M.S. Installer'))
        self.options = {
                            cyan_font('1'): 'Install A.D.A.M.S.',
                            cyan_font('2'): 'Install Skynet Webportal',
                            cyan_font('3'): 'Install Handshake Node',
                            cyan_font('4'): 'Install PowerDNS Server',
                            cyan_font('5'): 'Install NGINX Webserver',
                            '': '',
                            cyan_font('B'): 'Back to A.D.A.M.S.',
                            cyan_font('Q'): 'Quit A.D.A.M.S.'
                        }

        try:
            while True: # Display A.D.A.M.S. Installer Menu
                self.display()
                
                user_input = self.get_input(prompt_style('What would you like to do? : '))
                
                if user_input.upper() == '1':   # Install A.D.A.M.S.
                    install('adams')

                elif user_input.upper() == '2': # Install Skynet Webportal
                    install('skynet-webportal')

                elif user_input.upper() == '3': # Install Handshake Daemon
                    install('handshake')

                elif user_input.upper() == '4': # Install PowerDNS
                    install('powerdns')

                elif user_input.upper() == '5': # Install NGINX Webserver
                    install('nginx')
                    
                elif user_input.upper() == 'B':
                    return

                elif user_input.upper() == 'EXIT' or user_input.upper() == 'Q' or user_input.upper() == 'QUIT':
                    self.clear_screen()    # Clear console window
                    sys.exit(0)

        except AttributeError as e:
            print(error_style(str(e)))
            self.wait(2)
            self.main_menu()
        except KeyboardInterrupt:
            return
    #################################################### END: main_menu()
## END CLASS: Installer(Menu) ##########################


    ############################################################
    ##                                                        ##
    ##                   A.D.A.M.S. Manager                   ##
    ##                                                        ##
    ############################################################

class AdamsManager(Menu):
    def __init__(self, menu:str = None):
        self.clear_screen()

        if menu == None or menu.lower() == 'main': # Main Menu
            self.main_menu()
        elif menu.lower() == 'skynet-webportal' or menu.lower() == 'skynet': 
            print('Skynet Webportal Not Implemented Yet')
            self.wait(1)
            self.main_menu()
            # SkyManager()
        elif menu.lower() == 'handshake' or menu.lower() == 'hsd' or menu.lower() == 'hns':
            HSDManager()
        elif menu.lower() == 'powerdns' or menu.lower() == 'pdns': 
            PDNSManager()
        elif menu.lower() == 'nginx':
            print('NGINX Not Implemented Yet')
            self.wait(1)
            self.main_menu()
            # NGINXManager()
        #################################################### END: __init__(self, menu:str = None)
    
    def main_menu(self):
        self.title = green_font(title_style('A.D.A.M.S. Management'))
        self.options = {
                            cyan_font('1'): underline_font('S') + 'kynet Webportal',
                            cyan_font('2'): underline_font('H') + 'andshake Node',
                            cyan_font('3'): underline_font('P') + 'owerDNS Server',
                            cyan_font('4'): underline_font('N') + 'GINX Webserver',
                            '': '',
                            cyan_font('B'): 'Back to Managment',
                            cyan_font('Q'): 'Quit A.D.A.M.S.'
                        }
        
        try:
            while True:  # Display PowerDNS Management Menu
                self.display()
                
                user_input = self.get_input(prompt_style('What would you like to do? : '))
                
                # Skynet Webportal
                if user_input.lower() == '1' or user_input.lower() == 's' or user_input.lower() == 'skynet' or user_input.lower() == 'skynet-webportal' or user_input.lower() == 'portal':
                    print('Skynet Webportal')
                    self.wait(1)

                # Handshake Node
                elif user_input.lower() == '2' or user_input.lower() == 'h' or user_input.lower() == 'hsd' or user_input.lower() == 'handshake': 
                    HSDManager()

                # PowerDNS Server
                elif user_input.lower() == '3' or user_input.lower() == 'p' or user_input.lower() == 'pdns' or user_input.lower() == 'powerdns':
                    print('pdnsManager.createRecord()')
                    self.wait(1)

                # NGINX Webserver
                elif user_input.lower() == '4' or user_input.lower() == 'n' or user_input.lower() == 'nginx': 
                    print('pdnsManager.createRecord()')
                    self.wait(1)

                elif user_input.lower() == 'b':
                    break

                elif user_input.lower() == 'exit' or user_input.lower() == 'q' or user_input.lower() == 'quit':
                    self.quit()  

        except AttributeError as e:
            print(error_style(str(e)))
            self.wait(1)
            self.main_menu()

        except KeyboardInterrupt:
            self.quit()
        #################################################### END: main_menu(self)
## END CLASS: AdamsManager(Menu) ###########################


    ############################################################
    ##                                                        ##
    ##                 Handshake Node Manager                 ##
    ##                                                        ##
    ############################################################

class HSDManager(Menu):
    def __init__(self):
        self.clear_screen()
        self.main_menu()
        #################################################### END: __init__(self, menu:str = None)
    
    def main_menu(self):
        self.title = green_font(title_style('Handshake Management'))
        self.options = {
                            cyan_font('1'): underline_font('W') + 'allet Management',
                            cyan_font('2'): underline_font('H') + 'NS Records Management',
                            '': '',
                            cyan_font('B'): 'Back to Managment',
                            cyan_font('Q'): 'Quit A.D.A.M.S.'
                        }
        
        try:
            while True:  # Display PowerDNS Management Menu
                self.display()
                
                user_input = self.get_input(prompt_style('What would you like to do? : '))
                
                # Skynet Webportal
                if user_input.lower() == '1' or user_input.lower() == 'w' or user_input.lower() == 'wallet':
                    self.wallet_menu()

                # Handshake Node
                elif user_input.lower() == '2' or user_input.lower() == 'h' or user_input.lower() == 'hsd' or user_input.lower() == 'records': 
                    print('HSDManager.records()')
                    self.wait(1)

                elif user_input.lower() == 'b':
                    break

                elif user_input.lower() == 'exit' or user_input.lower() == 'q' or user_input.lower() == 'quit':
                    self.quit()  

        except AttributeError as e:
            print(error_style(str(e)))
            self.wait(1)
            self.main_menu()

        except KeyboardInterrupt:
            self.quit()
        #################################################### END: main_menu(self)
    
    def wallet_menu(self):
        self.title = green_font(title_style('Handshake Management'))
        self.options = {
                            bold_font(underline_font('Wallet')): '',
                            '': '',
                            cyan_font('1'): underline_font('A') + 'ccounts and balances',
                            cyan_font('2'): underline_font('S') + 'end HNS',
                            cyan_font('3'): underline_font('R') + 'eceive HNS',
                            '': '',
                            bold_font(underline_font('Auction:')): '',
                            '': '',
                            cyan_font('4'): 'Open Auction',
                            cyan_font('5'): 'Bid on Auction',
                            cyan_font('6'): 'Reveal Bid',
                            cyan_font('7'): 'Redeem Name',
                            '': '',
                            cyan_font('B'): 'Back to Managment',
                            cyan_font('Q'): 'Quit A.D.A.M.S.'
                        }
        
        try:
            while True:  # Display PowerDNS Management Menu
                self.display()
                
                user_input = self.get_input(prompt_style('What would you like to do? : '))
                
                # Skynet Webportal
                if user_input.lower() == '1' or user_input.lower() == 'a' or user_input.lower() == 'accounts':
                    print('HSDManager.accounts()')
                    self.wait(1)

                # Handshake Node
                elif user_input.lower() == '2' or user_input.lower() == 's' or user_input.lower() == 'send':
                    print('HSDManager.send()')
                    self.wait(1)

                # Handshake Node
                elif user_input.lower() == '3' or user_input.lower() == 'r' or user_input.lower() == 'receive':
                    print('HSDManager.receive()')
                    self.wait(1)

                # Handshake Node
                elif user_input.lower() == '4' or user_input.lower() == 'open':
                    print('HSDManager.open()')
                    self.wait(1)

                # Handshake Node
                elif user_input.lower() == '5' or user_input.lower() == 'bid':
                    print('HSDManager.bid()')
                    self.wait(1)

                # Handshake Node
                elif user_input.lower() == '6' or user_input.lower() == 'reveal':
                    print('HSDManager.reveal()')
                    self.wait(1)

                # Handshake Node
                elif user_input.lower() == '7' or user_input.lower() == 'redeem':
                    print('HSDManager.redeem()')
                    self.wait(1)

                elif user_input.lower() == 'b':
                    self.main_menu()

                elif user_input.lower() == 'exit' or user_input.lower() == 'q' or user_input.lower() == 'quit':
                    self.quit()  

        except AttributeError as e:
            print(error_style(str(e)))
            self.wait(1)
            self.main_menu()

        except KeyboardInterrupt:
            self.quit()
        #################################################### END: wallet(self)
## END CLASS: HSDManager(Menu) #############################


    ############################################################
    ##                                                        ##
    ##                  PowerDNS Node Manager                 ##
    ##                                                        ##
    ############################################################

class PDNSManager(Menu):
    def __init__(self):
        self.clear_screen()
        self.main_menu()
        #################################################### END: __init__(self, menu:str = None)
    
    def main_menu(self):
        self.title = green_font(title_style('PowerDNS Management'))
        self.options = {
                            cyan_font('1'): 'New Zone',
                            cyan_font('2'): 'Secure Zone',
                            cyan_font('3'): 'Add Record',
                            '': '',
                            cyan_font('B'): 'Back to Managment',
                            cyan_font('Q'): 'Quit A.D.A.M.S.'
                        }
        
        try:
            while True:  # Display PowerDNS Management Menu
                self.display()
                
                user_input = self.get_input(prompt_style('What would you like to do? : '))
                
                if user_input.lower() == '1':   # Create new zone
                    print('PDNSManager.new_zone()')
                    self.wait(1)

                elif user_input.lower() == '2': # Secure existing zone
                    print('pdnsManager.secureZone()')
                    self.wait(1)

                elif user_input.lower() == '3': # Create new record
                    print('pdnsManager.createRecord()')
                    self.wait(1)

                elif user_input.lower() == 'b':
                    break

                elif user_input.lower() == 'exit' or user_input.lower() == 'q' or user_input.lower() == 'quit':
                    self.quit()  

        except AttributeError as e:
            print(error_style(str(e)))
            self.wait(1)
            self.main_menu()

        except KeyboardInterrupt:
            self.quit()
        #################################################### END: main_menu(self)
## END CLASS: PDNSManager(Menu) ############################

if __name__ == "__main__":
    Main(sys.argv)