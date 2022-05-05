"""               _                                    
      __ _     __| |     __ _       _ _ _      ____    
     / _` |   / _` |    / _` |     | ` ` |    / __/    
    | (_| |  | (_| |   | (_| |     | | | |    \__ \    
     \__,_|⍟ \__,_|▄⍟█\__,_|██⍟▄|_|_|_| ⍟ /___/ ⍟ 
                   ████         ████                   
                 ███               ███                 
                ██                  ███                
               ██        ▄▄█▄▄        ██               
                       ███───███                       
               ██     ███──█──███     ██               
                       ██──▄──██                       
               ██        ▀▀█▀▀        ██               
                ██                   ██                
                 ███               ███                 
    Automated Decentralization And Management System   
                    ▀▀▀█████████▀▀▀                    
"""

import time
import os
from sys import platform
from lib.colours import colours as colours

if platform == "linux":
    from getch import getch as getch
elif platform == "win32":
    from msvcrt import getch as getch

class splash(object):
    def __init__(self):
        self.clear_screen()
        self.print_splash()

    ### START: clear_screen()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    #################################################### END: clear_screen()

    def print_splash(self):
        #Pallets: ░ ▄ █ ─ ` 
        print()
        print(colours().yellow("\t                  _                                    "))
        print(colours().yellow("\t      __ _     __| |     __ _       _ _ _     ____     "))
        print(colours().yellow("\t     / _` |   / _` |    / _` |     | ` ` |   / __/     "))
        print(colours().yellow("\t    | (_| |  | (_| |   | (_| |     | | | |   \__ \     "))
        print(colours().yellow("\t     \__,_|⍟  \__,_|") + colours().blue("▄") + colours().yellow("⍟") + colours().blue(" █") + colours().yellow("\__,_|") + colours().blue("██") + colours().yellow("⍟") + colours().blue(" ▄") + colours().yellow("|_|_|_| ⍟ /___/ ⍟ "))
        print(colours().blue("\t                   ████         ████                   "))
        print(colours().blue("\t                 ███               ███                 "))
        print(colours().blue("\t                ██                  ███                "))
        print(colours().blue("\t               ██        ") + colours().blue("▄▄█▄▄") + colours().blue("        ██"))
        print(colours().blue("\t                       ") + colours().blue("███") + colours().white_bg("───") + colours().blue("███") + colours().blue("                       "))
        print(colours().blue("\t               ") + colours().white("██     ") + colours().blue("███") + colours().white_bg("──") + colours().blue("█") + colours().white_bg("──") + colours().blue("███") + colours().white("     ██               "))
        print(colours().blue("\t                       ") + colours().blue("██") + colours().white_bg("──") + colours().blue(colours().white_bg("▄")) + colours().white_bg("──") + colours().blue("██") + colours().blue("                       "))
        print(colours().blue("\t               ██        ") + colours().blue("▀▀█▀▀") + colours().blue("        ██               "))
        print(colours().blue("\t                ██                   ██                "))
        print(colours().blue("\t                 ███               ███                 "))
        print(colours().yellow("\t    Automated Decentralization And Management System   "))
        print(colours().blue("\t                    ▀▀▀█████████▀▀▀                    "))
        print(colours().white("\t                                                       "))
        print(colours().white("\t                     press any key                     "))
        print(colours().white("\t                                                       "))
        print(colours().white("\t                 WHERE'S THE ANY KEY!?                 "))
        print()
        
        getch()
    