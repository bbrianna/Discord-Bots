##Command that will eat a random person in theserver##
from datetime import datetime
date_object = datetime.now()
from discord.ext.commands import Bot
import random
from discord import Game
import requests
import asyncio
BOT_PREFIX = ("[Prefix]", "[Prefix]")
TOKEN = "[Discord developer bot token]"

client = Bot(command_prefix=BOT_PREFIX)

##Define command
@client.command(
    name='8ball',
    description="Answers a yes or no question. \n  Usage: 2!8ball <message>",
    brief="Answers from the beyond.",
    aliases=['eight_ball', 'eightball', '8-ball'],
    pass_context=True)
async def eight_ball(context):
	possible_responses = [
	    'That is a resounding no',
	    "It isn't likely",
	    "Unfortunately... No",
	    "Too hard to tell",
	    "It is possible",
	    "Definitely",
	]
	ranmsg = random.choice(possible_responses)
	##send the message
	await client.say(ranmsg + ", " + context.message.author.mention)

##Create a repeating task to print out list of servers which the bot has been added to.
async def list_servers():
	await client.wait_until_ready()
	while not client.is_closed:
		print("##----+++------Currents servers:------+++----##")
		for server in client.servers:
			print(server.name)
		await asyncio.sleep(120)

##Set up the bot and start listening for commands
@client.event
async def on_ready():
	await client.change_presence(game=Game(name="Procrastination | 2!help"))
	print("logged in as " + client.user.name)

client.loop.create_task(list_servers())
client.run(TOKEN)