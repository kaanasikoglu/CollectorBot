import discord
from discord.ext import commands
import requests
import json
import random
import os

class fun_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

	
    @commands.command(help="displays a random Chuck Norris fact")
    async def chucknorris(self, ctx):
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url)
        value = response.json()['value']
        await ctx.channel.send(value)

    @commands.command(help="displays current value of bitcoin")
    async def bitcoin(self, ctx):
	    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
	    response = requests.get(url)
	    value = response.json()['bpi']['USD']['rate']
	    await ctx.channel.send("Current Bitcoin price is : $" + value)
    
    @commands.command(help="rolls a dice between the range user decide")
    async def roll(self, ctx, dice: str):
        try:
            rolls, limit = map(int, dice.split('-'))
        except Exception:
            await ctx.send('Format has to be in N-N!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)
    
