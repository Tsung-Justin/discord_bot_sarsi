import time, os, discord
from core import constant
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)
localtime = time.strftime(f'%Y-%m-%d-%A_%H-%M-%S')

@bot.event
async def on_ready():
    for filename in os.listdir('./scripts'):
        if filename.endswith('.py'):
            await bot.load_extension(f'scripts.{filename[:-3]}')

    print (f'現在時間：{localtime}\n{bot.user.name} 已上線！\n')

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'scripts.{extension}')
    await ctx.send(f'{extension} script is loaded.')

@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'scripts.{extension}')
    await ctx.send(f'{extension} script is reloaded.')

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f'scripts.{extension}')
    await ctx.send(f'{extension} script is unloaded.')

if __name__ == '__main__':
    bot.run(constant.DISCORD_BOT['TOKEN'])
