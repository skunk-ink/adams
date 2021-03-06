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

import sys as sys

from sys import platform
from display import clear_screen
from colours import colours

if platform == "linux":
    from getch import getch as getch
elif platform == "win32":
    from msvcrt import getch as getch

class splash:
    def __init__(self):
        clear_screen()
        self.print_splash()
    
    #################################################### END: __init__(self)

    def print_splash(self):
        #Pallets: ░ ▄ ▀ █ ─ `
        try: 
            print()
            print(colours().yellow("\t                  _                                    "))
            print(colours().yellow("\t     __ _      __| |     __ _      _ _ _      ____     "))
            print(colours().yellow("\t    / _` |    / _` |    / _` |    | ` ` |    / __/     "))
            print(colours().yellow("\t   | (_| |   | (_| |   | (_| |    | | | |    \__ \     "))
            print(colours().yellow("\t    \__,_| ⍟  \__,_|") + colours().green("▄") + colours().yellow("⍟") + colours().green(" ▄") + colours().yellow("\__,_|") + colours().green("█") + colours().yellow("⍟") + colours().green(" ▄") + colours().yellow("|_|_|_| ⍟  /___/ ⍟  "))
            print(colours().green("\t                   ███           ███                   "))
            print(colours().green("\t                 ███               ███                 "))
            print(colours().green("\t                ██                   ██                "))
            print(colours().green("\t                         ") + colours().green("▄▄█▄▄                         "))
            print(colours().green("\t               ") + colours().white("▄       ") + colours().green("███") + colours().white_bg("───") + colours().green("███       ") + colours().white("▄               "))
            print(colours().green("\t              ") + colours().white("███     ") + colours().green("███") + colours().white_bg("──") + colours().green("█") + colours().white_bg("──") + colours().green("███     ") + colours().white("███              "))
            print(colours().green("\t               ") + colours().white("▀       ") + colours().green("██") + colours().white_bg("──") + colours().green(colours().white_bg("▄")) + colours().white_bg("──") + colours().green("██       ") + colours().white("▀               "))
            print(colours().green("\t                         ") + colours().green("▀▀█▀▀                         "))
            print(colours().green("\t                ██                   ██                "))
            print(colours().green("\t                 ███               ███                 "))
            print(colours().yellow("\t    Automated Decentralization And Management System   "))
            print(colours().green("\t                    ▀▀▀█████████▀▀▀                    "))
            print(colours().white("\t                                                       "))
            print(colours().white("\t                     press any key                     "))
            print(colours().white("\t                                                       "))
            print(colours().white("\t                 WHERE'S THE ANY KEY!?                 "))
            print()

        except AttributeError as e:
            sys.exit(0)

        except KeyboardInterrupt:
            sys.exit(0)
        
        getch()
    #################################################### END: print_splash(self)

    def print_splash2(self):
        #Pallets: ░ ▄ █ ─ ` 
        try:
            print()
            print(colours().yellow("\t                  _                                    "))
            print(colours().yellow("\t     __ _      __| |     __ _      _ _ _      ____     "))
            print(colours().yellow("\t    / _` |    / _` |    / _` |    | ` ` |    / __/     "))
            print(colours().yellow("\t   | (_| |   | (_| |   | (_| |    | | | |    \__ \     "))
            print(colours().yellow("\t    \__,_| ⍟  \__,_|") + colours().blue("▄") + colours().yellow("⍟") + colours().blue(" ▄") + colours().yellow("\__,_|") + colours().blue("█") + colours().yellow("⍟") + colours().blue(" ▄") + colours().yellow("|_|_|_| ⍟  /___/ ⍟  "))
            print(colours().blue("\t                   ███           ███                   "))
            print(colours().blue("\t                 ███               ███                 "))
            print(colours().blue("\t                ██                   ██                "))
            print(colours().blue("\t                         ") + colours().blue("▄▄█▄▄                         "))
            print(colours().blue("\t               ") + colours().white("▄       ") + colours().blue("███") + colours().white_bg("───") + colours().blue("███       ") + colours().white("▄               "))
            print(colours().blue("\t              ") + colours().white("███     ") + colours().blue("███") + colours().white_bg("──") + colours().blue("█") + colours().white_bg("──") + colours().blue("███     ") + colours().white("███              "))
            print(colours().blue("\t               ") + colours().white("▀       ") + colours().blue("██") + colours().white_bg("──") + colours().blue(colours().white_bg("▄")) + colours().white_bg("──") + colours().blue("██       ") + colours().white("▀               "))
            print(colours().blue("\t                         ") + colours().blue("▀▀█▀▀                         "))
            print(colours().blue("\t                ██                   ██                "))
            print(colours().blue("\t                 ███               ███                 "))
            print(colours().yellow("\t    Automated Decentralization And Management System   "))
            print(colours().blue("\t                    ▀▀▀█████████▀▀▀                    "))
            print(colours().white("\t                                                       "))
            print(colours().white("\t                     press any key                     "))
            print(colours().white("\t                                                       "))
            print(colours().white("\t                 WHERE'S THE ANY KEY!?                 "))
            print()

        except AttributeError as e:
            sys.exit(0)
            
        except KeyboardInterrupt:
            sys.exit(0)
        
        getch()
    #################################################### END: print_splash2(self)