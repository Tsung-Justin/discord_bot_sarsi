from discord.ext import commands
from core.classes import Classes

class command(Classes):
    def __init__(self, bot):
        super().__init__(bot)

    @commands.command()
    async def test(self, ctx):
        await ctx.message.delete()
        await ctx.send('test')

    @commands.command()
    async def ping (self, ctx):
        await ctx.message.delete()
        await ctx.send (f"{round( self.bot.latency*1000)} ms")

    @commands.command()
    async def get_user(self, user_id):
        user = await self.bot.fetch_user(user_id)
        print(user)

    @commands.command()
    async def fetch_user(self, ctx, user_id):
        user = await self.bot.fetch_user(user_id)
        print(user)

    @commands.command()
    async def get_channel(self, ctx, channel_id: int):
        channel = self.bot.get_channel(channel_id)
        print(channel)

    @commands.command()
    async def fetch_channel(self, ctx, channel_id: int):
        channel = await self.bot.fetch_channel(channel_id)
        print(channel)

async def setup(bot):
    await bot.add_cog(command(bot))
    print('Add cog command')
