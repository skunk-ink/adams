from getpass import getpass
import os
import sys

from handshake import api
from sys import platform
from time import sleep as sleep
from colours import colours
from display import clear_screen

enableSubprocesses = True         # Ghost run, does not affect the system
enableLogging = False             # Disable console logs

ADAMS_PATH = os.getcwd()                                # A.D.A.M.S. directory
USER_DIR = os.path.expanduser('~')                      # User home directory
HSD_CONFIG = USER_DIR + '/.hsd/hsd.conf'                # Location of HSD node config
HSW_CONFIG = USER_DIR + '/.hsd/hsw.conf'                # Location of HSD wallet config

HSD_API_KEY = ''
HSW_API_KEY = ''

if platform == 'linux':
    from getch import getch as getch
elif platform == 'win32':
    from msvcrt import getch as getch

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
                sleep(1)

        elif config[0] == 'enablesubprocesses':
            if config[1].lower() == 'true':
                enableSubprocesses = True
            else:
                enableSubprocesses = False
                
            if enableLogging == True:
                print('Disable Subprocesses: ' + str(enableSubprocesses))
                sleep(1)

with open(HSD_CONFIG, 'r') as hsdConfig:
    lines = hsdConfig.readlines()

for line in lines:
    if line.startswith('api-key:'):
        keyValue = line.split(':')
        HSD_API_KEY = str(keyValue[1]).strip()

with open(HSW_CONFIG, 'r') as hswConfig:
    lines = hswConfig.readlines()

for line in lines:
    if line.startswith('api-key:'):
        keyValue = line.split(':')
        HSW_API_KEY = str(keyValue[1]).strip()

class hsd_interface:
    hsd = None
    hsw = None

    def __init__(self):
        global hsd
        global hsw

        hsd = api.hsd(HSD_API_KEY, _port=14037)
        hsw = api.hsw(HSW_API_KEY, _port=14039)
    #################################################### END: __init__(self)

    def getWallets(self):
        return hsw.listWallets()
    #################################################### END: getWallets(self)

    def setWallet(self, walletID:str=''):
        hsw.rpc_selectWallet(walletID)
    #################################################### END: setWallet(self, walletID:str='')

    def getAddress(self):
        return hsw.rpc_getAccountAddress()['result']
    #################################################### END: getAddress(self)

    def getNewAddress(self):
        return hsw.rpc_getNewAddress()['result']
    #################################################### END: getNewAddress(self)

    def createWallet(self, password:str='', walletID:str='', watchOnly=False):
        if password == '':
            isMatch = False
            while isMatch == False:
                password = cli.get_input_pass(self, '\n\tEnter a password : ')
                confirm = cli.get_input(self, '\n\tRe-enter your password : ')

                if password == confirm:
                    isMatch = True
                else:
                    print(colours.yellow(self, '\n [!] ') + 'Passwords do not match, try again.')

        if walletID == '':
            walletID = cli.get_input(self, '\n\tEnter a wallet name [default = adams] : ')

            if walletID == '':
                walletID = 'adams'

        try:
            if enableSubprocesses == True:
                hsw.createWallet(password, walletID, _watchonly=watchOnly)
            else:
                print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')

            print(colours.green(self, '\n [+] ') + 'Wallet "' + walletID + '" created.')
            sleep(2)
        except:
            print(colours.yellow(self, '\n [!] ') + 'Could not create wallet.')
    #################################################### END: createWallet(self, password:str='', walletID:str='', watchOnly=False)
            
    def walletName(self):
        try:
            walletInfo = hsw.rpc_getWalletInfo()['result']
            return walletInfo['walletid']
        except:
            print(colours.yellow(self, '\n [!] ') + 'Could not get wallet id.')
    #################################################### END: walletName(self)

    def getBalance(self, walletID:str):
        hsw.rpc_selectWallet(walletID)
        balance = hsw.rpc_getBalance()
        return balance['result']
    #################################################### END: getBalance(self, walletID:str)

    def createRecord(self, namespace):
        if namespace == '':
            namespace = cli.get_input(self, '\n\tDomain Name : ')

        # Check if wallet is unlocked
        results = hsw.rpc_getWalletInfo()['result']
        for result in results:
            if results['unlocked_until'] > 0:
                isUnlocked = True
            else:
                isUnlocked = False

        # If wallet is locked, prompt for password
        if isUnlocked == False:
            passwordOK = False

            while passwordOK == False:
                password = cli.get_input_pass(self, '\n\tEnter your wallet password : ')
                result = hsw.rpc_walletPassphrase(password)['error']

                if result == None:
                    passwordOK = True
                    isUnlocked = True
                else:
                    print(colours.yellow(self, '\n [!] ') + 'Invalid password!')
                    passwordOK = False
                    isUnlocked = False

        record = {'records': [{'type': 'NS', 'ns': 'ns1.' + namespace + '.'}]}

        if enableSubprocesses == True:
            hsw.rpc_sendUPDATE(namespace, record)
        else:
            print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')

        print(colours.green(self, '\n [+] ') + 'Record created, press any key to continue')
        sleep(2)
    #################################################### END: createRecord(self, namespace)

class cli:
    hsdIFace = None
    menu_title = ''
    menu_options = ''

    def __init__(self, _type:str=None):
        global hsdIFace
        hsdIFace = hsd_interface()

        clear_screen()

        if _type == None or _type.upper() == "MAIN": 
            self.main_menu()
        elif _type.upper() == "HSW" or _type.upper() == "WALLET": 
            self.hsdManagerCli()
        
        self.main_menu()
        sleep(1)
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
        global hsdIFace
        global menu_title
        global menu_options
        
        if menu_id.upper() == 'MAIN':       # Main Menu Options
            menu_title = ['HSD_MANAGMENT',
                          'Handshake Node Management']
                          
            menu_options = [colours().cyan('1') + ': Wallet Management',
                            colours().cyan('2') + ': HNS Records Management',
                            '',
                            colours().cyan('B') + ': Back to Management',
                            colours().cyan('Q') + ': Quit A.D.A.M.S.']
            
        elif menu_id.upper() == 'HSW':      # Handshake Wallet Menu Options
            menu_title = ['HANDSHAKE_WALLET',
                          'Handshake Wallet Management']
                          
            menu_options = [colours().cyan('1') + ': Accounts and balances',
                            colours().cyan('2') + ': Send HNS',
                            colours().cyan('3') + ': Receive HNS',
                            '',
                            colours().cyan('4') + ': Create New Account',
                            '',
                            colours().cyan('B') + ': Back to HSD Management',
                            colours().cyan('Q') + ': Quit A.D.A.M.S.']
                            
                            
        elif menu_id.upper() == 'HSD_RECORDS':      # Handshake Wallet Menu Options
            menu_title = ['HANDSHAKE_RECORDS',
                          'Handshake Records Management']
                          
            menu_options = [colours().cyan('1') + ': View Records',
                            colours().cyan('2') + ': Create/Update Record',
                            '',
                            colours().cyan('B') + ': Back to HSD Management',
                            colours().cyan('Q') + ': Quit A.D.A.M.S.']

    #################################################### END: set_menu(menu_id)
    ### START: main_menu()

    def main_menu(self):
        self.set_menu('MAIN')    # Initialize A.D.A.M.S. Configuration Menu

        try:
            while True:  # Display Handshake Daemon Management Menu
                self.print_header()
                self.print_options()
    
                user_input = self.get_input('\n\tWhat would you like to do? : ')

                if user_input.upper() == '1':   # Wallet Management
                    self.hsdWallet()

                elif user_input.upper() == '2': # HNS Records Management
                    self.hsdRecordsManagerCli()

                elif user_input.upper() == 'B':
                    import manager
                    manager.cli()

                elif user_input.upper() == 'EXIT' or user_input.upper() == 'Q' or user_input.upper() == 'QUIT':
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

    def hsdWallet(self):
        global menu_title
        
        self.set_menu('HSW')    # Initialize Handshake Daemon Management Menu

        try:
            adamsWalletFound = False

            for wallet in hsdIFace.getWallets():
                if str(wallet).lower() == 'adams':
                    adamsWalletFound = True
                    
            if adamsWalletFound == False:
                print(colours.yellow(self, '\n [!] ') + 'Adams wallet not found. Creating wallet...')
                hsdIFace.createWallet(walletID='adams')
            
            hsdIFace.setWallet('adams')

            while True:  # Display Handshake Wallet Management Menu
                # self.set_menu(menu)  # Initialize Handshake Wallet Management Menu
                self.print_header()
                self.print_options()
                
                print(colours().green('\t  Wallet  : ') + str(hsdIFace.walletName()))
                print(colours().green('\t  Balance : ') + str(hsdIFace.getBalance(hsdIFace.walletName())) + ' HNS')
                print(colours().green('\t  Address : ') + str(hsdIFace.getAddress()))
    
                user_input = self.get_input('\n\tWhat would you like to do? : ')
                
                if user_input.upper() == '1':
                    #self.skynetWallet()
                    print(colours().error('Handshake accounts not yet implemented.'))
                    sleep(1)

                elif user_input.upper() == '2':
                    #self.skynetContracts()
                    print(colours().error('Handshake transactions not yet implemented.'))
                    sleep(1)

                elif user_input.upper() == '3':
                    #self.skynetBlocklists()
                    print(colours().error('Handshake transactions not yet implemented.'))
                    sleep(1)

                elif user_input.upper() == '4':
                    hsd_interface.createWallet(self)

                elif user_input.upper() == 'B':
                    self.main_menu()

                elif user_input.upper() == 'EXIT' or user_input.upper() == 'Q' or user_input.upper() == 'QUIT':
                    clear_screen()    # Clear console window
                    sys.exit(0)    
        except KeyboardInterrupt:
            self.main_menu()
            pass
    #################################################### END: hsdWallet(self)

    def hsdManagerCli(self):
        global menu_title
        
        self.set_menu('HSD')    # Initialize Handshake Daemon Management Menu

        try:
            while True:  # Display Handshake Daemon Management Menu
                self.print_header()
                self.print_options()
                
                user_input = self.get_input('\n\tWhat would you like to do? : ')
                
                if user_input.upper() == '1':   # Wallet Management
                    self.hsdWallet()

                elif user_input.upper() == '2': # HNS Records Management
                    self.hsdRecordsManagerCli()

                elif user_input.upper() == 'B':
                    self.main_menu()

                elif user_input.upper() == 'EXIT' or user_input.upper() == 'Q' or user_input.upper() == 'QUIT':
                    clear_screen()    # Clear console window
                    sys.exit(0)

        except KeyboardInterrupt:
            self.main_menu()
            pass
    #################################################### END: hsdManagerCli()

    def hsdRecordsManagerCli(self):
        global menu_title
        
        self.set_menu('HSD_RECORDS')  # Initialize Handshake Wallet Management Menu

        try:
            while True:  # Display Handshake Wallet Management Menu
                self.print_header()
                self.print_options()
                
                user_input = self.get_input('\n\tWhat would you like to do? : ')
                
                if user_input.upper() == '1':
                    #self.skynetWallet()
                    print(colours().error('Records management not yet implemented.'))
                    sleep(1)

                elif user_input.upper() == '2':
                    #self.skynetContracts()
                    print(colours().error('Records management not yet implemented.'))
                    sleep(1)

                elif user_input.upper() == 'B':
                    self.hsdManagerCli()

                elif user_input.upper() == 'EXIT' or user_input.upper() == 'Q' or user_input.upper() == 'QUIT':
                    clear_screen()    # Clear console window
                    sys.exit(0)    
        except KeyboardInterrupt:
            self.main_menu()
            pass
    #################################################### END: hsdWalletManagerCli(self)

if __name__ == "__main__":
    clear_screen()
    #hsd = hsd_interface()
    #hsd.getWallets()
    #print(hsd.getBalance('skunk'))
    cli()
#################################################### END: __main__