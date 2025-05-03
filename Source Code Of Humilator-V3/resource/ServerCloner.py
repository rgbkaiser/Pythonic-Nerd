"""
Discord Server Cloner Bot (Interactive Input Version)
Prompts user to enter bot token, source guild ID, and destination guild ID.
Clones categories, channels, and roles from one Discord server to another.
"""

import discord
from discord.ext import commands
import asyncio
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
   ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗      ██████╗██╗      ██████╗  █████╗ ███╗   ██╗███████╗██████╗ 
   ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗    ██╔════╝██║     ██╔═══██╗██╔══██╗████╗  ██║██╔════╝██╔══██╗
   ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝    ██║     ██║     ██║   ██║███████║██╔██╗ ██║█████╗  ██████╔╝
   ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██║     ██║     ██║   ██║██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗
   ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║    ╚██████╗███████╗╚██████╔╝██║  ██║██║ ╚████║███████╗██║  ██║
   ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝     ╚═════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                                                    
{colors.RED}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{colors.RESET}
''')

# Prompt user for essential info
TOKEN = input("Enter your bot token: ").strip()
SOURCE_GUILD_ID = int(input("Enter the SOURCE guild ID: ").strip())
DESTINATION_GUILD_ID = int(input("Enter the DESTINATION guild ID: ").strip())

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    source_guild = bot.get_guild(SOURCE_GUILD_ID)
    destination_guild = bot.get_guild(DESTINATION_GUILD_ID)

    if not source_guild or not destination_guild:
        print("Could not find one or both guilds. Check the IDs and ensure the bot is in both servers.")
        return

    print("Cloning roles...")
    await clone_roles(source_guild, destination_guild)
    print("Cloning categories and channels...")
    await clone_channels(source_guild, destination_guild)

    print("Server cloning complete.")
    await bot.close()

async def clone_roles(source, dest):
    role_map = {}
    for role in source.roles[::-1]:
        if role.name == "@everyone":
            continue
        new_role = await dest.create_role(
            name=role.name,
            permissions=role.permissions,
            colour=role.colour,
            hoist=role.hoist,
            mentionable=role.mentionable
        )
        role_map[role.id] = new_role
        await asyncio.sleep(1)
    return role_map

async def clone_channels(source, dest):
    category_map = {}
    for category in source.categories:
        new_category = await dest.create_category(name=category.name)
        category_map[category.id] = new_category
        await asyncio.sleep(1)

    for channel in source.channels:
        if isinstance(channel, discord.TextChannel):
            cat = category_map.get(channel.category_id)
            await dest.create_text_channel(name=channel.name, category=cat, topic=channel.topic)
        elif isinstance(channel, discord.VoiceChannel):
            cat = category_map.get(channel.category_id)
            await dest.create_voice_channel(name=channel.name, category=cat)
        await asyncio.sleep(1)

bot.run(TOKEN)
