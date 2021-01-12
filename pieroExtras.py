import discord
from discord.ext import commands

def commandLineEmbed(title, lines, done):
		embed = discord.Embed(colour=discord.Colour(0xff0000))
		if done:
			embed = discord.Embed(colour=discord.Colour(0x00ff00))
		embed.set_author(name="Piero™ Server Management")
		embed.add_field(name=title, value="Shell Command")
		for i in lines:
			embed.add_field(name="\u200b", value=i, inline=True)
		# await bot.say(embed=embed)
		return embed