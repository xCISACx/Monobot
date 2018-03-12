import discord
import asyncio

from discord.ext.commands import Bot
from discord.ext import commands

from commands.gifs import gifs
from commands.judgement import judgement
from commands.memes import memes

extensions = [
	'commands.gifs',
	'commands.judgement',
	'commands.memes'
]

client = Bot(description="Monobot by モノクマ#1038", command_prefix="!kuma", pm_help = False, help_attrs = { 'name': 'nds' })

@client.event
async def on_ready():
	print('Logged in as {} | Connected to {} servers | Connected to {} users'.format(
		client.user.name,
		len(client.servers),
		len(set(client.get_all_members()))
	))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))

	return await client.change_presence(game=discord.Game(name='the Killing  Game')) #This is buggy, let us know if it doesn't work.

@client.event
async def on_command_error(error, ctx):
	print(error)

for extension in extensions:
	try:
	    client.load_extension(extension)
	except Exception as e:
	    print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))
client.run('NDIwNDY0MzY4MjQxNjA2NjU2.DX_Deg.mEM2eUBdgqLVQjONyY0o1YPQY3k')

