import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')





#---------- Commandes ---------#

#embed liste des commandes
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Command list',
        description = "Liste des commandes du bot et leur description",
        colour = discord.Colour.dark_purple()

    )
    embed.set_author(name = "objectsConnecteBot#4796")
    embed.set_footer(text = "Fait par Charles Rioux en .py")  
    embed.add_field(name = "!purge x", value = "Supprime X nombre de messages ou x es la quantitee, tu peux rien mettre pour en supprimmer 10\n", inline=False) 
    embed.add_field(name = "!ping", value = "donne la latence", inline=False)

    await ctx.send(embed=embed)

#clear X+1 messages
@bot.command()
async def clear(ctx,amount=10):
    await ctx.channel.purge(limit=amount+1)

#commande savoir latence
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! 🏓 \nLatence: **{round(bot.latency * 1000)}ms**")


#---------- Console shits ----------#

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
