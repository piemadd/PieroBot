import discord
from discord.ext import commands
import random, os, pieroExtras
from subprocess import Popen, PIPE
from flask import Flask
from threading import Thread

print("testing")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='pi$', description="Bot or whateva", intents=intents, help_command=None)
app = Flask('')

bot.load_extension("cogs.serverManagement")
bot.load_extension("cogs.botHelp")

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
	if ctx.message.author.id == 231628302152892427:
		print("yes!")
	p = Popen("bash yourprogram.sh", stdout=PIPE, close_fds=True, shell=True)
	lines = []
	message = "Starting program (only prints 3 lines at a time)"
	done = False
	msg = await ctx.send('\u200b')
	count = 0
	while True:
		line = p.stdout.readline().strip().decode("utf-8")
		message, lines, done = formatShell(message, line, lines, "yourprogram.sh", "Sorry, there was an error with the following script:")
		if count < 3:
			count = 0
			await msg.edit(content=message)
		count += 1
		if done:
			break

@bot.command()
async def pipInstall(ctx, package):
	if ctx.message.author.id != 231628302152892427:
		return
	if "aiohttp" in package.lower() or "pynacl" in package.lower():
		return
	p = Popen("pip install " + package.split()[0], stdout=PIPE, close_fds=True, shell=True)
	lines = []
	message = "Starting program (only prints 3 lines at a time)"
	done = False
	msg = await ctx.send('\u200b')
	count = 0
	while True:
		line = p.stdout.readline().strip().decode("utf-8")
		message, lines, done = formatShell(message, line, lines, package.split()[0], "Sorry the following package does not exist:")
		if count < 3:
			count = 0
			await msg.edit(content=message)
		count += 1
		if done:
			break

@bot.command()
async def pipUninstall(ctx, package):
	if ctx.message.author.id != 231628302152892427:
		return
	if "aiohttp" in package.lower() or "pynacl" in package.lower():
		return
	p = Popen("pip uninstall -y " + package.split()[0], stdout=PIPE, close_fds=True, shell=True)
	lines = []
	message = "Starting uninstalll (only prints 3 lines at a time)"
	done = False
	msg = await ctx.send('\u200b')
	count = 0
	while True:
		line = p.stdout.readline().strip().decode("utf-8")
		message, lines, done = formatShell(message, line, lines, package.split()[0], "Sorry the following package does not exist on your system:")
		if count < 3:
			count = 0
			await msg.edit(content=message)
		count += 1
		if done:
			break

bot.run(os.getenv("DISCORD_TOKEN"))