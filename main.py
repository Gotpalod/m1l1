import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def Minecraft(ctx):
    await ctx.send(f'Майнкрафт это мая жизнь МАЙНКРАФФФФФФФФФТ')

@bot.command()
async def pon(ctx, count_heh = 5):
    await ctx.send("ПОН" * count_heh)

bot.run("MTE1OTg3NzgzNjcxOTUzODIyNg.GBOUUX.ojW5CJzRLpUyw-2phaL8ymS8dLIEmT2ecQSCJs")

