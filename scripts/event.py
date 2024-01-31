from discord.ext import commands
from core import Classes

class Event(Classes):
    @commands.Cog.listener()
    async def on_message(self, data):
        # print(data)
        pass

async def setup(bot):
    await bot.add_cog(Event(bot))
    print('Add cog event')
