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

def formatShell(sending, line, lines, variable, errorMessage):
	if line:
		lines.append(str(line))
		while len(line) > 125:
			line = line[125:]
		if len(lines) > 15:
			lines.remove(lines[0])
	else:
		line = ""
		print(sending)
		if sending == "":
			sending = errorMessage + "\n" + variable
		else:
			sending = "Done\n" + sending
		return sending, lines, True
	sending = ""
	for i in lines:
		sending = sending + i + "\n"
	sending = '```' + sending + '```'
	return sending, lines, False

def progressBar(value, max):
	num = int(value*20/max)
	bar = ""
	x = 0
	while x < num:
		bar = bar + "█"
		x+=1
	while len(bar) < 20:
		bar = bar + " "
	return "["+bar+"] - "