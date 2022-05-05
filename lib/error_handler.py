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

class Error(Exception):
    """
    Base class for other exceptions.
    """
    pass
    
class MethodNotFound(Error):
    """
    Raised when the method called is not found.
    """
    pass
    
