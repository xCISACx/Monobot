from discord import Embed
from discord.ext import commands
from asyncio import sleep

class memes:
	"""Memes"""

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def olá(self):
		"""This meme belongs to Maddie."""
		await self.client.say('© Maddie 2017')
		e = Embed()
		e.set_image(url='https://cdn.discovery.pgsitecore.com/en-us/-/media/Olay_PathFinder/Images/a/OLAY%20TE%207IN1%20DEEP%20PENETRATING%20MOISTURE%20BODY%20WASH_Front.png?w=460&v=1-201705260605')
		await self.client.say(embed=e)

	@commands.command()
	async def diplomacy(self):
		e = Embed()
		e.set_image(url='https://i.imgur.com/YAwLsU2.png')
		await self.client.say(embed=e)

	@commands.command()
	async def getsomehelp(self):
		e = Embed()
		e.set_image(url='https://i.imgur.com/y8Ea8jB.gif')
		await self.client.say(embed=e)

	@commands.command()
	async def delet(self):
		e = Embed()
		e.set_image(url='https://i.imgur.com/cs3QA0p.jpg')
		await self.client.say(embed=e)

	@commands.command()
	async def edadelet(self):
		e = Embed()
		e.set_image(url='https://img.fireden.net/v/image/1475/40/1475405308388.png')
		await self.client.say(embed=e)

	@commands.command()
	async def deletdog(self):
		e = Embed()
		e.set_image(url='https://i.imgur.com/huf6YNM.png')
		await self.client.say(embed=e)

	@commands.command()
	async def yurunning(self):
		e = Embed()
		e.set_image(url='https://cdn.discordapp.com/attachments/407207388693790750/420692979989086227/fdEqJh.gif')
		await self.client.say(embed=e)

	@commands.command()
	async def portuguese(self):
		"""QUACK QUACK"""
		e = Embed()
		e.set_image(url='https://img.buzzfeed.com/buzzfeed-static/static/2017-12/27/14/asset/buzzfeed-prod-fastlane-02/sub-buzz-30017-1514404758-11.png')
		await self.client.say(embed=e)

	@commands.command()
	async def dab(self):
		e = Embed()
		e.set_image(url='https://pm1.narvii.com/6240/fe3e4735239ea8192110cc2eee4df4b60f7eb9d8_hq.jpg')
		await self.client.say(embed=e)

	#@commands.command()
	async def abc(self):
		"""aka portable Zero"""
		alphabet = ['abcdefg','hijklmnop','qrs','tuv','wx','yz']
		for segment in alphabet:
			await self.client.say('%0A'.join(segment.split()))
			await sleep(0.5)
		await self.client.say('***flies away***')

	#@commands.command()
	async def nations(self):
		"""aka portable Zero"""
		nations = ['United States, Canada, Mexico, Panama, Haiti, Jamaica, Peru', 'Republic Dominican, Cuba, Caribbean', 'Greenland, El Salvador too',
		 'Puerto Rico, Colombia, Venezuela, Honduras, Guyana, and still', 'Guatemala, Bolivia, then Argentina, Ecuador, Chile, and Brazil.', 
		 'Costa Rica, Belize, Nicaragua, Bermuda, Bahamas, Tobago, San Juan.', 'Paraguay, Uruguay, Suriname, and French Guiana, Barbados, and Guam', 
		 'Norway and Sweden and Iceland and Finland, and Germany now in one piece;', 'Switzerland, Austria, Czechoslovakia, Italy, Tukey and Greece', 
		 'Poland, Romania, Scotland, Albania, Ireland, Russia, Oman;', 'Bulgaria, Saudi Arabia, Hungary, Cyprus, Iraq and Iran', 'There\'s Syria, Lebanon, Israel, Jordan, both Yemens, Kuwait, and Bahrain;', 
		 'The Netherlands, Luxembourg, Belgium, and Portugal, France, England, Denmark, and Spaaaaaaaain', 'India, Pakistan, Burma, Afghanistan, Thailand, Nepal, and Bhutan;', 
		 'Kampuchea, Malaysia, then Bangladesh, Asia, and China, Korea, Japan','Mongolia, Laos, and Tibet, Indonesia, the Philippine Islands, Taiwan;', 
		 'Sri Lanka, New Guinea, Sumatra, New Zealand, then Borneo, and Vietnam', 'Tunisia, Morocco, Uganda, Angola, Zimbabwe, Djibouti, Botswana;', 'Mozambique, Zambia, Swaziland, Gambia, Guinea, Algeria, Ghana', 
		 'Burundi, Lesotho, and Malawi, Togo, The Spanish Sahara is gone;', 'Niger, Nigeria, Chad, and Liberia, Egypt, Benin, and Gabon',  'Tanzania, Somalia, Kenya, and Mali, Sierra Leone, and Algiers;', 
		 'Dahomey, Namibia, Senegal, Libya, Cameroon, Congo, Zaire.', 'Ethiopia, Guinea-Bissau, Madagascar, Rwanda, Maore, and Cayman;','Hong Kong, Abu Dhabi, Qatar, Yugoslavia—', 
		 'Crete, Mauritania, then Transylvania—', 'Monaco, Liechtenstein, Malta, and Palestine, Fiji, Australia, Sudan!']
		for segment in nations:
			await self.client.say('\n'.join(segment.split()))
			await sleep(0.5)
		await self.client.say('***flies away***')



def setup(client):
    client.add_cog(memes(client))