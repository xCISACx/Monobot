from discord import Embed
from discord.ext import commands

class gifs:
	"""Fun GIFs to mess around with"""

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def laugh(self):
		e = Embed()
		e.set_image(url='https://pa1.narvii.com/6174/c1e7ec9420b3ad9b26a771067171b0aaee910707_hq.gif')
		await self.client.say(embed=e)

	@commands.command()
	async def laugh2(self):
		e = Embed()
		e.set_image(url='http://pa1.narvii.com/6374/1ba42d7c652fe8a3b17f6d008b8a98a246133de4_00.gif')
		await self.client.say(embed=e)

	@commands.command()
	async def mad(self):
		e = Embed()
		e.set_image(url='https://pa1.narvii.com/6517/996ef5597410e78681e40222c8343dba0e85cd1c_hq.gif')
		await self.client.say(embed=e)

	@commands.command()
	async def mad2(self):
		e = Embed()
		e.set_image(url='https://78.media.tumblr.com/074981170897f50c802f640c74076ba2/tumblr_mky7hcsWNK1qzqnxxo1_500.gif')
		await self.client.say(embed=e)

	@commands.command()
	async def mad3(self):
		e = Embed()
		e.set_image(url='http://i.imgur.com/EFY1SKI.gif')
		await self.client.say(embed=e)

	@commands.command()
	async def hot(self):
		e = Embed()
		e.set_image(url='https://pa1.narvii.com/6387/2f715952ae9ae062f2490060cb47fe16e6846457_hq.gif')
		await self.client.say(embed=e)

	@commands.command()
	async def startled(self):
		e = Embed()
		e.set_image(url='https://media.giphy.com/media/uuAafrSFCT4ic/giphy.gif')
		await self.client.say(embed=e)

	@commands.command()
	async def dance(self):
		e = Embed()
		e.set_image(url='https://media.tenor.com/images/4faf16106c9741d02037e3060ea7788b/tenor.gif')
		await self.client.say(embed=e)

	@commands.command(pass_context=True)
	async def jumpscare(self, context):
		await self.client.delete_message(context.message)
		e = Embed()
		e.set_image(url='https://i.imgur.com/aH1xD9S.gif')
		await self.client.say(embed=e)

	@commands.command()
	async def when_you_compliment_me(self):
		"""This command does not exist."""

		e = Embed()
		e.set_image(url='https://pa1.narvii.com/5673/d3ccd3b9789a575d82537607420261c8a2bb7f49_hq.gif')
		await self.client.say(embed=e)

	@commands.command()
	async def wisdom_from_dev(self):
		"""This command does not exist."""

		e = Embed()
		e.set_image(url='https://i.imgur.com/BY7S66c.png')
		await self.client.say(embed=e)

def setup(client):
    client.add_cog(gifs(client))