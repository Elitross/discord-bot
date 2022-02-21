import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')







@bot.command()
async def clear(ctx,amount=10):
    await ctx.channel.purge(limit=amount+1)

#commande savoir latence
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! 🏓 \nLatence: **{round(bot.latency * 1000)}ms**")

#pseudo log des messages
@bot.event
async def on_message(message):
    print('Message from {0.author}: {0.content}'.format(message))
    await bot.process_commands(message)

#setup debut loading status et comfirmation bot allume
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="!help"))
    print('We have logged in as {0.user}'.format(bot))

bot.run(TOKEN)
