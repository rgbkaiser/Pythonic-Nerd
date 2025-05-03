import colorama
import os
import subprocess
from colorama import Fore
import time

clear = lambda:os.system('cls')
clear()
colorama.init(autoreset=True)
os.system('title Humilator V3 - Da Discord Terminator')

class colors:
    DARKRED = '\033[31m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f'''                                                                                                                
                                     
           {colors.DARKRED}@@@@@@@@@@@@@@@@@@@@@@@@@@{colors.RESET}                                                                                  
           {colors.DARKRED}@@::::::-=+++++++++++==-=@@@@{colors.RESET}          {colors.DARKRED}[Humilator V3 | Da Discord Terminator | discord.gg/secretxsociety]{colors.RESET}
            {colors.DARKRED}@@@@@@@@=+*#%@@@@@@@@@@%#=-#@@{colors.RESET}                         
                   {colors.DARKRED}+@*@@+  :%@@%:  -@@#+=#@@{colors.RESET}              {colors.WHITE}[1] Mass Dm Spammer          [2] Server Nuker{colors.RESET}   
 {colors.DARKRED}@@@@   @@@@@@@@@@@@#@  {colors.WHITE}.@@-    =@@+{colors.RESET} {colors.DARKRED}.@%#++@@                                                
 {colors.DARKRED}@@@@@ @@@@@@@@@#:-#*  {colors.WHITE}@@          %@:{colors.RESET} {colors.DARKRED}#%#+=@@            {colors.WHITE}[3] Nitro Generator          [4] Promo Gen{colors.RESET} 
                {colors.DARKRED}@@*% {colors.WHITE}*@    %%%%%@    @-{colors.RESET} {colors.DARKRED}##*+*@ 
            {colors.DARKRED}@@@@@### {colors.WHITE}@    *=----=*.   @{colors.RESET} {colors.DARKRED}=%**:@            {colors.WHITE}[5] Account Token Grabber    [6] Token Checker {colors.RESET} 
          {colors.DARKRED}-@%::-=+%  {colors.WHITE}@  .@+------+%-  @{colors.RESET} {colors.DARKRED}-%**:@
           {colors.DARKRED}=@@@:**%# {colors.WHITE}@    *=----=*.   @{colors.RESET} {colors.DARKRED}=%**:@            {colors.WHITE}[7] Self Bot                 [8] Server Cloner{colors.RESET}
              {colors.DARKRED}@:+*#% {colors.WHITE}@@   .#%###@    @={colors.RESET} {colors.DARKRED}##*+*@ 
              {colors.DARKRED}@@=+*%* {colors.WHITE}:@@          *@-{colors.RESET} {colors.DARKRED}*%#*=@@            {colors.WHITE}[9] Status Rotator           [10] Mass Unban{colors.RESET} 
               {colors.DARKRED}@@++*%@  {colors.WHITE}:@@.     @@*{colors.RESET}  {colors.DARKRED}@%#++@@  
                {colors.DARKRED}@@*-+#@@:  {colors.WHITE}-@@@@={colors.RESET}  {colors.DARKRED}:@@#+=#@@   
                  {colors.DARKRED}@@#-+#%@@@%##@@@@%#+=*@@     
                    {colors.DARKRED}@@@#--=+****+=--#@@@       
                       {colors.DARKRED}@@@@@@@@@@@@@@          
                             {colors.DARKRED}..   

{colors.WHITE}Credit: {colors.RESET}{colors.RED}rgbkaiser{colors.RESET}
{colors.WHITE}Server: {colors.RESET}{colors.RED}discord.gg/secretxsociety{colors.RESET}

{colors.DARKRED}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{colors.RESET}
\n''')

choice = int(input(f"{colors.WHITE}Enter The Tool Number 》 "))
print(f"{colors.RESET}\n")
print(f"{colors.DARKRED}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{colors.RESET}")
print()

def dmSpammer():
    subprocess.run([r"resource/dmSpammer/dmSpammer.exe"])

def ServerNuker():
    subprocess.run(["python", "resource/ServerNuker.py"])

def NitroGen():
    subprocess.run(["python", "resource/NitroGen.py"])

def MassUnabn():
    subprocess.run(["python", "resource/MassUnban.py"])

def TokenGrabber():
    subprocess.run(["python", "resource/TokenGrabber/TokenGrabber.py"])

def SelfBot():
    subprocess.run(["python", "resource/SelfBot/SelfBot.py"])

def TokenChecker():
    subprocess.run(["python", "resource/TokenChecker/TokenChecker.py"])

def ServerCloner():
    subprocess.run(["python", "resource/ServerCloner.py"])

def StausRotator():
    subprocess.run(["python", "resource/StatusRotator.py"])
def PromoGen():
    subprocess.run(["python", "resource/PromoGen.py"])


if choice == 1:
    dmSpammer()
elif choice == 2:
    ServerNuker()
elif choice == 3:
    NitroGen()
elif choice == 4:
    PromoGen()
elif choice == 5:
    TokenGrabber()
elif choice == 6:
    TokenChecker()
elif choice == 7:
    SelfBot()
elif choice == 8:
    ServerCloner()
elif choice == 9:
    StausRotator()
elif choice == 10:
    PromoGen()
elif choice > 10 or choice < 1:
    print(f"{colors.WHITE}❌ INVALID SELECTION ❌{colors.RESET}")

print(f"\n{colors.DARKRED}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{colors.RESET}\n\n")

PAUSE = input(f"{colors.RED}Press Enter To Exit...")

print(f"\n\n{colors.DARKRED}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{colors.RESET}\n")
time.sleep(2)





