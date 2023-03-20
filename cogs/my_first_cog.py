from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycommand(self, ctx):
        await ctx.send("This is my command!")

def setup(bot):
    bot.add_cog(MyCog(bot))
