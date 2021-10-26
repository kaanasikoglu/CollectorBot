import discord
from discord.ext import commands
import sqlite3

class collector_cog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.db = sqlite3.connect('collectorbot.db')
        self.create_table()
        cur = self.db.cursor()
        self.check = 0
        self.balancecheck = 0
        
    #Creating a table
    def create_table(self):
        cur = self.db.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id integer PRIMARY KEY AUTOINCREMENT,
            userid text  NOT NULL,
            username text NOT NULL,
            user_balance integer NOT NULL
        )
        ''')
        self.db.commit()

    #Register the user who use the command .register if s/he not registered before if so gives error 
    @commands.command(help="Registers user to database")
    async def register(self, ctx):
        cur = self.db.cursor()

        for row in cur.execute('SELECT * FROM accounts'):
            if int(row[1]) == int(ctx.author.id):
                await ctx.send(ctx.message.author.mention + " You are already registered!")
                self.check = 1    
        if (self.check == 0):
            cur.execute('''
                    INSERT INTO accounts (userid, username, user_balance)
                    VALUES(?,?,?)
                    ''',[ctx.author.id,ctx.author.name,0])
            self.db.commit()
                    
            await ctx.send(ctx.message.author.mention + "You have been successfully registered!")
    
    #Show User's balance
    @commands.command(help="Sends DM to user with user's balance", pass_context = True)
    async def balance(self, ctx):
        cur = self.db.cursor()
        for row in cur.execute('SELECT * FROM accounts'):
            if int(row[1]) == int(ctx.author.id):
                #await ctx.send(ctx.message.author.mention + "Your balance: " + str(row[3]))
                await ctx.message.author.send("Your balance: " + str(row[3]))
                self.balancecheck = 1
        if(self.balancecheck == 0):
            await ctx.send(ctx.message.author.mention + "You are not registered. Please register first")
    
    #Add balance to tagged user
    @commands.command(help="Adds the amount that written to tagged user's balance (Works if used by Majors)", pass_context = True)
    async def add_balance(self, ctx, message: str):
        permission = 0
        L = ctx.message.author.roles
        for i in range (len(L)):
            if(str(L[i])=='Major'):
                permission = 1
        try:
            sign, value = map(str, message.split('+'))
        except ValueError:
            await ctx.send('Format has to be +{amount}k')
            return
        
        try:
            sign, value = map(str, message.split('+'))
            points, temp = value.split("k")
        except ValueError:
            await ctx.send('Format has to be +{amount}k')
            return
        if (permission == 1):
            cur = self.db.cursor()
            for row in cur.execute('SELECT * FROM accounts'):
                if (int(row[1]) == int(ctx.message.mentions[0].id)):
                    sign, value = map(str, message.split('+'))
                    points, temp = value.split("k")
                    result = int(points) * 1000
                    cur.execute('''
                        UPDATE accounts SET user_balance = user_balance + (?) WHERE userid = (?)
                        ''',[result, row[1]])
                    self.db.commit()
                    await ctx.send(ctx.message.author.mention + "Balance successfully added to " + row[2])
        else:
            await ctx.send(ctx.message.author.mention + " You don't have permision to change user's balance!")

    
    #Remove balance from tagged user
    @commands.command(help="Removes the amount that written to tagged user's balance (Works if used by Majors)", pass_context = True)
    async def remove_balance(self,ctx, message: str):
        permission = 0
        L = ctx.message.author.roles
        for i in range (len(L)):
            if(str(L[i])=='Major'):
                permission = 1
        try:
            sign, value = map(str, message.split('-'))
        except ValueError:
            await ctx.send('Format has to be -{amount}k')
            return
        
        try:
            sign, value = map(str, message.split('-'))
            points, temp = value.split("k")
        except ValueError:
            await ctx.send('Format has to be -{amount}k')
            return
        if(permission == 1):
            cur = self.db.cursor()
            for row in cur.execute('SELECT * FROM accounts'):
                if (int(row[1]) == int(ctx.message.mentions[0].id)):
                    sign, value = map(str, message.split('-'))
                    points, temp = value.split("k")
                    result = int(points) * 1000
                    cur.execute('''
                        UPDATE accounts SET user_balance = user_balance - (?) WHERE userid = (?)
                        ''',[result, row[1]])
                    self.db.commit()
                    await ctx.send(ctx.message.author.mention + " Balance succesfully reduced from " + row[2])
        else:
            await ctx.send(ctx.message.author.mention + " You don't have permision to change user's balance!")

    
    
    
    #send all the data in the accounts table
    @commands.command(help="Send all the information in the database via DM (Works if used by Majors)")
    async def send_all_acc_info(self,ctx):
        permission = 0
        L = ctx.message.author.roles
        for i in range (len(L)):
            if(str(L[i])=='Major'):
                permission = 1
        if(permission == 1):
            cur = self.db.cursor()
            for row in cur.execute('SELECT * FROM accounts'):
                #await ctx.send(row)
                await ctx.message.author.send(row)
        else:
            await ctx.send(ctx.message.author.mention + " You don't have permission to see all the accounts details")

