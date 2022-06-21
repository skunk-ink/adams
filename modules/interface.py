import os
import subprocess

from sys import platform
from handshake import api
from skunkworks_ui.cli import Menu
from skunkworks_ui.style import *

if platform == 'linux':
    from getch import getch as getch
elif platform == 'win32':
    from msvcrt import getch as getch

_USER_DIR = os.path.expanduser('~')                 # User home directory
_ADAMS_PATH = os.getcwd()                           # A.D.A.M.S. directory
_ADAMS_CONFIG = _ADAMS_PATH + '/config/adams.conf'  # Location of A.D.A.M.S. config

_enable_subprocesses = True                         # Ghost run, does not affect the system
_enable_logging = False                             # Enable console logs

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
                _enable_logging = True
            else:
                _enable_logging = False

            if _enable_logging == True:
                print('[Logging] `interface.py` disabled Logging: ' + str(_enable_logging))

        elif config[0] == 'enable_subprocesses':
            if config[1].lower() == 'true':
                _enable_subprocesses = True
            else:
                _enable_subprocesses = False
                
            if _enable_logging == True:
                print('[Logging] `interface.py` disabled Subprocesses: ' + str(_enable_subprocesses))



"""
 /$$   /$$  /$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$  /$$   /$$ /$$$$$$$$
| $$  | $$ /$$__  $$| $$$ | $$| $$__  $$ /$$__  $$| $$  | $$ /$$__  $$| $$  /$$/| $$_____/
| $$  | $$| $$  \ $$| $$$$| $$| $$  \ $$| $$  \__/| $$  | $$| $$  \ $$| $$ /$$/ | $$      
| $$$$$$$$| $$$$$$$$| $$ $$ $$| $$  | $$|  $$$$$$ | $$$$$$$$| $$$$$$$$| $$$$$/  | $$$$$   
| $$__  $$| $$__  $$| $$  $$$$| $$  | $$ \____  $$| $$__  $$| $$__  $$| $$  $$  | $$__/   
| $$  | $$| $$  | $$| $$\  $$$| $$  | $$ /$$  \ $$| $$  | $$| $$  | $$| $$\  $$ | $$      
| $$  | $$| $$  | $$| $$ \  $$| $$$$$$$/|  $$$$$$/| $$  | $$| $$  | $$| $$ \  $$| $$$$$$$$
|__/  |__/|__/  |__/|__/  \__/|_______/  \______/ |__/  |__/|__/  |__/|__/  \__/|________/
"""


class HSD(Menu):
    global _USER_DIR
    global _ADAMS_PATH
    global _ADAMS_CONFIG
    global _enable_subprocesses
    global _enable_logging


    _HSD_PATH = _ADAMS_PATH + '/hsd/'               # HSD directory
    _HSD_CONFIG = _USER_DIR + '/.hsd/hsd.conf'      # Location of HSD node config
    _HSW_CONFIG = _USER_DIR + '/.hsd/hsw.conf'      # Location of HSD wallet config

    _HNS_WALLET_ID = None                           # HNS wallet id

    # Handshake configuration variables
    _HSD_API_KEY = None                             # HSD API key
    _HSW_API_KEY = None                             # HSW API key
    _HSD_PORT = None                                # HSD port
    _HSW_PORT = None                                # HSW port

    hsd = None                                      # HSD Instance
    hsw = None                                      # HSW Instance

    if os.path.exists(_HSD_CONFIG):
    # Read HSD config file
        with open(_HSD_CONFIG, 'r') as hsd_config:
            lines = hsd_config.readlines()

        for line in lines:
            if line.startswith('api-key:'):
                key_value = line.split(':')
                _HSD_API_KEY = str(key_value[1]).strip()
            elif line.startswith('network:'):
                key_value = line.split(':')
                network_type = str(key_value[1]).strip()

                if network_type.lower() == 'main':
                    _HSD_PORT = 12037
                elif network_type.lower() == 'testnet':
                    _HSD_PORT = 13037
                elif network_type.lower() == 'regtest':
                    _HSD_PORT = 14037
                elif network_type.lower() == 'simnet':
                    _HSD_PORT = 15037
    else:
        print(red_font('\n [!] ') + 'Could not locate `hsd.conf` configuration file.')

    if os.path.exists(_HSW_CONFIG):
        # Read HSW config file
        with open(_HSW_CONFIG, 'r') as hsw_config:
            lines = hsw_config.readlines()

        for line in lines:
            if line.startswith('api-key:'):
                key_value = line.split(':')
                _HSW_API_KEY = str(key_value[1]).strip()
            elif line.startswith('network:'):
                key_value = line.split(':')
                network_type = str(key_value[1]).strip()

                if network_type.lower() == 'main':
                    _HSW_PORT = 12039
                elif network_type.lower() == 'testnet':
                    _HSW_PORT = 13039
                elif network_type.lower() == 'regtest':
                    _HSW_PORT = 14039
                elif network_type.lower() == 'simnet':
                    _HSW_PORT = 15039
    else:
        print(red_font('\n [!] ') + 'Could not locate `hsw.conf` configuration file.')
    
    def __init__(self):
        global hsd
        global hsw

        hsd = api.hsd(api_key=self._HSD_API_KEY, port=self._HSD_PORT)
        hsw = api.hsw(api_key=self._HSW_API_KEY, port=self._HSW_PORT)

        if _enable_logging == True:
            print('[Logging] HSD Port   : ' + str(self._HSD_PORT))
            print('[Logging] HSD Api-Key: ' + str(self._HSD_API_KEY))
            print('[Logging] HSW Port   : ' + str(self._HSW_PORT))
            print('[Logging] HSW Api-Key: ' + str(self._HSW_API_KEY))
            self.pause()
        #################################################### END: __init__(self)

    def authenticate(self):
        # Check if wallet is unlocked
        results = hsw.rpc_getWalletInfo()['result']
        for result in results:
            if results['unlocked_until'] > 0:
                is_unlocked = True
            else:
                is_unlocked = False

        # If wallet is locked, prompt for password
        if is_unlocked == False:
            password_ok = False

            while password_ok == False:
                password = self.get_input_pass('\n\tEnter your wallet password : ')
                result = hsw.rpc_walletPassphrase(password)['error']

                if result == None:
                    password_ok = True
                    is_unlocked = True
                else:
                    print(yellow_font('\n [!] ') + 'Invalid password!')
                    password_ok = False
                    is_unlocked = False
        #################################################### END: authenticate(self)

    def getWallets(self):
        return hsw.listWallets()
        #################################################### END: getWallets(self)

    def setWallet(self, wallet_id:str=''):
        hsw.rpc_selectWallet(wallet_id)
        #################################################### END: setWallet(self, wallet_id:str='')

    def getAccounts(self):
        results = hsw.rpc_listAccounts()['result']
        accounts = []

        for account in results:
            accounts.append(account)

        return accounts
        #################################################### END: getAccounts(self)

    def getAccountInfo(self, accountID:str='default'):
        return hsw.getAccountInfo(str(self._HNS_WALLET_ID), accountID)
        #################################################### END: getAccountInfo(self, accountID:str='default')

    def getAddress(self):
        return hsw.rpc_getAccountAddress()['result']
        #################################################### END: getAddress(self)

    def getNewAddress(self):
        return hsw.rpc_getNewAddress()['result']
        #################################################### END: getNewAddress(self)

    def createWallet(self, wallet_id:str='', watch_only=False):
        # Prompt for wallet password
        password_match = False

        while password_match == False:
            password = self.get_input_pass('\n\tEnter a new password for `' + wallet_id + '` : ')
            confirm = self.get_input_pass('\n\tConfirm password for `' + wallet_id + '` : ')

            if password == confirm:
                password_match = True
            else:
                print(yellow_font('\n [!] ') + 'Passwords do not match, try again.')
                password_match = False

        if wallet_id == '':
            wallet_id = self.get_input('\n\tEnter name for your wallet ID : ')

        try:
            if _enable_subprocesses == True:
                hsw.createWallet(password, wallet_id, watch_only=watch_only)
            else:
                print(yellow_font('\n [!] ') + 'Subprocess disabled')

            print(green_font('\n [+] ') + 'Wallet "' + wallet_id + '" created.')
            self.wait(2)
        except:
            print(yellow_font('\n [!] ') + 'Could not create wallet.')
        #################################################### END: createWallet(self, password:str='', wallet_id:str='', watch_only=False)
            
    def walletName(self):
        try:
            wallet_info = hsw.rpc_getWalletInfo()['result']
            return wallet_info['walletid']
        except:
            print(yellow_font('\n [!] ') + 'Could not get wallet id.')
        #################################################### END: walletName(self)

    def getBalance(self, wallet_id:str):
        hsw.rpc_selectWallet(wallet_id)
        balance = hsw.rpc_getBalance()
        return balance['result']
        #################################################### END: getBalance(self, wallet_id:str)

    def sendAuctionOpen(self, domain_name:str):
        self.authenticate()     # Unlock wallet
        return hsw.rpc_sendOPEN(domain_name)['result']
        #################################################### END: sendAuctionOpen(self, domain_name:str)

    def sendAuctionBid(self, domain_name:str, bid_amount:float, lockup_blind:float, account_name:str='default'):
        self.authenticate()     # Unlock wallet
        return hsw.rpc_sendBID(domain_name, bid_amount, lockup_blind, account_name)['result']
        #################################################### END: sendAuctionBid(self, domain_name:str, bid_amount:float, lockup_blind:float, account_name:str='default')

    def sendAuctionReveal(self, domain_name:str):
        self.authenticate()     # Unlock wallet
        return hsw.rpc_sendREVEAL(domain_name)['result']
        #################################################### END: sendAuctionReveal(self, domain_name:str)

    def sendAuctionRedeem(self, domain_name:str):
        self.authenticate()     # Unlock wallet
        return hsw.rpc_sendREDEEM(domain_name)['result']
        #################################################### END: sendAuctionRedeem(self, domain_name:str)

    def viewRecords(self, domain_name:str):
        self.authenticate()
        return hsd.rpc_getNameResource(domain_name)['result']
        #################################################### END: viewRecords(self, domain_name:str)

    def createRecord(self, domain_name:str=None, record_type:str=None, ns_value:str=None, record_value:str=None,
                           address:str=None, key_tag:int=None, algo:int=None, digest_type:int=None, digest:str=None):
        print(green_font('\n [+] ') + 'Creating HNS record...')
        print('\tDomain name : ' + str(domain_name))
        print('\tRecord type : ' + str(record_type))
        print('\tNS value : ' + str(ns_value))
        print('\tRecord value : ' + str(record_value))
        print('\tAddress : ' + str(address))
        print('\tKey tag : ' + str(key_tag))
        print('\tAlgorithm : ' + str(algo))
        print('\tDigest type : ' + str(digest_type))
        print('\tDigest : ' + str(digest))

        record = None
        is_record_type = False
        #self.authenticate()     # Unlock wallet
        if domain_name == '':
            domain_name = self.get_input('\n\tDomain Name : ')

        # Check if wallet is unlocked
        results = hsw.rpc_getWalletInfo()['result']
        for result in results:
            if results['unlocked_until'] > 0:
                is_unlocked = True
            else:
                is_unlocked = False

        # If wallet is locked, prompt for password
        if is_unlocked == False:
            password_ok = False

            while password_ok == False:
                password = self.get_input_pass('\n\tEnter your wallet password : ')
                result = hsw.rpc_walletPassphrase(password)['error']

                if result == None:
                    password_ok = True
                    is_unlocked = True
                else:
                    print(yellow_font('\n [!] ') + 'Invalid password!')
                    password_ok = False
                    is_unlocked = False

        if domain_name == None:
            domain_name = self.get_input('\n\tDomain Name : ')

        if record_type == None:
            is_record_type = False
            record_type = ''

        if record_type.upper() == 'DS' or record_type.upper() == 'NS' or record_type.upper() == 'GLUE4' or record_type.upper() == 'GLUE6' \
        or record_type.upper() == 'SYNTH4' or record_type.upper() == 'SYNTH6' or record_type.upper() == 'TXT':
            is_record_type = True

        if is_record_type == False:
            while is_record_type == False:
                print('\t\t\nRecord Types = \'DS\', \'NS\', \'GLUE4\', \'GLUE6\', \'SYNTH4\', \'SYNTH6\', \'TXT\'')
                record_type = str(self.get_input('\n\tRecord Type : '))

                if record_type.upper() == 'DS' or record_type.upper() == 'NS' or record_type.upper() == 'GLUE4' or record_type.upper() == 'GLUE6' \
                or record_type.upper() == 'SYNTH4' or record_type.upper() == 'SYNTH6' or record_type.upper() == 'TXT':
                    is_record_type = True
                else:
                    print(yellow_font('\n [!] \'') + record_type + '\' is not a valid record type.')
                    is_record_type = False

        if record_type.upper() == 'DS':
            key_tag = int(self.get_input('\n\tKey Tag : '))
            algo = int(self.get_input('\n\tAlgorithm : '))
            digest_type = int(self.get_input('\n\tDigest Type : '))
            digest = str(self.get_input('\n\tDigest : '))

            record = { 'records': [{ 'type': record_type.upper() , 'keyTag': str(key_tag), 'algorithm': str(algo), 'digestType': str(digest_type), 'digest': digest }] }

        elif record_type.upper() == 'NS':
            ns_value = self.get_input('\n\tNS : ')

            is_record_type = True
            record = { 'records': [{ 'type': record_type.upper(), 'ns': ns_value }] }

        elif record_type.upper() == 'GLUE4':
            ns_value = self.get_input('\n\tNS : ')
            address = self.get_input('\n\tAddress : ')

            is_record_type = True
            record = { 'records': [{ 'type': record_type.upper(), 'ns': ns_value, 'address': address }] }

        elif record_type.upper() == 'GLUE6':
            ns_value = self.get_input('\n\tNS : ')
            address = self.get_input('\n\tAddress : ')

            is_record_type = True
            record = { 'records': [{ 'type': record_type.upper(), 'ns': ns_value, 'address': address }] }

        elif record_type.upper() == 'SYNTH4':
            address = self.get_input('\n\tAddress : ')

            is_record_type = True
            record = { 'records': [{ 'type': record_type.upper(), 'address': address }] }

        elif record_type.upper() == 'SYNTH6':
            address = self.get_input('\n\tAddress : ')

            is_record_type = True
            record = { 'records': [{ 'type': record_type.upper(), 'address': address }] }

        elif record_type.upper() == 'TXT':
            if record_value == None:
                record_value = self.get_input('\n\tTXT Record Value : ')

            is_record_type = True
            record = { 'records': [{ 'type': record_type.upper(), 'txt': [ record_value ] }] }
        else:
            print(yellow_font('\n [!] \'') + record_type + '\' is not a valid record type.')
            is_record_type = False

        if _enable_subprocesses == True:
            result = hsw.rpc_sendUPDATE(domain_name, record)
        else:
            print(yellow_font('\n [!] ') + 'Subprocess disabled')

        print(green_font('\n [+] ') + 'Record created')
        print(record)
        self.wait(1)
        return result
        #################################################### END: createRecord(self, domain_name)



"""
 /$$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$ /$$$$$$$        /$$$$$$$  /$$   /$$  /$$$$$$ 
| $$__  $$ /$$__  $$| $$  /$ | $$| $$_____/| $$__  $$      | $$__  $$| $$$ | $$ /$$__  $$
| $$  \ $$| $$  \ $$| $$ /$$$| $$| $$      | $$  \ $$      | $$  \ $$| $$$$| $$| $$  \__/
| $$$$$$$/| $$  | $$| $$/$$ $$ $$| $$$$$   | $$$$$$$/      | $$  | $$| $$ $$ $$|  $$$$$$ 
| $$____/ | $$  | $$| $$$$_  $$$$| $$__/   | $$__  $$      | $$  | $$| $$  $$$$ \____  $$
| $$      | $$  | $$| $$$/ \  $$$| $$      | $$  \ $$      | $$  | $$| $$\  $$$ /$$  \ $$
| $$      |  $$$$$$/| $$/   \  $$| $$$$$$$$| $$  | $$      | $$$$$$$/| $$ \  $$|  $$$$$$/
|__/       \______/ |__/     \__/|________/|__/  |__/      |_______/ |__/  \__/ \______/ 
"""


class PDNS(Menu):
    def __init__(self):
        pass

    def createZone(self, domain_name:str=None):

        if domain_name == '' or domain_name == None:
            domain_name = self.get_input('\n\tDomain Name : ')

        # Create a new zone
        if _enable_subprocesses == True:
            subprocess.run(['sudo', '-u', 'pdns', 'pdnsutil', 'create-zone', domain_name , 'ns1.' + domain_name], check=True)
        else:
            print(yellow_font('\n [!] ') + 'Subprocess disabled')

        print(green_font('\n [+] ') + 'Zone created')
        self.wait(2)     
    #################################################### END: createZone(self)

    def secureZone(self, domain_name:str=None):
        
        if domain_name == '' or domain_name == None:
            domain_name = self.get_input('\n\tEnter zone name to secure : ')

        # Secure an existing zone
        if _enable_subprocesses == True:
            subprocess.run(['sudo', '-u', 'pdns', 'pdnsutil', 'secure-zone', domain_name], check=True)
        else:
            print(yellow_font('\n [!] ') + 'Subprocess disabled')

        print(green_font('\n [+] ') + 'Zone secured')
        self.wait(2)
    #################################################### END: secureZone(self)

    def createRecord(self, domain_name:str=None, record_name:str=None, record_type:str=None, record_value:str=None):

        if domain_name == '' or domain_name == None:
            domain_name = self.get_input('\n\tDomain Name : ')

        if record_type == '' or record_type == None:
            record_type = str(self.get_input('\n\tRecord Type : ')).upper()

        if record_name == '' or record_name == None:
            record_name = self.get_input('\n\tRecord Name : ')

        if record_value == '' or record_value == None:
            record_value = self.get_input('\n\tRecord Value : ')
            record_value = record_value

        # Update PowerDNS Record
        if _enable_subprocesses == True:
            subprocess.run(['sudo', '-u', 'pdns', 'pdnsutil', 'add-record', domain_name + '.', record_name, record_type, '"' + record_value + '"'], check=True)
        else:
            print(yellow_font('\n [!] ') + 'Subprocess disabled')

        print(green_font('\n [+] ') + 'Record created')
        self.wait(1)

        update_hns_record = self.get_input('\n\tUpdate handshake records (Y/N)? [default = N] : ')
        if update_hns_record.lower() == 'y':
            if _enable_logging == True: print('pdnsManager: var domain_name = ' + domain_name) # Log output
            print(HSD().createRecord(domain_name=domain_name, record_type=record_type, record_value=record_value))
            self.pause()
    #################################################### END: createRecord(self, domain_name, record_name, record_type, record_value)