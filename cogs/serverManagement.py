from discord.ext import commands

class serverManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def acommand(self, ctx):
       await ctx.send("Stuff")        

def setup(bot):
    bot.add_cog(serverManagement(bot))