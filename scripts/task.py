import datetime
from discord.ext import commands, tasks

utc = datetime.timezone.utc
specify_time = datetime.time(hour=8, minute=9, tzinfo=utc)

class Task(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()

    @tasks.loop(time=specify_time)
    async def my_task(self):
        print('My task is running!')


async def setup(bot):
    print('Add cog task')
    await bot.add_cog(Task(bot))
