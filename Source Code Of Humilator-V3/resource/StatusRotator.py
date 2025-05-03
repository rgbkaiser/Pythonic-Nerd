# ⚠️ Selfbot use is against Discord ToS. Use at your own risk.

import discord
from discord.ext import commands, tasks
import itertools
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
  ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗    ██████╗  ██████╗ ████████╗ █████╗ ████████╗ ██████╗ ██████╗ 
  ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
  ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗    ██████╔╝██║   ██║   ██║   ███████║   ██║   ██║   ██║██████╔╝
  ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║    ██╔══██╗██║   ██║   ██║   ██╔══██║   ██║   ██║   ██║██╔══██╗
  ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║    ██║  ██║╚██████╔╝   ██║   ██║  ██║   ██║   ╚██████╔╝██║  ██║
  ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                     
{colors.RED}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{colors.RESET}
''')

TOKEN = input("Enter your Discord token (use at your own risk): ").strip()

bot = commands.Bot(command_prefix='&', self_bot=True)

# Define custom statuses
statuses = itertools.cycle([
    discord.Activity(type=discord.ActivityType.watching, name="the stars ✨"),
    discord.Activity(type=discord.ActivityType.listening, name="lofi beats 🎧"),
    discord.Game("Minecraft Steve 😎"),
    discord.Streaming(name="Code Live 💻", url="https://twitch.tv/your_channel"),
    discord.Activity(type=discord.ActivityType.playing, name="with Python 🐍")
])

rotator_running = False

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@tasks.loop(seconds=20)
async def change_status():
    activity = next(statuses)
    await bot.change_presence(activity=activity)

# Command to start status rotation
@bot.command()
async def start(ctx):
    global rotator_running
    if not change_status.is_running():
        change_status.start()
        rotator_running = True
        await ctx.send("✅ Status rotation started.")
    else:
        await ctx.send("⚠️ Status rotation is already running.")

# Command to stop status rotation
@bot.command()
async def stop(ctx):
    global rotator_running
    if change_status.is_running():
        change_status.stop()
        rotator_running = False
        await ctx.send("🛑 Status rotation stopped.")
    else:
        await ctx.send("⚠️ Status rotation is not running.")

# Command to check if rotator is running
@bot.command()
async def status(ctx):
    if rotator_running:
        await ctx.send("🔄 Status rotator is currently running.")
    else:
        await ctx.send("⏸️ Status rotator is not running.")

bot.run(TOKEN)
