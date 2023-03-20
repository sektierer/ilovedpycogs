from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycommand(self, ctx):
        await ctx.send("пошел нгаухуй")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Задержка бота: {round(self.bot.latency)}ms')
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if message.content == "ping":
            await message.channel.send("pong")

async def setup(bot):
    await bot.add_cog(MyCog(bot))