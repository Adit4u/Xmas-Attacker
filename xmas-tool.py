import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""
 ██╗░░██╗███╗░░░███╗░█████╗░░██████╗░░░░░░░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
╚██╗██╔╝████╗░████║██╔══██╗██╔════╝░░░░░░██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
░╚███╔╝░██╔████╔██║███████║╚█████╗░█████╗███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
░██╔██╗░██║╚██╔╝██║██╔══██║░╚═══██╗╚════╝██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██╔╝╚██╗██║░╚═╝░██║██║░░██║██████╔╝░░░░░░██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░░░░░░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                                                                                                                   
                                                                 
BY: ! - 𝘒 𝘌 𝘕
Version 0.1 (0.2 version on its way (more tool)?)
""")

print(Fore.YELLOW+"""
1: Xmas-Tool (Hacking Tools)   | 2:Xmas-Web-Hacking-Tool
3: Xmas-Token-Generator        | 4.Spammer (Beta)
5: Information about us        | 6.SELFBOT(NOT A HACKING TOOL)
""")

command = input('> ')

if command == '1':
   os.system('cmd /k "python Xmas-Tool/xmas.py"')


elif command == '2':
  os.system('cmd /k "python Xmas-Web-Hacktool/web_bugger.py"')
    

elif command == '3':
  os.system('cmd /k "python Xmas-Gen/start.py"')

elif command == '4':
  os.system('cmd /k "python Spammers(Beta)/spammer.py"')

elif command == '5':
  os.system('cmd /k "python info.py"')

elif command == '6':
  os.system('cmd /k "python XMASSELFBOT-(NOT-HACKING-TOOL)/xmasselfbot.py"')


    
      

else:
  print('Please choose the correct one dont be dumb')
