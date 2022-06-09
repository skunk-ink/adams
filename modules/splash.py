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
from skunkworks_ui.cli import Menu
from skunkworks_ui.style import *

if platform == "linux":
    from getch import getch as getch
elif platform == "win32":
    from msvcrt import getch as getch

class Splash(Menu):
    def __init__(self):
        self.clear_screen()
        self.print_splash()
    
    #################################################### END: __init__(self)

    def print_splash(self):
        #Pallets: ░ ▄ ▀ █ ─ `
        try: 
            print()
            print(yellow_font("\t                  _                                    "))
            print(yellow_font("\t     __ _      __| |     __ _      _ _ _      ____     "))
            print(yellow_font("\t    / _` |    / _` |    / _` |    | ` ` |    / __/     "))
            print(yellow_font("\t   | (_| |   | (_| |   | (_| |    | | | |    \__ \     "))
            print(yellow_font("\t    \__,_| ⍟  \__,_|") + green_font("▄") + yellow_font("⍟") + green_font(" ▄") + yellow_font("\__,_|") + green_font("█") + yellow_font("⍟") + green_font(" ▄") + yellow_font("|_|_|_| ⍟  /___/ ⍟  "))
            print(green_font("\t                   ███           ███                   "))
            print(green_font("\t                 ███               ███                 "))
            print(green_font("\t                ██                   ██                "))
            print(green_font("\t                         ") + green_font("▄▄█▄▄                         "))
            print(green_font("\t               ") + white_font("▄       ") + green_font("███") + white_bg("───") + green_font("███       ") + white_font("▄               "))
            print(green_font("\t              ") + white_font("███     ") + green_font("███") + white_bg("──") + green_font("█") + white_bg("──") + green_font("███     ") + white_font("███              "))
            print(green_font("\t               ") + white_font("▀       ") + green_font("██") + white_bg("──") + green_font(white_bg("▄")) + white_bg("──") + green_font("██       ") + white_font("▀               "))
            print(green_font("\t                         ") + green_font("▀▀█▀▀                         "))
            print(green_font("\t                ██                   ██                "))
            print(green_font("\t                 ███               ███                 "))
            print(yellow_font("\t    Automated Decentralization And Management System   "))
            print(green_font("\t                    ▀▀▀█████████▀▀▀                    "))
            print(white_font("\t                                                       "))
            print(white_font("\t                     press any key                     "))
            print(white_font("\t                                                       "))
            print(white_font("\t                 WHERE'S THE ANY KEY!?                 "))
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
            print(yellow_font("\t                  _                                    "))
            print(yellow_font("\t     __ _      __| |     __ _      _ _ _      ____     "))
            print(yellow_font("\t    / _` |    / _` |    / _` |    | ` ` |    / __/     "))
            print(yellow_font("\t   | (_| |   | (_| |   | (_| |    | | | |    \__ \     "))
            print(yellow_font("\t    \__,_| ⍟  \__,_|") + blue_font("▄") + yellow_font("⍟") + blue_font(" ▄") + yellow_font("\__,_|") + blue_font("█") + yellow_font("⍟") + blue_font(" ▄") + yellow_font("|_|_|_| ⍟  /___/ ⍟  "))
            print(blue_font("\t                   ███           ███                   "))
            print(blue_font("\t                 ███               ███                 "))
            print(blue_font("\t                ██                   ██                "))
            print(blue_font("\t                         ") + blue_font("▄▄█▄▄                         "))
            print(blue_font("\t               ") + white_font("▄       ") + blue_font("███") + white_bg("───") + blue_font("███       ") + white_font("▄               "))
            print(blue_font("\t              ") + white_font("███     ") + blue_font("███") + white_bg("──") + blue_font("█") + white_bg("──") + blue_font("███     ") + white_font("███              "))
            print(blue_font("\t               ") + white_font("▀       ") + blue_font("██") + white_bg("──") + blue_font(white_bg("▄")) + white_bg("──") + blue_font("██       ") + white_font("▀               "))
            print(blue_font("\t                         ") + blue_font("▀▀█▀▀                         "))
            print(blue_font("\t                ██                   ██                "))
            print(blue_font("\t                 ███               ███                 "))
            print(yellow_font("\t    Automated Decentralization And Management System   "))
            print(blue_font("\t                    ▀▀▀█████████▀▀▀                    "))
            print(white_font("\t                                                       "))
            print(white_font("\t                     press any key                     "))
            print(white_font("\t                                                       "))
            print(white_font("\t                 WHERE'S THE ANY KEY!?                 "))
            print()

        except AttributeError as e:
            sys.exit(0)
            
        except KeyboardInterrupt:
            sys.exit(0)
        
        getch()
    #################################################### END: print_splash2(self)