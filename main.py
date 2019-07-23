import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Logged in.")

@bot.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if channel.name == "general":
            await channel.send("Welcome " + member.mention + " to the bot time server!")

@bot.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if channel.name == "general":
            await channel.send("Sadly, " + member.name + " just left the server.")

@bot.command()
async def ping(ctx, *, argument: str):
    await ctx.send("Pong" + argument)

bot.run("NjAyOTgzMTA1NjQ0NDYyMTEx.XTaU6w.1GO2MgbwPCbZI6jHtgIB9UgRAHE")
