"""
Mass Targeted DM Spammer Bot (Multi-Token Version)
"""

import asyncio
import aiohttp
import json
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
             ██████╗  ███╗   ███╗     ███████╗ ██████╗   █████╗  ███╗   ███╗ ███╗   ███╗ ███████╗ ██████╗ 
             ██╔══██╗ ████╗ ████║     ██╔════╝ ██╔══██╗ ██╔══██╗ ████╗ ████║ ████╗ ████║ ██╔════╝ ██╔══██╗
             ██║  ██║ ██╔████╔██║     ███████╗ ██████╔╝ ███████║ ██╔████╔██║ ██╔████╔██║ █████╗   ██████╔╝
             ██║  ██║ ██║╚██╔╝██║     ╚════██║ ██╔═══╝  ██╔══██║ ██║╚██╔╝██║ ██║╚██╔╝██║ ██╔══╝   ██╔══██╗
             ██████╔╝ ██║ ╚═╝ ██║     ███████║ ██║      ██║  ██║ ██║ ╚═╝ ██║ ██║ ╚═╝ ██║ ███████╗ ██║  ██║
             ╚═════╝  ╚═╝     ╚═╝     ╚══════╝ ╚═╝      ╚═╝  ╚═╝ ╚═╝     ╚═╝ ╚═╝     ╚═╝ ╚══════╝ ╚═╝  ╚═╝
    
{colors.RED}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{colors.RESET}
''')

MESSAGE = "Hulla You Got Trolled...!!!"
TOKENS_FILE = 'resource/dmSpammer/spam-tokens.txt'
SPAM_COUNT = 50

async def send_dm(session, token, user_id, message):
    url = f"https://discord.com/api/v9/users/@me/channels"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    payload = {
        "recipient_id": user_id
    }

    try:
        # Create DM Channel
        async with session.post(url, headers=headers, json=payload) as resp:
            if resp.status == 200:
                data = await resp.json()
                channel_id = data["id"]
                print(f"[+] Created DM channel with {user_id}.")

                # Spam 50 messages
                message_url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
                for _ in range(SPAM_COUNT):
                    message_payload = {
                        "content": message
                    }
                    async with session.post(message_url, headers=headers, json=message_payload) as msg_resp:
                        if msg_resp.status == 200:
                            print(f"[+] Sent spam message to {user_id}.")
                        else:
                            print(f"[-] Failed to send spam message. Status: {msg_resp.status}")
                    await asyncio.sleep(0.5)  # Slight delay to avoid instant ban
            else:
                print(f"[-] Failed to create DM channel. Status: {resp.status}")

    except Exception as e:
        print(f"[-] Error sending DM: {e}")

async def start_spam(token, user_id):
    async with aiohttp.ClientSession() as session:
        await send_dm(session, token, user_id, MESSAGE)

async def main():
    user_id = input("Enter the User ID to spam: ").strip()

    tokens = []
    with open(TOKENS_FILE, 'r') as f:
        tokens = [line.strip() for line in f.readlines() if line.strip()]

    spam_tasks = []
    for token in tokens:
        spam_tasks.append(start_spam(token, user_id))

    await asyncio.gather(*spam_tasks)

if __name__ == "__main__":
    asyncio.run(main())
