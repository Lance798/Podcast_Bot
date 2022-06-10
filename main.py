import discord
from discord.ext import commands
import json
import os

with open("settings.json", 'r', encoding='utf8') as f:
    data = json.load(f)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='$', intents=intents)


# for filename in os.listdir("./src/Commands"):
#     if filename.endswith('.py'):
#         bot.load_extension(f"src.Commands.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f'{bot.user}已上線')

@bot.command
async def test(ctx):
    await ctx.send("HI")

bot.run(data['TOKEN'])
