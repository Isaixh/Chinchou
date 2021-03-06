import discord
import asyncio
from .utils.dataIO import dataIO
from string import ascii_letters
from .utils import checks
import os
import re
import aiohttp
import random
from discord.ext import commands
from random import uniform

class Metagirl:
    """Met a girl at..."""

    def __init__(self,bot):
        self.bot = bot
        self.header = {"User-Agent": "User_Agent"}

    async def message_triggered(self, message):
        message2 = message.content.lower()
        if 'met a girl at' in message2:
            await self.bot.send_message(message.channel, random.randint(0,100))


def setup(bot):
    print("setting up...")
    n = Metagirl(bot)
    bot.add_listener(n.message_triggered, "on_message")
    bot.add_cog(n)
