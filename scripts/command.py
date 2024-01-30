from discord.ext import commands
from core.classes import Classes

class command(Classes):
    @commands.command()
    async def test(self, ctx):
        await ctx.message.delete()
        await ctx.send('test')

    @commands.command()
    async def ping (self, ctx):
        await ctx.message.delete()
        await ctx.send (f"{round( self.bot.latency*1000)} ms")

async def setup(bot):
    print('Add cog command')
    await bot.add_cog(command(bot))
