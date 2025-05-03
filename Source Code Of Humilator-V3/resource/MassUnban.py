import discord
import asyncio
from discord.ext import commands
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
               ███╗   ███╗  █████╗  ███████╗ ███████╗    ██╗   ██╗ ███╗   ██╗ ██████╗   █████╗  ███╗   ██╗
               ████╗ ████║ ██╔══██╗ ██╔════╝ ██╔════╝    ██║   ██║ ████╗  ██║ ██╔══██╗ ██╔══██╗ ████╗  ██║
               ██╔████╔██║ ███████║ ███████╗ ███████╗    ██║   ██║ ██╔██╗ ██║ ██████╔╝ ███████║ ██╔██╗ ██║
               ██║╚██╔╝██║ ██╔══██║ ╚════██║ ╚════██║    ██║   ██║ ██║╚██╗██║ ██╔══██╗ ██╔══██║ ██║╚██╗██║
               ██║ ╚═╝ ██║ ██║  ██║ ███████║ ███████║    ╚██████╔╝ ██║ ╚████║ ██████╔╝ ██║  ██║ ██║ ╚████║
               ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚══════╝ ╚══════╝     ╚═════╝  ╚═╝  ╚═══╝ ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═══╝
                                                                                     
{colors.RED}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{colors.RESET}
''')

# --------- Configuration & Input ---------
TOKEN = input(f"Enter Your Bot Discord Token: ").strip()
GUILD_ID = int(input("Server ID Of The Targetted Server: "))

# --------- Bot Setup ---------
intents = discord.Intents.default()
intents.guilds = True
intents.bans = True
bot = commands.Bot(command_prefix='&', intents=intents)

# --------- Mass Unban Function ---------
async def mass_unban(guild):
    try:
        bans = []
        async for ban_entry in guild.bans():
            bans.append(ban_entry)

        if not bans:
            print(f"No banned users found in {guild.name}.")
            return

        print(f"Attempting to unban {len(bans)} users in {guild.name}...")

        success = 0
        fail = 0

        for ban_entry in bans:
            user = ban_entry.user
            try:
                await guild.unban(user)
                success += 1
                print(f"✅ Unbanned {user.name}#{user.discriminator}")
            except Exception as e:
                fail += 1
                print(f"❌ Failed to unban {user}: {e}")

        print(f"Mass unban complete! ✅ Success: {success} ❌ Failed: {fail}")

    except Exception as e:
        print(f"Error fetching bans: {e}")

# --------- Events ---------
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

    guild = bot.get_guild(GUILD_ID)
    if guild is None:
        print("Guild not found. Make sure the bot is in the server and the ID is correct.")
    else:
        await mass_unban(guild)

# --------- Run the Bot ---------
bot.run(TOKEN)
