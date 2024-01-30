import datetime
from discord.ext import commands, tasks
from core.classes import Classes

utc = datetime.timezone.utc
specify_time = datetime.time(hour=14, minute=3, tzinfo=utc)

class Event(Classes):
    @commands.Cog.listener()
    async def on_message(self, data):
        print(data)

    @tasks.loop(time=specify_time)
    async def my_task(self):
        print('My task is running!')

async def setup(bot):
    print('Add cog event')
    await bot.add_cog(Event(bot))
