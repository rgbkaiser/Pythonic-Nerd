# pip install -U git+https://github.com/dolfies/discord.py-self.git

import discord
from discord.ext import commands
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
                        ███████╗ ███████╗ ██╗      ███████╗     ██████╗   ██████╗  ████████╗
                        ██╔════╝ ██╔════╝ ██║      ██╔════╝     ██╔══██╗ ██╔═══██╗ ╚══██╔══╝
                        ███████╗ █████╗   ██║      █████╗       ██████╔╝ ██║   ██║    ██║   
                        ╚════██║ ██╔══╝   ██║      ██╔══╝       ██╔══██╗ ██║   ██║    ██║   
                        ███████║ ███████╗ ███████╗ ██║          ██████╔╝ ╚██████╔╝    ██║   
                        ╚══════╝ ╚══════╝ ╚══════╝ ╚═╝          ╚═════╝   ╚═════╝     ╚═╝   
    
{colors.RED}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{colors.RESET}
''')

TOKEN = input("Enter your Discord user token: ").strip()

# ❌ REMOVE discord.Intents — it's not supported in discord.py-self
# ✅ Just define the bot with self_bot=True
bot = commands.Bot(command_prefix='&', self_bot=True)

DATA_FILE = 'resource/SelfBot/data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({}, f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

data = load_data()
afk_mode = {"status": False, "reason": ""}

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_message(message):
    if afk_mode["status"] and message.author != bot.user and bot.user.mentioned_in(message):
        await message.channel.send(f"I'm AFK: {afk_mode['reason']}")
    await bot.process_commands(message)

@bot.command()
async def saveltc(ctx, *, address):
    data['ltc'] = address
    save_data(data)
    await ctx.send("✅ LTC address saved!")

@bot.command()
async def getltc(ctx):
    ltc = data.get('ltc', '❌ No LTC address saved.')
    await ctx.send(f"**LTC Address:** ```{ltc}```")

@bot.command()
async def saveupi(ctx, label, *, upi_id):
    if 'upi' not in data:
        data['upi'] = {}
    data['upi'][label] = upi_id
    save_data(data)
    await ctx.send(f"✅ UPI ID/QR saved under `{label}`.")

@bot.command()
async def getupi(ctx, label):
    upi = data.get('upi', {}).get(label)
    if upi:
        await ctx.send(f"UPI ({label}): ```{upi}```")
    else:
        await ctx.send(f"❌ No UPI found under `{label}`.")

@bot.command()
async def savemsg(ctx, name, *, message):
    if 'messages' not in data:
        data['messages'] = {}
    data['messages'][name] = message
    save_data(data)
    await ctx.send(f"✅ Message saved under `{name}`.")

@bot.command()
async def msg(ctx, name):
    message = data.get('messages', {}).get(name)
    if message:
        await ctx.send(message)
    else:
        await ctx.send(f"❌ No message found for `{name}`.")

@bot.command()
async def afk(ctx, *, reason="No reason given."):
    afk_mode["status"] = True
    afk_mode["reason"] = reason
    await ctx.send(f"🚫 You are now AFK: {reason}")

@bot.command()
async def back(ctx):
    afk_mode["status"] = False
    afk_mode["reason"] = ""
    await ctx.send("✅ Welcome back! AFK mode disabled.")

@bot.command()
async def purge(ctx, amount: int = 10):
    deleted = 0
    async for message in ctx.channel.history(limit=amount):
        if message.author == bot.user:
            try:
                await message.delete()
                deleted += 1
            except Exception as e:
                print(f"Failed to delete message: {e}")
    confirmation = await ctx.send(f"🧹 Deleted {deleted} message(s).")
    await confirmation.delete(delay=3)

bot.run(TOKEN)
