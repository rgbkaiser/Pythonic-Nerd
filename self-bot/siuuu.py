import asyncio
from discord.ext import commands
import discord

token = input("Enter token: ").strip()

bot = commands.Bot(command_prefix="!", self_bot=True, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user} (ID: {bot.user.id})")

bot.run(token)
