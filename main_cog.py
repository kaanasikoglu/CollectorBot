import discord
from discord.ext import commands
class main_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
General commands:
.help - displays all the available commands
.clear amount - will delete the past messages with the amount specified

Music commands:
.play <keywords> - finds the song on youtube and plays it in your current channel
.queue - displays the current music queue
.skip - skips the current song being played

Fun commands:
.chucknorris - displays a random Chuck Norris fact
.bitcoin - displays current value of bitcoin
.roll - rolls a dice between the range user decide

Collector bot commands:
.register - Registers user to database
.balance - Sends DM to user with user's balance
.add_balance - Adds the amount that written to tagged user's balance (Works if used by Majors)
.remove_balance - Removes the amount that written to tagged user's balance (Works if used by Majors)
.send_all_acc_info - Send all the information in the database via DM (Works if used by Majors)

Calculator commands:
.add - takes 2 number and add them Format: ".add x+y"
.subtract - takes 2 number and subtract them Format: ".substract x-y"
.multi - takes 2 number and multiply them Format: ".multi x*y"
.div - takes 2 number and divide them Format: ".div x/y"
.pow - takes 2 number and find the first number's power of second number Format: ".pow x**y"
.sqrt - takes a number and find the sqrt of that number Format. ".sqrt x"
```
"""
        self.text_channel_list = []

    #some debug info so that we know the bot has started    
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

        await self.send_to_all(self.help_message)        

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            #sending message when it became online
            #await text_channel.send("Collector Bot Online!")
            pass

    @commands.command(name="clear", help="Clears a specified amount of messages")
    async def clear(self, ctx, arg):
        #extract the amount to clear
        amount = 5
        try:
            amount = int(arg)
        except Exception: pass

        await ctx.channel.purge(limit=amount)
