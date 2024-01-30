import datetime
from discord.ext import commands, tasks
from core.classes import Classes


class Event(Classes):
    @commands.Cog.listener()
    async def on_message(self, data):
        print(data)

async def setup(bot):
    print('Add cog event')
    await bot.add_cog(Event(bot))
