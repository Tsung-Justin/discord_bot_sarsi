from discord.ext import commands
from core import Classes, Tools

class command(Classes):
    def __init__(self, bot):
        super().__init__(bot)
        self.tools = Tools(bot)

    @commands.command()
    async def test(self, ctx):
        await self.tools.bot_typing(ctx, 1)
        # await ctx.message.delete()
        await ctx.send('test')

    @commands.command()
    async def ping (self, ctx):
        await ctx.message.delete()
        await self.tools.bot_typing(ctx, 1)
        await ctx.send (f"{round(self.bot.latency*1000)} ms")

async def setup(bot):
    await bot.add_cog(command(bot))
    print('Add cog command')
