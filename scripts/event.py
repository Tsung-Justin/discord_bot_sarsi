from discord.ext import commands
from core import Classes, chatgpt_response, Tools

class Event(Classes):
    def __init__(self, bot):
        super().__init__(bot)
        self.tools = Tools(bot)

    @commands.Cog.listener()
    async def on_message(self, message):
        chatgpt_command = [',ai', '.bot', '.chatgpt']

        if message.author.bot and message.author != self.bot.user:
            return

        print(f'Author：{message.author}, Content：{message.content}')

        for chatgpt in chatgpt_command:
            if message.content.startswith(chatgpt):
                command, user_message = None, None

                for text in chatgpt_command:
                    if message.content.startswith(text):
                        command = message.content.split(' ')[0]
                        user_message = message.content.replace(text + ' ', '')

                if command == ',ai' or command == '.bot' or command == '.chatgpt':
                    self.previous_messages.append(
                        {
                            'role': 'user',
                            'content': user_message
                        }
                    )

                    bot_response = chatgpt_response(self.previous_messages)
                    self.previous_messages.append(
                        {
                            'role': 'assistant',
                            'content': bot_response
                        }
                    )

                    await self.tools.bot_typing(message.channel, 5)
                    await message.channel.send(f'{bot_response}')

async def setup(bot):
    await bot.add_cog(Event(bot))
    print('Add cog event')
