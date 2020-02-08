import discord
from discord.utils import get
import os
import psycopg2

conn = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode='require')
c = conn.cursor()


class Conf:
    def __init__(self, conf):
        self.conf = conf[0]
        print(self.conf)
        self.id = self.conf[0]
        self.welcomechannel = self.conf[1]
        self.welcomemessage = self.conf[2]

    def check(self, a):
        if a == 1234 or a == "abc":
            a = "None"
        return a

    def embed(self, ctx, bot):
        em = discord.Embed(title="Config", color=0x880000)
        em.add_field(name="Guild Name/ID", value=f"{get(bot.guilds, id=self.id).name} / {self.id}", inline=False)
        em.add_field(name="welcomechannel", value=self.check(self.welcomechannel), inline=False)
        em.add_field(name="welcomemessage", value=self.check(self.welcomemessage), inline=False)
        return em

    def __str__(self):
        return self.conf
