from discord.ext import commands
import discord
import distro
import psutil
import platform
from pieroExtras import *

class botHelp(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx):
		users = str(len(self.bot.users))
		guilds = str(len(self.bot.guilds))
		vote_link = "[**Vote link**](http://bit.ly/2mLoBOs) ⬆️"
		cpu0, cpu1, cpu2, cpu3 = psutil.cpu_percent(interval=1, percpu=True)
		ram = str(psutil.virtual_memory()[3] / 1000000000)
		ram_round = ram[:3]
		disk = str(psutil.disk_usage('/')[1] / 1000000000)
		disk_round = disk[:4]
		boot_time = str(psutil.boot_time() / 100000000)
		boot_time_round = boot_time[:4]
		linux_distro = distro.os_release_info()

		await ctx.send("```Piero™ Bot\nCPUs:\n\tCPU 0: "+progressBar(cpu0,100)+str(cpu0)+"\n\tCPU 1: "+progressBar(cpu1,100)+str(cpu1)+"\n\tCPU 2: "+progressBar(cpu2,100)+str(cpu2)+"\n\tCPU 3: "+progressBar(cpu3,100)+str(cpu3)+"\nRAM:"+ram+"```")
	
def setup(bot):
	bot.add_cog(botHelp(bot))