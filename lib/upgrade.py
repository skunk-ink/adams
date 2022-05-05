"""               _                                    
      __ _     __| |     __ _       _ _ _      ____    
     / _` |   / _` |    / _` |     | ` ` |    / __/    
    | (_| |  | (_| |   | (_| |     | | | |    \__ \    
     \__,_|⍟ \__,_|▄⍟█\__,_|██⍟▄|_|_|_| ⍟ /___/ ⍟ 
                   ████         ████                   
                 ███               ███                 
                ██                  ███                
               ██        ▄▄█▄▄        ██               
               ██      ███───███      ██               
               ██     ███──█──███     ██               
               ██      ██──▄──██      ██               
               ██        ▀▀█▀▀        ██               
                ██                   ██                
                 ███               ███                 
    Automated Decentralization And Management System   
                    ▀▀▀█████████▀▀▀                    
"""

import os

from time import sleep as sleep
from lib.colours import colours as colours

class menu(object):
    def __init__(self):
        self.clear_screen
        print(colours.error(self, "upgrade.py not yet complete."))
        sleep(1)
        
        from adams import adams as adams
        adams()

    ### START: clear_screen()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    #################################################### END: clear_screen()



if __name__ == '__main__':
    os.system('cls')
    print(colours.error("upgrade.py not yet complete."))
    sleep(1)
