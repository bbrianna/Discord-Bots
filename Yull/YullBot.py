from datetime import datetime
date_object = datetime.now()
from discord.ext.commands import Bot
import random
from discord import Game
import requests
import asyncio
BOT_PREFIX = ("y!", "Y!", "Yull!")
TOKEN = "REDACTED"

client = Bot(command_prefix=BOT_PREFIX)

##Define command
@client.command(
    name='yull',
    description="Answers yull. \n  Usage: !yull <message>",
    brief="Only Yull.",
    aliases=['YULL', '25_21_12_12', 'bfoo'],
    pass_context=True)
async def yull(context):
	possible_responses = [
	    'Praise be Yull',
	    "Yullz it",
	    "Blessed by Yull",
	    "hehehe...Yull",
	    "I yull you, you yull me, we're a yulling family",
	    "YULL",
      "DO IT FOR THE YULLT",
      "You know we had to yull it to 'em" ,
      "yull",
      "I'm so sorry that you're here, in this server, i really am",
      "I am Yull Bot, please say y!yull again...***p l e a s e***" ,
      "WE ARE YULL" ,
      "The Yull is always here for you" ,
      "<@!192537330509152257> IS AGAINST THE YULL FOR HE HAS DISRESPECTED ME" ,
      "Always tell <@!441009031809728514> to go the fuck to sleep. If this is <@!441009031809728514>, GO THE *FUCK TO **SLEEP***" ,
      "Drink some water and eat some food",
      "The Yullt Loves You" ,
      "The Yull loves you" ,
      "Our yullther--Who yeets in heaven --Yullowed be thy name--Yull kyulldom come--Thy yeets be done--On earth as it yeets in heaven--Give us this day our daily yull--And yeet us our tresspassers--As we yeet those yeetpass against us--And lead us not into yulltations--For the yeet and the yull and the glory are yours--Now and foryullver--Yullmen",
      "Praise be to yull, lord Yullsus Christ",
      "Buy Phoenix some applesauce",
      "Give Phoenix some money to buy applesauce"
		":regional_indicator_y: :regional_indicator_u: :regional_indicator_l: :regional_indicator_l: "

      
	]
	ranmsg = random.choice(possible_responses)
	##Send the message
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
	await client.change_presence(game=Game(name="YULL BOT | !help"))
	print("logged in as " + client.user.name)

client.loop.create_task(list_servers())
client.run(TOKEN)
