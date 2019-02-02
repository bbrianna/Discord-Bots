import logging
from time import sleep
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='logfile.log', encoding='utf-8', mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
from datetime import datetime
date_object = datetime.now()
from discord.ext.commands import Bot
import random
from discord import Game
import requests
import asyncio
logfiles = open("logfile.txt")
loglist = eval(logfiles.read())
logfiles.close()
print(loglist)
BOT_PREFIX = ("V!", "Venom!", "v!", "venom!")
TOKEN = "REDACTED"

client = Bot(command_prefix=BOT_PREFIX)


##Define command
@client.command(
    name='8ball',
    description="A game, good luck getting Venom to cooprate though.",
    brief="Good luck playing...",
    aliases=['eight_ball', 'eightball', '8-ball'],
    pass_context=True)
async def eight_ball(context):
	possible_responses = [
	    "I'M NOT A GAME",
	    "STOP THIS",
	    "I'M HUNGRY",
	    "STOP",
	    "APOLOGISE FOR BEING ANNOYING",
	    "APOLOGISE!",
	]
	ranmsg = random.choice(possible_responses)
	##send the message
	await client.say(ranmsg + ", " + context.message.author.mention)
	date_object = datetime.now()
	current_time = date_object.strftime('%Y:%D:%H:%M:%S')
	loglist.append(current_time + " " + context.message.author.mention +
	               " Command: 8ball " + " Response: " + ranmsg)
	logfiles = open("logfile.txt", "r+")
	logfiles.write(str(loglist))
	logfiles.close()
	print(ranmsg)


##Define command
@client.command(
    name='Squared',
    description="Squares any number for you.",
    brief="Squares any number for you.",
    aliases=['square', 'squared'],
    pass_number=True)
async def square(number):
	squared_value = int(number) * int(number)
	await client.say(str(number) + " squared is " + str(squared_value))
	date_object = datetime.now()
	current_time = date_object.strftime('%Y:%D:%H:%M:%S')
	loglist.append(current_time + " " + " Command: Square " + " Response: " +
	               str(squared_value))
	logfiles = open("logfile.txt", "r+")
	logfiles.write(str(loglist))
	logfiles.close()
	print(str(squared_value))


##Define command
@client.command(
    name='RandomNumGen',
    description=
    "A random number generator, generates a random number between 1, and 100",
    brief="Generates a random number",
    aliases=[
        'randomnumber', 'randomnumbergenerator', 'randnum', 'randomnumgen'
    ],
    pass_context=True)
async def randgen(context):
	ran = str(random.randint(1, 101))
	await client.say(ran + ", " + context.message.author.mention)
	date_object = datetime.now()
	current_time = date_object.strftime('%Y:%D:%H:%M:%S')
	loglist.append(current_time + " " + context.message.author.mention +
	               " Command: Randnum " + " Response: " + ran)
	logfiles = open("logfile.txt", "r+")
	logfiles.write(str(loglist))
	logfiles.close()
	print(ran)


##Define command
@client.command(
    name='Game',
    description="Some trashy humans are making a game about me and Eddie, I guess we should endorse them?",
    brief="Some trashy humans are making a game about me",
    aliases=['game', 'symbrockgame'],
    pass_context=True)
async def game():
	
	await client.say("Eddie told me some trashy humans are making a game about me and him.. I guess you should join and help them out / watch them at https://discord.gg/Sm5AdWS")

##Define command
@client.command(
    name="InsultMe",
    description="Will insult anyone without mercy",
    brief="Insults you.",
    aliases=['insultme', 'insult'],
    pass_context=True)
async def insultme(context):
	print("Insulted " + context.message.author.mention)
	possible_responses = [
	    'Garbage ape', 
      "Hairless mammal",
	    "Trash bae", 
      "MEAT SUIT",
	    "Chemical cocktail",
      "short - teethed",
	    "Landfill", 
	    "No u ∞+1",
      "Soiled meat",
      "Parasite monkey",
      "Lily-livered",
      "Dull teeth"
	]
	insultmsg = random.choice(possible_responses)
	await client.say(insultmsg + ", " + context.message.author.mention + ':heheyull:')
	date_object = datetime.now()
	current_time = date_object.strftime('%Y:%D:%H:%M:%S')
	loglist.append(current_time + " " + context.message.author.mention +
	               " Command: InsultMe" + " Response: " + insultmsg)
	logfiles = open("logfile.txt", "r+")
	logfiles.write(str(loglist))
	logfiles.close()
	print(insultmsg)



##Define command
@client.command(
    name='Aboutme',
    description="Tells you about the bot",
    brief="Bot information",
    aliases=['about', 'aboutme'],
    pass_context=True)
async def aboutme(context):
  possibleres = [
    "WE, ARE VENOM. [2tbc1887 Bot v0.0.16a(Beta), Venom Bot v0.0.07b(Alpha)]",
    "WE, ARE YULL. [2tbc1887 Bot v0.0.16a(Beta), Venom Bot v0.0.07b(Alpha)]"
  ]
  await client.say(random.choice(possibleres))



@client.command(
    name="Servers",
    description="Lists every server the bot is connected to",
    brief="Servers the bot is connected to",
    aliases=['servers'],
    pass_context=True)
async def serverslist(context):
	servers = client.servers
	serverlister = open("serverlister.txt", 'r+')
	serverlister.write("['Servers:']")
	for server in client.servers:
		await client.say(server.name + ", " + context.message.author.mention)
	serverlister.close()
	date_object = datetime.now()
	current_time = date_object.strftime('%Y:%D:%H:%M:%S')
	loglist.append(current_time + " " + context.message.author.mention +
	               " Command: Servers " + " Response: ##Server list sent##")
	logfiles = open("logfile.txt", "r+")
	logfiles.write(str(loglist))
	logfiles.close()


##@client.command(
##    name='StreamRequest (BETA)',
##    description="Request things for streams!",
##    brief="Stream requesting",
##    aliases=['request', 'streamrequest'],
##    pass_context=True)
##async def yesorno(context):
##  await client.say('This feature is currently in development!')
##  await client.say('Make a suggestion! You have 15 seconds and the message you send will be your response.')
##  response = client.wait_for_message(author=context.message.author, timeout=1500)
##  sleep(7)
##  await client.say("The recorded sugegstion was " + str(response))
##  requestfile = open("suggestionslist.txt", "r+")
##  requestlist = eval(requestfile.read())
##  print(requestlist)
##  requestlist.append(str(response))
##  print(requestlist)
##  requestfile.write(str(requestlist))


@client.command(
    name='Yull',
    description="The cult",
    brief="Cult",
    aliases=['yull'],
    pass_context=True)
async def Yull(context):

  possible_responses = [
      "Yull is love, Yull is life", 
      "Yull is everything",
      "Go Yull yourself",
      "YULL? YULL? YULLLLLLLLLL?",
      "Yull",
      "YULL THE YEET"
	  ]
  yullmsg = random.choice(possible_responses)
  await client.say(yullmsg + ", " + context.message.author.mention)
  date_object = datetime.now()
  current_time = date_object.strftime('%Y:%D:%H:%M:%S')
  loglist.append(current_time + " " + context.message.author.mention +
	               " Command:  " + " Response: " + yullmsg )
  logfiles = open("logfile.txt", "r+")
  logfiles.write(str(loglist))
  logfiles.close()



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
	await client.change_presence(game=Game(name="WITH MY FOOD | V!help"))
	print("logged in as " + client.user.name)


##pm_help = True
client.loop.create_task(list_servers())
client.run(TOKEN)
