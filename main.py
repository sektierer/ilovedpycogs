import os
import discord
import asyncio
from discord.ext import commands
from config import data

bot = commands.Bot(command_prefix=data['prefix'], intents = discord.Intents.all())

# Загружаем все коги из директории "cogs"
@bot.event
async def on_ready():
    await cogsLoad()
    print(f'{bot.user} online!')

async def cogsFind():
    list = []
    for filename in os.listdir("./cogs"):
        if filename == '__init__.py': continue
        if filename.endswith(".py"):
            list.append(filename)
    return list

async def cogsLoad():
    l = []
    for x in await cogsFind():
        await bot.load_extension(f"cogs.{x[:-3]}")
        l.append(x)
    return l

async def cogsUnload():
    for x in await cogsFind():
        await bot.unload_extension(f"cogs.{x[:-3]}")

@bot.command()
async def reload(ctx):
    await cogsUnload()
    cogs = await cogsLoad()
    await ctx.send(f'{len(cogs)} было перезагружено. Включая:\n' + '\n'.join(cogs))

    

bot.run(data['token'])
