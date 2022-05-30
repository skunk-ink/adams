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

    # Font Colours
magenta = '\033[95m'
white = '\033[97m'
black = '\033[30m'
blue = '\033[94m'
cyan = '\033[96m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'

    # Back Ground Colours
white_bg = '\033[107m'
red_bg = '\033[41m'
green_bg = '\033[102m'
blue_bg = '\033[44m'

    # Font Styles
bold = '\033[1m'
underline = '\033[4m'

    # Custom Colour Schemes
alert = '\033[1m\033[41m'

    # End escape character
endc = '\033[0m'


class colours:
    
        # Font Colours
    def black(self, text):
        return black + text + endc
        
    def white(self, text):
        return white + text + endc
        
    def yellow(self, text):
        return yellow + text + endc
        
    def red(self, text):
        return red + text + endc
    
    def blue(self, text):
        return blue + text + endc
        
    def green(self, text):
        return green + text + endc
        
    def cyan(self, text):
        return cyan + text + endc
        
        # Background Colours
    def white_bg(self, text):
        return white_bg + text + endc
        
    def red_bg(self, text):
        return red_bg + text + endc
    
    def green_bg(self, text):
        return green_bg + text + endc

    def blue_bg(self, text):
        return blue_bg + text + endc
        
        # Font Styles
    def bold(self, text):
        return bold + text + endc
        
        # Custom Font Styles
    def title(self, text):
        return green + bold + text + endc + endc
        
    def prompt(self, text):
        return yellow + bold + text + endc + endc
        
    def error(self, text):
        text = '\n\t ERROR : ' + text + ' '
        return red_bg + white + text + endc + endc
        