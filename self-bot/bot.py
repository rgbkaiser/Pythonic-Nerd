# pip install discord.py-self
import discord
from discord.ext import commands
import json
import os
import colorama
from colorama import Fore
clear = lambda:os.system('cls')
clear()
colorama.init(autoreset=True)

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

print(f'{colors.RED}' + '''
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗██╗ ██████╗    ███╗   ██╗███████╗██████╗ ██████╗ 
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║██║██╔════╝    ████╗  ██║██╔════╝██╔══██╗██╔══██╗
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║██║██║         ██╔██╗ ██║█████╗  ██████╔╝██║  ██║
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║██║██║         ██║╚██╗██║██╔══╝  ██╔══██╗██║  ██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║██║╚██████╗    ██║ ╚████║███████╗██║  ██║██████╔╝
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝    ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═════╝  
''')

# ⚠️ Replace this with your Discord user token
TOKEN = 'MTI0MjM2NDQ0MzI3OTQ5MTExNg.GxDXOu.UwF83aH4z9aB0ZEe9vXtUAggjVv8ooA88wwjKw'

bot = commands.Bot(command_prefix='&', self_bot=True)
DATA_FILE = 'data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({}, f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Load data
data = load_data()
afk_mode = {"status": False, "reason": ""}

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if afk_mode["status"] and message.author != bot.user and bot.user.mentioned_in(message):
        await message.channel.send(f"I'm AFK: {afk_mode['reason']}")
    await bot.process_commands(message)

# 💰 LTC address commands
@bot.command()
async def saveltc(ctx, *, address):
    data['ltc'] = address
    save_data(data)
    await ctx.send("✅ LTC address saved!")

@bot.command()
async def getltc(ctx):
    ltc = data.get('ltc', '❌ No LTC address saved.')
    await ctx.send(f"**LTC Address:** ```{ltc}```")

# 🏦 UPI commands
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

# 📝 Custom message commands
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

# 💤 AFK system
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

# 🧹 Purge messages
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

# ✅ Run the bot (no 'bot=False' needed in latest versions)
bot.run(TOKEN)
