# IMPORTS #
import discord
from discord.ext import commands
import os
import dotenv
import json

with open("info.json", 'r') as f:
    leaders = json.load(f)["leaders"]

dotenv.load_dotenv()
token, inv, koda = os.environ.get('TOKEN'), os.environ.get('INVITE'), os.environ.get("KODA")
bot = commands.Bot(command_prefix=">", description="Ricardo Bot")
# List of cogs
cogs = []

bot.remove_command('help')


@bot.command()
async def load(ctx, cog):
    await ctx.message.delete()
    if ctx.author.id in leaders:
        try:
            bot.load_extension(f"cogs.{cog}")
            await ctx.send(f"Loaded '{cog}' successfully!", delete_after=3)
        except Exception as er:
            await ctx.send(f"{cog} cannot be loaded. [{er}]", delete_after=3)
    else:
        raise commands.CommandNotFound('error')


@bot.command()
async def unload(ctx, cog):
    await ctx.message.delete()
    if ctx.author.id in leaders:
        try:
            bot.unload_extension(f"cogs.{cog}")
            await ctx.send(f"Unloaded '{cog}' successfully!", delete_after=3)
        except Exception as er:
            await ctx.send(f"{cog} cannot be unloaded. [{er}]", delete_after=3)
    else:
        raise commands.CommandNotFound("error")


@bot.command()
async def invite(ctx):
    if ctx.author.id in leaders:
        await ctx.message.delete()
        await ctx.author.send(inv)
    else:
        await ctx.send("You do not have permission to use this command.")

# immediately stop the bot
@bot.command(aliases=['restart'])
async def stop(ctx):
    await bot.logout()


# Loads the list of cogs
if __name__ == "__main__":
    for cog in cogs:
        try:
            bot.load_extension(f"cogs.{cog}")
            print(f"Loaded '{cog}' successfully!")
        except Exception as er:
            print(f"{cog} cannot be loaded. [{er}]")


# Runs this before the bot starts
@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(activity=discord.Game(name="| >help | Made by Koda#8495"))
    print('------')


# Starts the bot
bot.run(token, reconnect=True)
