from discord.ext import commands

class Classes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.previous_messages = []
