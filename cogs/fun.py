import discord
from discord.ext import commands
from random import randint

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def gay(self, ctx, user: discord.Member=None):
        e = discord.Embed(color=0x880000)
        if user == None:
            user = ctx.author
        if user.id == 641016825693601812:
            v = 100
        else:
            v = randint(0, 100)
        e.add_field(name="How gay are you?", value=f"You are {v}% gay, {user.mention}")
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Fun(bot))