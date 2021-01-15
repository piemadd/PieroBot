from discord.ext import commands

class packageManagement(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def pipInstall(self, ctx, package):
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

	@commands.command(pass_context=True)
	async def pipUninstall(self, ctx, package):
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

def setup(bot):
	bot.add_cog(packageManagement(bot))