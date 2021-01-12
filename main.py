import discord
from discord.ext import commands
import random, os, pieroExtras
from subprocess import Popen, PIPE

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='pi$', description="Bot or whateva", intents=intents)

bot.load_extension("cogs.serverManagement")

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
	for i in range(times):
		await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
	await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def shellTest(ctx):
	p = Popen("bash yourprogram.sh", stdout=PIPE, close_fds=True, shell=True)
	lines = []
	msg = await ctx.send('\u200b')
	while True:
		line = p.stdout.readline().strip().decode("utf-8")[0:100]
		if line:
			lines.append(str(line))
			if len(lines) > 10:
				lines.remove(lines[0])
		else:
			sending = "Done\n" + sending
			await msg.edit(content=sending)
			break
		sending = ""
		for i in lines:
			sending = sending + i + "\n"
		sending = '```' + sending + '```'
		await msg.edit(content=sending)

@bot.command()
async def pipInstall(ctx, package):
	p = Popen("pip install " + package, stdout=PIPE, close_fds=True, shell=True)
	lines = []
	msg = await ctx.send('\u200b')
	while True:
		line = p.stdout.readline().strip().decode("utf-8")
		if line:
			lines.append(str(line))
			while len(line) > 125:
				line = line[125:]
			if len(lines) > 10:
				lines.remove(lines[0])
		else:
			try:
				sending = "Done\n" + sending
			except:
				sending = "Done"
			await msg.edit(content=sending)
			break
		sending = ""
		for i in lines:
			sending = sending + i + "\n"
		sending = '```' + sending + '```'
		await msg.edit(content=sending)

@bot.command()
async def pipUninstall(ctx, package):
	p = Popen("pip uninstall -y " + package, stdout=PIPE, close_fds=True, shell=True)
	lines = []
	msg = await ctx.send('\u200b')
	while True:
		line = p.stdout.readline().strip().decode("utf-8")
		if line:
			lines.append(str(line))
			while len(line) > 125:
				line = line[125:]
			if len(lines) > 10:
				lines.remove(lines[0])
		else:
			try:
				sending = "Done\n" + sending
			except:
				sending = "Package " + package + " does not exist!"
			await msg.edit(content=sending)
			break
		sending = ""
		for i in lines:
			sending = sending + i + "\n"
		sending = '```' + sending + '```'
		print(sending)
		await msg.edit(content=sending)

bot.run(os.getenv("DISCORD_TOKEN"))