import discord
from discord.ext import commands
import math

class calculator_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="takes 2 number and add them Format: .add x+y", pass_context = True)
    async def add(self, ctx, message: str):
        try:
            x, y = map(int, message.split('+'))
        except Exception:
            await ctx.send('Format has to be in N+N!')
            return
        x, y = map(int, message.split('+'))
        result = x + y
        await ctx.send(message + ' = ' + str(result))

    @commands.command(help="takes 2 number and subtract them Format: .substract x-y", pass_context = True)
    async def subtract(self, ctx, message: str):
        try:
            x, y = map(int, message.split('-'))
        except Exception:
            await ctx.send('Format has to be in N-N!')
            return
        x,y = map(int, message.split('-'))
        result = x - y
        await ctx.send(message + ' = ' + str(result))

    @commands.command(help="takes 2 number and multiply them Format: .multi x*y", pass_context= True)
    async def multi(self, ctx, message: str):
        try:
            x, y = map(int, message.split('*'))
        except Exception:
            await ctx.send('Format has to be in N*N!')
            return
        x,y = map(int, message.split('*'))
        result = x * y
        await ctx.send(message + ' = ' + str(result))
    
    @commands.command(help="takes 2 number and divide them Format: .div x/y", pass_context = True)
    async def div(self, ctx, message: str):
        try:
            x, y = map(int, message.split('/'))
        except Exception:
            await ctx.send('Format has to be in N/N!')
            return
        x,y = map(int, message.split('/'))
        result = x / y
        await ctx.send(message + ' = ' + str(result))
    
    @commands.command(help="takes 2 number and find the first number's power of second number Format: .pow x**y", pass_context = True)
    async def pow(self, ctx, message: str):
        try:
            x, y = map(int, message.split('**'))
        except Exception:
            await ctx.send('Format has to be in N**N!')
            return
        x,y = map(int, message.split('**'))
        result = math.pow(x,y)
        await ctx.send(message + ' = ' + str(result))
    
    @commands.command(help="takes a number and find the sqrt of that number Format. .sqrt x", pass_context = True)
    async def sqrt(self, ctx, message: str):
        try:
            x = math.sqrt(int(message))
        except Exception:
            await ctx.send('Invalid value entered!')
            return
        result = math.sqrt(int(message))
        await ctx.send("Square Root of " + message + ' = ' + str(result))