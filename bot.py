import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='~')

bot_token = 'NjI2MDM3OTE5NTUwOTMwOTg1.XYt44Q.GWGaAQUJuIjguYnkfTSffu60d74'



@bot.event
async def on_ready():
    print(">>BOT IS ONLINE<<")

@bot.event
async def on_member_join(member):
    channel =bot .get_channel(619200604413231109)
    await channel.send(f'{member}加入了宿舍!!>_<')
    

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(619200604413231109)
    await channel.send(f'{member}就這樣狠心的離開我們! T_T')

@bot.command()
async def load(ctx,extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(F'Loaded {extension} done')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(F'Un-Loaded {extension} done')

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(F'Re-Loaded {extension} done')

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(F'cmds.{Filename[:-3]}')

if __name__ == '__main__':
    bot.run(bot_token)