import requests
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
  ████████╗  ██████╗  ██╗  ██╗ ███████╗ ███╗   ██╗     ██████╗ ██╗  ██╗ ███████╗  ██████╗ ██╗  ██╗ ███████╗ ██████╗ 
  ╚══██╔══╝ ██╔═══██╗ ██║ ██╔╝ ██╔════╝ ████╗  ██║    ██╔════╝ ██║  ██║ ██╔════╝ ██╔════╝ ██║ ██╔╝ ██╔════╝ ██╔══██╗
     ██║    ██║   ██║ █████╔╝  █████╗   ██╔██╗ ██║    ██║      ███████║ █████╗   ██║      █████╔╝  █████╗   ██████╔╝
     ██║    ██║   ██║ ██╔═██╗  ██╔══╝   ██║╚██╗██║    ██║      ██╔══██║ ██╔══╝   ██║      ██╔═██╗  ██╔══╝   ██╔══██╗
     ██║    ╚██████╔╝ ██║  ██╗ ███████╗ ██║ ╚████║    ╚██████╗ ██║  ██║ ███████╗ ╚██████╗ ██║  ██╗ ███████╗ ██║  ██║
     ╚═╝     ╚═════╝  ╚═╝  ╚═╝ ╚══════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝ ╚══════╝  ╚═════╝ ╚═╝  ╚═╝ ╚══════╝ ╚═╝  ╚═╝
                                                                                                            
{colors.RED}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{colors.RESET}
''')

def check_discord_token(token):
    """
    Checks if a given Discord token is valid.
    Args:
        token (str): Discord token to check.
    Returns:
        str: Result indicating the token's status.
    """
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get("https://discord.com/api/v9/users/@me", headers=headers, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error checking token {token[:10]}...: {e}")
        return "unknown"

    if response.status_code == 200:
        return "valid"
    elif response.status_code == 401:
        return "invalid"
    elif response.status_code == 403:
        return "banned"
    else:
        return "unknown"

def main():
    try:
        with open("resource/TokenChecker/tokens.txt", "r") as file:
            tokens = [line.strip() for line in file if line.strip()]

        if not tokens:
            print("❌ 'tokens.txt' is empty. Add tokens to it first.")
            return

        valid_tokens = []
        invalid_tokens = []

        for idx, token in enumerate(tokens, start=1):
            result = check_discord_token(token)

            if result == "valid":
                valid_tokens.append(token)
                print(f"[{idx}] ✅ VALID: {token[:10]}...")
            elif result in ["invalid", "banned"]:
                invalid_tokens.append(token)
                if result == "invalid":
                    print(f"[{idx}] ❌ INVALID: {token[:10]}...")
                else:
                    print(f"[{idx}] 🚫 BANNED/FORBIDDEN: {token[:10]}...")
            else:
                print(f"[{idx}] ⚠️ UNKNOWN STATUS ({token[:10]}...)")

        if valid_tokens:
            with open("resource/TokenChecker/valid_tokens.txt", "w") as vf:
                for token in valid_tokens:
                    vf.write(token + "\n")
            print(f"\n✅ Saved {len(valid_tokens)} valid tokens to 'valid_tokens.txt'.")
        else:
            print("\n❌ No valid tokens found.")

        if invalid_tokens:
            with open("resource/TokenChecker/invalid_tokens.txt", "w") as inf:
                for token in invalid_tokens:
                    inf.write(token + "\n")
            print(f"❌ Saved {len(invalid_tokens)} invalid/banned tokens to 'invalid_tokens.txt'.")
        else:
            print("✅ No invalid/banned tokens found.")

    except FileNotFoundError:
        print("❌ 'tokens.txt' not found. Please create a file named 'tokens.txt' with one token per line.")

if __name__ == "__main__":
    main()

