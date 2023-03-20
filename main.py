import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

# Загружаем все коги из директории "cogs"
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run("TOKEN")