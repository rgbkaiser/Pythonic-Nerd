import ctypes
import requests
import random
import string
import time
import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

# Example usage
clear_screen()

# from subprocess import call
# call('color 2', shell=True)
# os.system('color 2')

import colorama
from colorama import Fore
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

print(f'''{colors.RED}
                    ███╗   ██╗ ██╗ ████████╗ ██████╗   ██████╗      ██████╗  ███████╗ ███╗   ██╗
                    ████╗  ██║ ██║ ╚══██╔══╝ ██╔══██╗ ██╔═══██╗    ██╔════╝  ██╔════╝ ████╗  ██║
                    ██╔██╗ ██║ ██║    ██║    ██████╔╝ ██║   ██║    ██║  ███╗ █████╗   ██╔██╗ ██║
                    ██║╚██╗██║ ██║    ██║    ██╔══██╗ ██║   ██║    ██║   ██║ ██╔══╝   ██║╚██╗██║
                    ██║ ╚████║ ██║    ██║    ██║  ██║ ╚██████╔╝    ╚██████╔╝ ███████╗ ██║ ╚████║
                    ╚═╝  ╚═══╝ ╚═╝    ╚═╝    ╚═╝  ╚═╝  ╚═════╝      ╚═════╝  ╚══════╝ ╚═╝  ╚═══╝
                                                                        
{colors.RED}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{colors.RESET}
''')

num = int(input('Input How Many Codes to Generate and Check: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, be patient if you entered the high number!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" [Valid] >       {nitro} ")
            break
        else:
            print(f" [Invalid] >       {nitro} ")


time.sleep(0.2)

input("\nAll codes have been generated, You will se valid codes in Valid Codes.txt")
input("\nIf Valid Codes.txt is not created, then better luck next time")
