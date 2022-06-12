# Import
import sys
import os
import interface

from time import sleep
from sys import platform
from splash import Splash
from install import Install as install
from skunkworks_ui.cli import Menu
from skunkworks_ui.style import *

## Globals
_USER_DIR = os.path.expanduser('~')                 # User home directory
_ADAMS_PATH = os.getcwd()                           # A.D.A.M.S. directory
_ADAMS_CONFIG = _ADAMS_PATH + '/config/adams.conf'  # Location of A.D.A.M.S. config

enable_subprocesses = True              # Ghost run, does not affect the system
enable_dependencies = True              # Enable dependency check on all install methods
enable_logging = False                  # Enable console logs

if platform == 'linux':
    from getch import getch as getch
elif platform == 'win32':
    from msvcrt import getch as getch

# Load configurations file
with open(_ADAMS_CONFIG) as configFile:
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

        if config[0] == 'enable_logging':
            if config[1].lower() == 'true':
                enable_logging = True
            else:
                enable_logging = False

            if enable_logging == True:
                print('[Logging] `adams.py` disabled Logging: ' + str(enable_logging))

        elif config[0] == 'enable_subprocesses':
            if config[1].lower() == 'true':
                enable_subprocesses = True
            else:
                enable_subprocesses = False
                
            if enable_logging == True:
                print('[Logging] `adams.py` disabled Subprocesses: ' + str(enable_subprocesses))

        elif config[0] == 'enable_adams':
            if config[1].lower() == 'true':
                enable_adams = True
            else:
                enable_adams = False
                
            if enable_logging == True:
                print('[Logging] `adams.py` disabled Install Methods: ' + str(enable_adams))

        elif config[0] == 'enable_skynet':
            if config[1].lower() == 'true':
                enable_skynet = True
            else:
                enable_skynet = False
                
            if enable_logging == True:
                print('[Logging] `adams.py` disabled Install Methods: ' + str(enable_skynet))

        elif config[0] == 'enable_handshake':
            if config[1].lower() == 'true':
                enable_handshake = True
            else:
                enable_handshake = False
                
            if enable_logging == True:
                print('[Logging] `adams.py` disabled Install Methods: ' + str(enable_handshake))

        elif config[0] == 'enable_power_dns':
            if config[1].lower() == 'true':
                enable_power_dns = True
            else:
                enable_power_dns = False
                
            if enable_logging == True:
                print('[Logging] `adams.py` disabled Install Methods: ' + str(enable_power_dns))

        elif config[0] == 'enable_nginx':
            if config[1].lower() == 'true':
                enable_nginx = True
            else:
                enable_nginx = False
                
            if enable_logging == True:
                print('[Logging] `adams.py` disabled Install Methods: ' + str(enable_nginx))

        elif config[0] == 'enable_dependencies':
            if config[1].lower() == 'true':
                enable_dependencies = True
            else:
                enable_dependencies = False
                
            if enable_logging == True:
                print('[Logging] `adams.py` disabled Dependencies: ' + str(enable_dependencies))


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
                    Installer()
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
                            cyan_font('Q'): 'Quit A.D.A.M.S.'
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
                            cyan_font('1'): 'Skynet Webportal',
                            cyan_font('2'): 'Handshake Node',
                            cyan_font('3'): 'PowerDNS Server',
                            cyan_font('4'): 'NGINX Webserver',
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
    hsd = interface.HSD()
    _HSD_PATH = _ADAMS_PATH + '/hsd/'
    _HSD_CONFIG = _USER_DIR + '/.hsd/hsd.conf'          # Location of HSD node config
    _HSW_CONFIG = _USER_DIR + '/.hsd/hsw.conf'          # Location of HSD wallet config
    _HNS_WALLET_ID = None                               # HSD Wallet ID
    
    def __init__(self, type:str = None):
        # Load configurations file
        with open(_ADAMS_CONFIG) as configFile:
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

                if config[0] == 'hns_wallet_id':
                    _HNS_WALLET_ID = config[1]

                    if enable_logging == True:
                        print('[Logging] HNS Wallet ID: ' + str(_HNS_WALLET_ID))
                        self.wait(1)

        # Load HSD configurations
        with open(self._HSD_CONFIG, 'r') as hsdConfig:
            lines = hsdConfig.readlines()
            
        for line in lines:
            if line.startswith('api-key:'):
                keyValue = line.split(':')
                HSD_API_KEY = str(keyValue[1]).strip()
            elif line.startswith('network:'):
                keyValue = line.split(':')
                networkType = str(keyValue[1]).strip()

                if networkType.lower() == 'main':
                    HSD_PORT = 12037
                elif networkType.lower() == 'testnet':
                    HSD_PORT = 13037
                elif networkType.lower() == 'regtest':
                    HSD_PORT = 14037
                elif networkType.lower() == 'simnet':
                    HSD_PORT = 15037

        with open(self._HSW_CONFIG, 'r') as hswConfig:
            lines = hswConfig.readlines()

        for line in lines:
            if line.startswith('api-key:'):
                keyValue = line.split(':')
                HSW_API_KEY = str(keyValue[1]).strip()
            elif line.startswith('network:'):
                keyValue = line.split(':')
                networkType = str(keyValue[1]).strip()

                if networkType.lower() == 'main':
                    HSW_PORT = 12039
                elif networkType.lower() == 'testnet':
                    HSW_PORT = 13039
                elif networkType.lower() == 'regtest':
                    HSW_PORT = 14039
                elif networkType.lower() == 'simnet':
                    HSW_PORT = 15039

        if os.path.exists(self._HSD_CONFIG) == False and os.path.exists(self._HSW_CONFIG) == False and os.path.exists(self._HSD_PATH) == False:
            try:
                print('\033[41m\033[97m\n\t Handshake node not detected! Please install. \033[0m\033[0m')
                print('\033[93m\033[1m\n\tPress any key to install now, or use \033[96m`ctrl+c`\033[93m to return.\033[0m\033[0m')
                self.pause()
                Installer('handshake')
            except KeyboardInterrupt:
                self.clear_screen()
                return

        elif os.path.exists(self._HSD_CONFIG) == False or os.path.exists(self._HSW_CONFIG) == False or os.path.exists(self._HSD_PATH) == False:
            try:
                print('\033[41m\033[97m\n\t Handshake node misconfigured! Please reinstall. \033[0m\033[0m')
                print('\033[93m\033[1m\n\tPress any key to install now, or use \033[96m`ctrl+c`\033[93m to return.\033[0m\033[0m')
                self.pause()
                Installer('handshake')
            except KeyboardInterrupt:
                self.clear_screen()
                return

        walletFound = False

        for wallet in self.hsd.getWallets():
            if str(wallet) == _HNS_WALLET_ID:
                walletFound = True
                
        if walletFound == False:
            print(yellow_font('\n [!] ') + '`' + _HNS_WALLET_ID + '` wallet not found.')

            # Prompt user to create wallet
            while walletFound == False:
                user_input = self.get_input('\n\tWould you like to create a wallet with the ID of `' + _HNS_WALLET_ID + '`? [yes or no] : ')

                if user_input.lower() == 'yes' or user_input.lower() == 'y':
                    result = self.hsd.createWallet(_HNS_WALLET_ID)

                    if enable_logging == True:
                        print('[Logging] ' + str(result))

                    for wallet in self.hsd.getWallets():
                        if str(wallet) == _HNS_WALLET_ID:
                            walletFound = True
                else:
                    _HNS_WALLET_ID = self.get_input('\n\tEnter a name for your HNS Wallet [default = \'adams\'] : ')

                    if _HNS_WALLET_ID == '':
                        _HNS_WALLET_ID = 'adams'

                    self.hsd.createWallet(_HNS_WALLET_ID)

                    for wallet in self.hsd.getWallets():
                        if str(wallet) == _HNS_WALLET_ID:
                            walletFound = True

        #### UPDATE CONFIG FILE: adams.conf
        # Read `adams.conf` to memory
        with open(_ADAMS_CONFIG, 'r') as script:
            adamsConfig = script.readlines()

        lnCount = 0

        # Replace 'hnsWalletID' in 'adams.conf' with newly created wallet id
        for line in adamsConfig:
            if line.startswith('hnsWalletID:'):
                adamsConfig[lnCount] = 'hnsWalletID: ' + _HNS_WALLET_ID + '\n'

            lnCount += 1

        # Write new 'adams.conf' file
        with open(_ADAMS_CONFIG, 'w') as script:
            script.writelines(adamsConfig)

        # Set wallet RPC to specified wallet id
            self.hsd.setWallet(_HNS_WALLET_ID)

        self.clear_screen()

        if type == None or type.upper() == "MAIN": 
            self.main_menu()
        elif type.upper() == "HSW" or type.upper() == "WALLET": 
            self.wallet_menu
        elif type.upper() == "HSD" or type.upper() == "NODE": 
            pass
            # self.hsdNode()

        self.clear_screen()
        self.main_menu()
        #################################################### END: __init__(self, menu:str = None)
    
    def main_menu(self):
        self.title = green_font(title_style('Handshake Management'))
        self.options = {
                            cyan_font('1'): 'Wallet Management',
                            cyan_font('2'): 'HNS Records Management',
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
                            cyan_font('1'): 'Accounts and balances',
                            cyan_font('2'): 'Send HNS',
                            cyan_font('3'): 'Receive HNS',
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
            while True:  # Display Handshake Wallet Menu
                self.display()
                
                user_input = self.get_input(prompt_style('What would you like to do? : '))
                
                # Accounts and balances
                if user_input.lower() == '1' or user_input.lower() == 'a' or user_input.lower() == 'accounts':
                    self.display_accounts()
                # Send HNS
                elif user_input.lower() == '2' or user_input.lower() == 's' or user_input.lower() == 'send':
                    print('HSDManager.send()')
                    self.wait(1)

                # Receive HNS
                elif user_input.lower() == '3' or user_input.lower() == 'r' or user_input.lower() == 'receive':
                    print('HSDManager.receive()')
                    self.wait(1)

                # Open Auction
                elif user_input.lower() == '4' or user_input.lower() == 'open':
                    domainName = self.get_input('\n\tEnter name of HNS domain to start auction : ')

                    try:
                        print(self.hsd.sendAuctionOpen(domainName))
                        print(green_font('\n [+] ') + 'Auction started for `' + domainName + '`')
                    except:
                        print(yellow_font(self, '\n [!] ') + 'Failed to start auction for `' + domainName + '`')
                    
                    self.wait(2)

                # Bid on Auction
                elif user_input.lower() == '5' or user_input.lower() == 'bid':
                    
                    print('HSDManager.bid()')
                    self.wait(1)

                # Reveal Bid
                elif user_input.lower() == '6' or user_input.lower() == 'reveal':
                    print('HSDManager.reveal()')
                    self.wait(1)

                # Redeem Name
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

    def display_accounts(self):
        user_input = None
        while True:
            accounts = self.hsd.getAccounts()
            
            self.title = green_font(title_style('Wallet Accounts for `' + str(self._HNS_WALLET_ID) + '`'))
            self.options = {}
            accounts_display = {}
            accountIndex = 0
            
            for account in accounts:
                accountIndex += 1
                self.options[cyan_font(str(accountIndex))] = ': View `' + str(account) + '`'

            self.options['space'] = ''
            self.options[cyan_font('B')] = ': Back to Wallet Management'
            self.options[cyan_font('Q')] = ': Quit A.D.A.M.S.'

            self.clear_screen()

            if user_input == None or user_input == ' ':
                self.display()

                user_input = self.get_input('\n\tWhat would you like to do? : ')

            else:
                accountIndex = 0

                for account in accounts:
                    accountIndex += 1

                    if user_input == str(accountIndex):
                        results = self.hsd.getAccountInfo(str(account))
                        print(results)
                        self.pause()
                        accounts_display[green_font('Account ID')] = '  : ' + str(results['name'])
                        balance = results['balance']
                        accounts_display[green_font('Balance')] = '     : ' + str(balance['account'])
                        accounts_display[green_font('Initialized')] = ' : ' + str(results['initialized'])
                        accounts_display[green_font('Watch Only')] = '  : ' + str(results['watchOnly'])
                        accounts_display[green_font('Address')] = '     : ' + results['receiveAddress']

                self.display()
                
                for option in accounts_display:     # Print menu options to screen
                    print('\t  ' + option)
                print()
                
                user_input = self.get_input('\n\tWhat would you like to do? : ')
            if user_input.upper() == 'B' or user_input.upper() == ' ':
                self.wallet_menu()

            elif user_input.upper() == 'EXIT' or user_input.upper() == 'Q' or user_input.upper() == 'QUIT':
                self.clear_screen()    # Clear console window
                self.quit ()

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