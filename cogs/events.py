import discord
from discord.ext import commands
from discord.utils import get
from conf import Conf
from random import choice
import os.path
import sys
import psycopg2
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

conn = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode='require')
c = conn.cursor()


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != 674372235166744613:
            if "i love you" in message.content.lower():
                await message.channel.send("I love you too.")

    @commands.Cog.listener()
    async def on_member_join(self, ctx):
        c.execute(f"SELECT * FROM conf WHERE id = {ctx.guild.id}")
        conf = Conf(c.fetchall())
        ch = get(ctx.guild.channels, id=conf.welcomechannel)
        await ch.send(conf.welcomemessage)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        channel = choice(guild.text_channels)
        await channel.send("Thank you for inviting me to your server! I will server you well.\nMy prefix is `>`.")
        c.execute("SELECT id FROM conf")
        e = c.fetchall()
        l = []
        for row in e:
            l.append(row[0])
        if not guild.id in l:
            c.execute(f"INSERT INTO conf VALUES({guild.id}, 1234, 'abc', 1234)")
        conn.commit()


def setup(bot):
    bot.add_cog(Events(bot))
