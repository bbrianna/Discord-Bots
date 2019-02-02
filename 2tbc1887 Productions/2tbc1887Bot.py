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
BOT_PREFIX = ("2!", "2t!")
TOKEN = "REDACTED"

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
    name='Spam',
    description="Spams you many times",
    brief="You've got mail!",
    aliases=['spamme', 'spam'],
    pass_context=True)
async def spam(context):
	await client.say(context.message.author.mention + "Enjoy!")
	await client.say(context.message.author.mention)
	await client.say(context.message.author.mention)
	await client.say(context.message.author.mention)
	await client.say(context.message.author.mention)
	await client.say(context.message.author.mention)
	await client.say(context.message.author.mention)
	await client.say(context.message.author.mention)
	await client.say(context.message.author.mention)
	await client.say(context.message.author.mention)
	await client.say(context.message.author.mention)
	await client.say(context.message.author.mention)
	await client.say(context.message.author.mention)
	await client.say(context.message.author.mention)
	await client.say(context.message.author.mention)
	await client.say(context.message.author.mention)
	date_object = datetime.now()
	current_time = date_object.strftime('%Y:%D:%H:%M:%S')
	loglist.append(current_time + " " + context.message.author.mention +
	               " Command: Spam" + " Response: " +
	               context.message.author.mention)
	print(context.author.message.mention + "Spammed :)")


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
    name='BitcoinWorth',
    description="Will query CoinBase for the current BTC price in USD",
    brief="Prints the current price of Bitcoin",
    aliases=['btc', 'btcprice', 'btcworth', 'bitcoinworth', 'bitcoin'])
async def bitcoin():
	url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
	response = requests.get(url)
	value = response.json()['bpi']['USD']['rate']
	await client.say("Bitcoin price is: $" + value + "USD")
	##date_object = datetime.now()
	##current_time = date_object.strftime('%Y:%D:%H:%M:%S')
	##loglist.append(current_time + " " + context.message.author.mention + " Command: BTC " + " Response: " + value )
	print("$" + value)


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
	    'Your family tree LGBT', "Your parents come from Thottage Cottage",
	    "Your ancestors incestors", "Your Granny Tranny",
	    "Your sister a mister", "Your brother is your mother",
	    "You come from The Thottage Cottage", "You come from the Hoe Home",
	    "no u ∞+1", "Your mum gay", "Your moe a hoe",
	    "Hippity Hoppity you are now my Property",
	    "Your mother is your Brother"
	]
	insultmsg = random.choice(possible_responses)
	await client.say(insultmsg + ", " + context.message.author.mention)
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
    name="Nudes",
    description="Sends you nudes",
    brief="Sends you nudes.",
    aliases=['nudes', 'sendnudes'],
    pass_context=True)
async def nudes(context):
	possible_responses = [
	    'http://bit.ly/MyNuDeS',
	    "https://cdn-images-1.medium.com/max/1600/1*iFN_PWPWs6TQ9JzDp2v9Wg.jpeg",
	    "https://cdn.static-economist.com/sites/default/files/images/2015/09/blogs/economist-explains/code2.png",
	    "http://mediad.publicbroadcasting.net/p/kuow/files/styles/x_large/public/201710/36605465764_3b9393175b_b.jpg",
	    "https://nerdist.com/wp-content/uploads/2017/10/The-Matrix-code.jpg",
	    "http://zelig880.com/wp-content/uploads/2018/01/javascript-promises.jpg",
	]
	nudemsg = random.choice(possible_responses)
	await client.say(context.message.author.mention +
	                 " just this once, don't tell anyone! " + nudemsg)
	date_object = datetime.now()
	current_time = date_object.strftime('%Y:%D:%H:%M:%S')
	loglist.append(current_time + " " + context.message.author.mention +
	               " Command: Nudes " + " Response: " + nudemsg)
	logfiles = open("logfile.txt", "r+")
	logfiles.write(str(loglist))
	logfiles.close()
	print("Nudes :)")


##Define command
@client.command(
    name='Aboutme',
    description="Tells you about the bot",
    brief="Bot information",
    aliases=['about', 'aboutme'],
    pass_context=True)
async def aboutme(context):
	await client.say("The offical 2tbc1887 Productions Bot v0.0.15c(Beta). " +
	                 context.message.author.mention)
	print("About")


##Define command
@client.command(
    name="InsultMegen",
    description="Will insult anyone without mercy",
    brief="Randomly generated insults (BETA)",
    aliases=['insultmegen', 'insultgen'],
    pass_context=True)
async def insultmegen(context):
	print("Insulted " + context.message.author.mention)
	possible_responses = ['thottiest thot of them all', "accident"]
	insultmsg = random.choice(possible_responses)
	await client.say("You are the biggest " + insultmsg + ", " +
	                 context.message.author.mention)
	date_object = datetime.now()
	current_time = date_object.strftime('%Y:%D:%H:%M:%S')
	loglist.append(current_time + " " + context.message.author.mention +
	               " Command: InsultMeGen" + " Response: " + insultmsg)
	logfiles = open("logfile.txt", "r+")
	logfiles.write(str(loglist))
	logfiles.close()
	print(insultmsg)


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


@client.command(
    name='WhoIsAwesome',
    description="Will tell you who is awesome",
    brief="Who is awesome? Ask!",
    aliases=['whoisawesome', 'awesome'],
    pass_context=True)
async def whoisawesome(context):
	msg = "The person who is most awesome is "
	##msg2 = " Oh, and that @192537330509152257 guy is pretty cool"
	await client.say(msg + context.message.author.mention)
	date_object = datetime.now()
	current_time = date_object.strftime('%Y:%D:%H:%M:%S')
	loglist.append(current_time + " " + context.message.author.mention +
	               " Command: WhoIsAwesome " + " Response: " + msg)
	logfiles = open("logfile.txt", "r+")
	logfiles.write(str(loglist))
	logfiles.close()


@client.command(
    name='StreamRequest (BETA)',
    description="Request things for streams!",
    brief="Stream requesting",
    aliases=['request', 'streamrequest'],
    pass_context=True)
async def yesorno(context):
  await client.say('This feature is currently in development!')
  await client.say('Make a suggestion! You have 15 seconds and the message you send will be your response.')
  response = client.wait_for_message(author=context.message.author, timeout=1500)
  sleep(7)
  await client.say("The recorded sugegstion was " + str(response))
  requestfile = open("suggestionslist.txt", "r+")
  requestlist = eval(requestfile.read())
  print(requestlist)
  requestlist.append(str(response))
  print(requestlist)
  requestfile.write(str(requestlist))


@client.command(
    name='Anime',
    description="Anime",
    brief="Anime",
    aliases=['anime'],
    pass_context=True)
async def anime(context):
	possible_responses = ["Yuri on Ice", "Erased"]
	msg = "Do you like " + random.choice(possible_responses) + " ? I do!"
	await client.say(msg + ", " + context.message.author.mention)
	date_object = datetime.now()
	current_time = date_object.strftime('%Y:%D:%H:%M:%S')
	loglist.append(current_time + " " + context.message.author.mention +
	               " Command: Anime " + " Response: " + msg)
	logfiles = open("logfile.txt", "r+")
	logfiles.write(str(loglist))
	logfiles.close()

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
	await client.change_presence(game=Game(name="Procrastination | 2!help"))
	print("logged in as " + client.user.name)

##pm_help = True
client.loop.create_task(list_servers())
client.run(TOKEN)
