import datetime
from discord.ext import tasks
from core.classes import Classes
from core import constant

class Task(Classes):
    utc_8 = datetime.timezone(datetime.timedelta(hours=8))
    today = datetime.datetime.now(tz=utc_8)
    calcium_time = datetime.time(hour=23, minute=0, tzinfo=utc_8)
    birth_control_time = datetime.time(hour=23, minute=30, tzinfo=utc_8)

    def __init__(self, bot):
        super().__init__(bot)
        self.eat_calcium.start()
        self.eat_birth_control_pill.start()

    @tasks.loop(time=calcium_time)
    async def eat_calcium(self):
        user = await self.bot.fetch_user(constant.DISCORD_BOT['SANNY'])
        await user.send('該吃鈣ㄌ')
        print('該吃鈣ㄌ')

    @tasks.loop(time=birth_control_time)
    async def eat_birth_control_pill(self):
        user = await self.bot.fetch_user(constant.DISCORD_BOT['SANNY'])
        await user.send('該吃避孕藥ㄌ')
        print('該吃避孕藥ㄌ')

async def setup(bot):
    await bot.add_cog(Task(bot))
    print('Add cog task')
