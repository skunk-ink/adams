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
from xml import dom

from handshake import api
from sys import platform
from time import sleep as sleep
from colours import colours
from display import clear_screen

USER_DIR = os.path.expanduser('~')                      # User home directory
ADAMS_PATH = os.getcwd()                                # A.D.A.M.S. directory
ADAMS_CONFIG = ADAMS_PATH + '/config/adams.conf'        # Location of A.D.A.M.S. config
HSD_PATH = ADAMS_PATH + '/hsd/'
HSD_CONFIG = USER_DIR + '/.hsd/hsd.conf'                # Location of HSD node config
HSW_CONFIG = USER_DIR + '/.hsd/hsw.conf'                # Location of HSD wallet config

# A.D.A.M.S. configuration variables
HNS_WALLET_ID = None
ENABLE_SUBPROCESSES = True         # Ghost run, does not affect the system
ENABLE_LOGGING = False             # Disable console logs

# Handshake configuration variables
HSD_API_KEY = None
HSW_API_KEY = None
HSD_PORT = None
HSW_PORT = None

if platform == 'linux':
    from getch import getch as getch
elif platform == 'win32':
    from msvcrt import getch as getch

if os.path.exists(HSD_CONFIG) == False and os.path.exists(HSW_CONFIG) == False and os.path.exists(HSD_PATH) == False:
    try:
        print('\033[41m\033[97m\n\t Handshake node not detected! Please install. \033[0m\033[0m')
        print('\033[93m\033[1m\n\tPress any key to install now, or use \033[96m`ctrl+c`\033[93m to return.\033[0m\033[0m')
        getch()
        from main import main
        main(['adams', 'install', 'handshake'])
    except KeyboardInterrupt:
        clear_screen()
        sys.exit(0)

elif os.path.exists(HSD_CONFIG) == False or os.path.exists(HSW_CONFIG) == False or os.path.exists(HSD_PATH) == False:
    try:
        print('\033[41m\033[97m\n\t Handshake node misconfigured! Please reinstall. \033[0m\033[0m')
        print('\033[93m\033[1m\n\tPress any key to install now, or use \033[96m`ctrl+c`\033[93m to return.\033[0m\033[0m')
        getch()
        from main import main
        main(['adams', 'install', 'handshake'])
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

        elif config[0] == 'hnswalletid':
            HNS_WALLET_ID = config[1]

            if ENABLE_LOGGING == True:
                print('HNS Wallet ID: ' + str(HNS_WALLET_ID))
                sleep(1)

with open(HSD_CONFIG, 'r') as hsdConfig:
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

with open(HSW_CONFIG, 'r') as hswConfig:
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

class hsmanager:
    hsd = None
    hsw = None

    def __init__(self):
        global hsd
        global hsw

        hsd = api.hsd(HSD_API_KEY, _port=HSD_PORT)
        hsw = api.hsw(HSW_API_KEY, _port=HSW_PORT)
    #################################################### END: __init__(self)

    def authenticate(self):
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

    def getWallets(self):
        return hsw.listWallets()
    #################################################### END: getWallets(self)

    def setWallet(self, walletID:str=''):
        hsw.rpc_selectWallet(walletID)
    #################################################### END: setWallet(self, walletID:str='')

    def getAccounts(self):
        results = hsw.rpc_listAccounts()['result']
        accounts = []

        for account in results:
            accounts.append(account)

        return accounts
    #################################################### END: getWallets(self)

    def getAccountInfo(self, accountID:str='default'):
        return hsw.getAccountInfo(HNS_WALLET_ID, accountID)
    #################################################### END: getWallets(self)

    def getAddress(self):
        return hsw.rpc_getAccountAddress()['result']
    #################################################### END: getAddress(self)

    def getNewAddress(self):
        return hsw.rpc_getNewAddress()['result']
    #################################################### END: getNewAddress(self)

    def createWallet(self, walletID:str='', watchOnly=False):
        # Prompt for wallet password
        passwordMatch = False

        while passwordMatch == False:
            password = cli.get_input_pass(self, '\n\tEnter a new password for `' + walletID + '` : ')
            confirm = cli.get_input_pass(self, '\n\tConfirm password for `' + walletID + '` : ')

            if password == confirm:
                passwordMatch = True
            else:
                print(colours.yellow(self, '\n [!] ') + 'Passwords do not match, try again.')
                passwordMatch = False

        if walletID == '':
            walletID = cli.get_input(self, '\n\tEnter name for your wallet ID : ')

        try:
            if ENABLE_SUBPROCESSES == True:
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

    def sendAuctionOpen(self, _domainName:str):
        self.authenticate()
        return hsw.rpc_sendOPEN(_domainName)['result']
    #################################################### END: sendAuctionOpen(self, _domainName:str)

    def sendAuctionBid(self, _domainName:str, _bidAmount:float, _lockupBlind:float, _accountName:str='default'):
        self.authenticate()
        return hsw.rpc_sendBID(_domainName, _bidAmount, _lockupBlind, _accountName)['result']
    #################################################### END: sendAuctionBid(self, _domainName:str, _bidAmount:float, _lockupBlind:float, _accountName:str='default')

    def sendAuctionReveal(self, _domainName:str):
        self.authenticate()
        return hsw.rpc_sendREVEAL(_domainName)['result']
    #################################################### END: sendAuctionReveal(self, _domainName:str)

    def sendAuctionRedeem(self, _domainName:str):
        self.authenticate()
        return hsw.rpc_sendREDEEM(_domainName)['result']
    #################################################### END: sendAuctionRedeem(self, _domainName:str)

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

        if ENABLE_SUBPROCESSES == True:
            hsw.rpc_sendUPDATE(namespace, record)
        else:
            print(colours.yellow(self, '\n [!] ') + 'Subprocess disabled')

        print(colours.green(self, '\n [+] ') + 'Record created')
        sleep(2)
    #################################################### END: createRecord(self, namespace)

class cli:
    hs_manager = None
    menu_title = ''
    menu_options = ''
    menu_display = []

    def __init__(self, _type:str=None):
        global HNS_WALLET_ID
        global hs_manager
        hs_manager = hsmanager()

        walletFound = False

        for wallet in hs_manager.getWallets():
            if str(wallet) == HNS_WALLET_ID:
                walletFound = True
                
        if walletFound == False:
            print(colours.yellow(self, '\n [!] ') + '`' + HNS_WALLET_ID + '` wallet not found.')

            # Prompt user to create wallet
            while walletFound == False:
                user_input = self.get_input('\n\tWould you like to create a wallet with the ID of `' + HNS_WALLET_ID + '`? [yes or no] : ')

                if user_input.lower() == 'yes' or user_input.lower() == 'y':
                    hs_manager.createWallet(HNS_WALLET_ID)

                    for wallet in hs_manager.getWallets():
                        if str(wallet) == HNS_WALLET_ID:
                            walletFound = True
                else:
                    HNS_WALLET_ID = self.get_input('\n\tEnter a name for your HNS Wallet [default = "adams"] : ')

                    if HNS_WALLET_ID == '':
                        HNS_WALLET_ID = 'adams'

                    hs_manager.createWallet(HNS_WALLET_ID)

                    for wallet in hs_manager.getWallets():
                        if str(wallet) == HNS_WALLET_ID:
                            walletFound = True

        #### UPDATE CONFIG FILE: adams.conf
        # Read `adams.conf` to memory
        with open(ADAMS_CONFIG, 'r') as script:
            adamsConfig = script.readlines()

        lnCount = 0

        # Replace 'hnsWalletID' in 'adams.conf' with newly created wallet id
        for line in adamsConfig:
            if line.startswith('hnsWalletID:'):
                adamsConfig[lnCount] = 'hnsWalletID: ' + HNS_WALLET_ID + '\n'

            lnCount += 1

        # Write new 'adams.conf' file
        with open(ADAMS_CONFIG, 'w') as script:
            script.writelines(adamsConfig)

        # Set wallet RPC to specified wallet id
            hs_manager.setWallet(HNS_WALLET_ID)

        clear_screen()

        if _type == None or _type.upper() == "MAIN": 
            self.main_menu()
        elif _type.upper() == "HSW" or _type.upper() == "WALLET": 
            self.hsdWallet()
        elif _type.upper() == "HSD" or _type.upper() == "NODE": 
            self.hsdNode()
        
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

    def print_display(self):
        for option in self.menu_display:     # Print menu options to screen
            print('\t  ' + option)
        print()
    #################################################### END: print_options()

    def set_menu(self, menu_id):
        global hs_manager
        global menu_title
        global menu_options
        
        if menu_id.upper() == 'MAIN':       # Main Menu Options
            menu_title = ['HSD_MANAGMENT',
                          'Handshake Management']
                          
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
                            'Auction Commands:',
                            colours().cyan('4') + ': Send Open',
                            colours().cyan('5') + ': Send Bid',
                            colours().cyan('6') + ': Send Reveal',
                            colours().cyan('7') + ': Send Redeem',
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
        self.set_menu('MAIN')    # Initialize Handshake Management Menu

        # Check for `adams` wallet. If none found, prompt user to create.

        try:
            while True:  # Display Handshake Management Menu
                self.print_header()
                self.print_options()
    
                user_input = self.get_input('\n\tWhat would you like to do? : ')

                if user_input.upper() == '1':   # Wallet Management
                    self.hsdWallet()

                elif user_input.upper() == '2': # HNS Records Management
                    self.hsdNode()

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
            from main import main
            main(['adams', 'main'])
    #################################################### END: main_menu()

    def hsdWallet(self, menu_id:str='MAIN'):
        global menu_title
        global menu_options

        try:                                
            while True:  # Run Handshake Wallet Management
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

                if menu_id.upper() == 'MAIN':       # Main Menu Options
                    self.set_menu('HSW')            # Initialize Handshake Daemon Management Menu
                    self.print_header()
                    self.print_options()
                    
                    print(colours().green('\t  Wallet ID : ') + str(hs_manager.walletName()))
                    print(colours().green('\t  Balance   : ') + str(hs_manager.getBalance(hs_manager.walletName())) + ' HNS')
                    print(colours().green('\t  Address   : ') + str(hs_manager.getAddress()))
        
                    user_input = self.get_input('\n\tWhat would you like to do? : ')
                    
                    if user_input.upper() == '1':
                        menu_options = []
                        menu_id = 'ACCOUNTS'

                    elif user_input.upper() == '2':
                        menu_options = []
                        menu_id = 'SEND_HNS'

                    elif user_input.upper() == '3':
                        menu_options = []
                        menu_id = 'RECEIVE_HNS'

                    elif user_input.upper() == '4':
                        menu_options = []
                        menu_id = 'SEND_OPEN'

                    elif user_input.upper() == '5':
                        menu_options = []
                        menu_id = 'SEND_BID'

                    elif user_input.upper() == '6':
                        menu_options = []
                        menu_id = 'SEND_REVEAL'

                    elif user_input.upper() == '7':
                        menu_options = []
                        menu_id = 'SEND_REDEEM'

                    elif user_input.upper() == 'B':
                        self.main_menu()

                    elif user_input.upper() == 'EXIT' or user_input.upper() == 'Q' or user_input.upper() == 'QUIT':
                        clear_screen()    # Clear console window
                        sys.exit(0)  
                    
                elif menu_id.upper() == 'ACCOUNTS':      # Handshake Wallet Menu Options
                    user_input = None
                    while True:
                        accounts = hs_manager.getAccounts()
                            
                        menu_title = ['HANDSHAKE_WALLET',
                                    'Wallet Accounts for `' + HNS_WALLET_ID + '`']
                        menu_options = []
                        self.menu_display = []
                        accountIndex = 0
                        
                        for account in accounts:
                            accountIndex += 1
                            menu_options.append(colours().cyan(str(accountIndex)) + ': View `' + str(account) + '`')

                        menu_options.append('')
                        menu_options.append(colours().cyan('B') + ': Back to Wallet Management')
                        menu_options.append(colours().cyan('Q') + ': Quit A.D.A.M.S.')

                        clear_screen()

                        if user_input == None or user_input == ' ':
                            self.print_header()
                            self.print_options()

                            user_input = self.get_input('\n\tWhat would you like to do? : ')

                        else:
                            accountIndex = 0

                            for account in accounts:
                                accountIndex += 1

                                if user_input == str(accountIndex):
                                    results = hs_manager.getAccountInfo(str(account))

                                    self.menu_display.append(colours().green('Account ID') + '  : ' + str(results['name']))
                                    balance = results['balance']
                                    self.menu_display.append(colours().green('Balance') + '     : ' + str(balance['account']))
                                    self.menu_display.append(colours().green('Initialized') + ' : ' + str(results['initialized']))
                                    self.menu_display.append(colours().green('Watch Only') + '  : ' + str(results['watchOnly']))
                                    self.menu_display.append(colours().green('Address') + '     : ' + results['receiveAddress'])

                            self.print_header()
                            self.print_options()
                            self.print_display()
                            
                            user_input = self.get_input('\n\tWhat would you like to do? : ')
                        if user_input.upper() == 'B' or user_input.upper() == ' ':
                            self.hsdWallet('MAIN')

                        elif user_input.upper() == 'EXIT' or user_input.upper() == 'Q' or user_input.upper() == 'QUIT':
                            clear_screen()    # Clear console window
                            sys.exit(0)  
                                    
                elif menu_id.upper() == 'SEND_HNS':      # Handshake Wallet Menu Options
                    
                    print(colours().error('Transaction UI not implemented.'))
                    sleep(2)
                    self.hsdWallet('MAIN')

                    menu_title = ['HANDSHAKE_RECORDS',
                                'Send HNS']
                                
                    menu_options = [colours().cyan('1') + ': View Records',
                                    colours().cyan('2') + ': Create/Update Record',
                                    '',
                                    colours().cyan('B') + ': Back to HSD Management',
                                    colours().cyan('Q') + ': Quit A.D.A.M.S.'] 

                    self.print_header()
                    self.print_options()
        
                    user_input = self.get_input('\n\tWhat would you like to do? : ')
                    
                    if user_input.upper() == '1':
                        #View account option
                        pass

                    elif user_input.upper() == 'B':
                        self.hsdWallet('MAIN')

                    elif user_input.upper() == 'EXIT' or user_input.upper() == 'Q' or user_input.upper() == 'QUIT':
                        clear_screen()    # Clear console window
                        sys.exit(0)  
                                    
                elif menu_id.upper() == 'RECEIVE_HNS':      # Handshake Wallet Menu Options
                    
                    print(colours().error('Transaction UI not implemented.'))
                    sleep(2)
                    self.hsdWallet('MAIN')

                    menu_title = ['HANDSHAKE_RECORDS',
                                'Receive HNS']
                                
                    menu_options = [colours().cyan('1') + ': View Records',
                                    colours().cyan('2') + ': Create/Update Record',
                                    '',
                                    colours().cyan('B') + ': Back to HSD Management',
                                    colours().cyan('Q') + ': Quit A.D.A.M.S.'] 

                    self.print_header()
                    self.print_options()
        
                    user_input = self.get_input('\n\tWhat would you like to do? : ')
                    
                    if user_input.upper() == '1':
                        #View account option
                        pass

                    elif user_input.upper() == 'B':
                        self.hsdWallet('MAIN')

                    elif user_input.upper() == 'EXIT' or user_input.upper() == 'Q' or user_input.upper() == 'QUIT':
                        clear_screen()    # Clear console window
                        sys.exit(0)  
                                    
                elif menu_id.upper() == 'SEND_OPEN':      # Send OPEN on auction

                    domainName = self.get_input('\n\tEnter name of HNS domain : ')

                    try:
                        hs_manager.sendAuctionOpen(domainName)
                        print(colours.green(self, '\n [+] ') + 'Auction started for `' + domainName + '`')
                    except:
                        print(colours.yellow(self, '\n [!] ') + 'Failed to start auction for `' + domainName + '`')
                    
                    sleep(2)

                    self.hsdWallet('MAIN') 
                                    
                elif menu_id.upper() == 'SEND_BID':      # Send BID on auction

                    domainName = self.get_input('\n\tEnter name of HNS domain : ')
                    bid = self.get_input('\n\tEnter your bid : ')
                    lockupBlind = self.get_input('\n\tEnter your blind bid : ')

                    try:
                        hs_manager.sendAuctionBid(domainName, bid, lockupBlind)
                        print(colours.green(self, '\n [+] ') + 'Bid sent for `' + domainName + '`')
                    except:
                        print(colours.yellow(self, '\n [!] ') + 'Failed to send bid for `' + domainName + '`')
                    
                    sleep(2)

                    self.hsdWallet('MAIN') 
                                                        
                elif menu_id.upper() == 'SEND_REVEAL':      # Send REVEAL on auction

                    domainName = self.get_input('\n\tEnter name of HNS domain : ')

                    try:
                        hs_manager.sendAuctionReveal(domainName)
                        print(colours.green(self, '\n [+] ') + 'Reveal sent for `' + domainName + '`')
                    except:
                        print(colours.yellow(self, '\n [!] ') + 'Failed to send reveal for `' + domainName + '`')
                    
                    sleep(2)

                    self.hsdWallet('MAIN') 
                                                        
                elif menu_id.upper() == 'SEND_REDEEM':      # Send REVEAL on auction

                    domainName = self.get_input('\n\tEnter name of HNS domain : ')

                    try:
                        hs_manager.sendAuctionRedeem(domainName)
                        print(colours.green(self, '\n [+] ') + 'Redeemed `' + domainName + '`')
                    except:
                        print(colours.yellow(self, '\n [!] ') + 'Failed to redeem `' + domainName + '`')
                    
                    sleep(2)

                    self.hsdWallet('MAIN') 
                    
        except KeyboardInterrupt:
            self.main_menu()
            pass
    #################################################### END: hsdWallet(self)

    def hsdNode(self):
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
                    self.main_menu()

                elif user_input.upper() == 'EXIT' or user_input.upper() == 'Q' or user_input.upper() == 'QUIT':
                    clear_screen()    # Clear console window
                    sys.exit(0)    
        except KeyboardInterrupt:
            self.main_menu()
            pass
    #################################################### END: hsdWalletManagerCli(self)

if __name__ == "__main__":
    clear_screen()
    cli()
#################################################### END: __main__