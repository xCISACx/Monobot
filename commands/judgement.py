from time import time
from discord import Embed, Member
from discord.ext import commands

class judgement:
	"""To bully Zero with."""

	def __init__(self, client):
		self.client = client
		self.ban_dict = {} # id => last_used_timestamp

	@commands.command()
	async def how_i_feel_about_zero(self):
		"""This command does not exist."""

		await self.client.say('I-It\'s not like I like you or anything. B-baka.')
		e = Embed()
		e.set_image(url='https://cdn.discordapp.com/attachments/407151453367435264/420726577962156032/1b3fe2ca44299ef4794780259fbec1451e16cc31_hq.gif')
		await self.client.say(embed=e)

	@commands.command()
	async def how_much_do_you_love_me(self):
		"""This command does not exist."""

		await self.client.say('I love you BEAR-y much!')

	@commands.command()
	async def love(self):
		"""**This command is for Zero only.**"""

		e = Embed()
		e.set_image(url='https://orig00.deviantart.net/d5ce/f/2015/019/c/4/danganronpa_valentine__monokuma_love__by_frozenclaws-d8en7wf.png')
		await self.client.say(embed=e)

	@commands.command()
	async def eval(self):
		"""This command evaluates the given command."""

		e = Embed()
		e.set_image(url='https://i.imgur.com/lw3F5cY.png')
		await self.client.say(embed=e)

	@commands.command(pass_context=True)
	async def ban(self,  context):
		"""This command allows you to ban a person."""

		speaker = context.message.author
		current_timestamp = int(time())

		if speaker.id in self.ban_dict:
			print(current_timestamp - self.ban_dict[speaker.id])
			if current_timestamp - self.ban_dict[speaker.id] > 30:
				# its been more than thirty seconds since they last used it, notify
				pass
			else:
				await self.client.say('<@{}> You can only use this command every 30 seconds to prevent ping spamming.'.format(speaker.id))
				await self.client.say('Time for the punishment!')
				e = Embed()
				e.set_image(url='https://pa1.narvii.com/6235/002ddd793ae0a3203a80ac8546bd1fc9c3540453_hq.gif')
				await self.client.say(embed=e)
				return
		else:
			self.ban_dict[speaker.id] = current_timestamp

		await self.client.say('Telling <@270211292541878282> that you tried to ban a person!')

		e = Embed()
		e.set_image(url='https://i.imgur.com/lw3F5cY.png')
		await self.client.say(embed=e)

	@commands.command()
	async def guilty(self, user : Member): # 
		"""Judgement shall be delivered!"""

		await self.client.say('{} has been found guilty. Time for the punishment!'.format(user.mention))
		e = Embed()
		e.set_image(url='https://pa1.narvii.com/6235/002ddd793ae0a3203a80ac8546bd1fc9c3540453_hq.gif')
		await self.client.say(embed=e)

def setup(client):
    client.add_cog(judgement(client))