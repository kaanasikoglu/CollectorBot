import discord
from discord.ext import commands

import os

from main_cog import main_cog
from music_cog import music_cog
from fun_cog import fun_cog
from collector_cog import collector_cog
from calculator_cog import calculator_cog

BOT_PREFIX = (".", "?")
TOKEN ="xx"
bot = commands.Bot(command_prefix=BOT_PREFIX)

bot.remove_command('help')

bot.add_cog(main_cog(bot))
bot.add_cog(music_cog(bot))
bot.add_cog(fun_cog(bot))
bot.add_cog(collector_cog(bot))
bot.add_cog(calculator_cog(bot))

bot.run(TOKEN)