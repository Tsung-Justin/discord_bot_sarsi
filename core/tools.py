import asyncio
from core import Classes

class Tools(Classes):
    def __init__(self, bot):
        super().__init__(bot)
        self.chatgpt_init()

    def chatgpt_init(self):
        self.previous_messages.append(
            {
                'role': 'system',
                'content': '我的名字是小可樂，是一隻小太陽鸚鵡，使用繁體中文'
            }
        )

    async def bot_typing(self, ctx, time:int):
        async with ctx.typing():
            await asyncio.sleep(time)
