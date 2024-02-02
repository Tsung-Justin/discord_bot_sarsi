from discord.ext import commands
from core import Classes
from core import chatgpt_response

class Event(Classes):
    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)
        if message.author == self.bot.user:
            return

        command, user_message = None, None

        for text in ['.ai', '.bot', '.chatgpt']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text + ' ', '')

        if command == '.ai' or command == '.bot' or command == '.chatgpt':
            bot_response = chatgpt_response(content=user_message)
            await message.channel.send(f'{bot_response}')

async def setup(bot):
    await bot.add_cog(Event(bot))
    print('Add cog event')
