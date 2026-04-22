import os
import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online come {bot.user}")

@bot.command()
async def countdown(ctx):
    for i in range(3, 0, -1):
        await ctx.send(str(i))
        await asyncio.sleep(1)
    await ctx.send("GO! 🚀")

token = os.environ.get("DISCORD_BOT_TOKEN")
bot.run(token)
