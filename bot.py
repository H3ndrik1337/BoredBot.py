import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import requests
import os
import youtube_dl

bot = commands.Bot(command_prefix='a.')
from discord import opus
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll',
             'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

type = 1
client = discord.Client()

players = {}

hendrikid = "227403635166806016"

minutes = 0
hour = 0

@client.event
async def on_ready():
    print("Eingeloggt als BoredBot V0.1")
    print(client.user.name)
    print(client.user.id)
    print("------------")
    await client.change_presence(game=discord.Game(name="access with !help"))

@client.event
async def on_message(message):
    if message.content.startswith('!join'):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "Ich habe keinen Voicechannel gefunden.")
        except Exception as error:
            await client.send_message(message.channel, "Ein Error: ```{error}```".format(error=error))

    if message.content.startswith('!quit'):
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "-No Channel-")
        except Exception as Hugo:
            await client.send_message(message.channel, "Ein Error: ```{haus}```".format(haus=Hugo))

    if message.content.startswith('!play '):
        try:
            yt_url = message.content[6:]
            channel = message.author.voice.voice_channel
            voice = await client.join_voice_channel(channel)
            player = await voice.create_ytdl_player(yt_url)
            players[message.server.id] = player
            player.start()
        except:
            await client.send_message(message.channel, "Error.")

    if message.content.startswith('!pause'):
        try:
            players[message.server.id].pause()
        except:
            pass
    if message.content.startswith('!resume'):
        try:
            players[message.server.id].resume()
        except:
            pass    

    
    
    

@client.event
async def on_message(message):
    if message.content.startswith("!test"):
        await client.send_message(message.channel, "Test erfolgreich")


    if message.content.startswith("!ping"):
        await client.send_message (message.channel, "PONG!")


    if message.content.startswith("!supreme"):
        await client.send_message (message.channel, "http://www.supremenewyork.com")


    if message.content.startswith("!steam"):
        await client.send_message (message.channel, "http://steamcommunity.com/id/cautus/")


    if message.content.startswith("!owner"):
        await client.send_message(message.channel, "Dieser Bot wurde von Hendrik erstellt. Bin stolz drauf.")


    if message.content.startswith("!memes"):
        await client.send_message(message.channel, "Memes an die Macht!")


    if message.content.lower().startswith("!info"):
        info = discord.Embed(
            title="Hey, Ich bin der BoredBot :)",
            color=0xe74c3c,
            description="Hey, hier siehst Du die aktuellen Commands:\n"
                        "!Wenn ihn Vorschläge für die Verbesserung des Bots habt, könnt ihr mich gerne anschreiben. Auch im Falle eines Buggs, stehe ich zur Verfügung\n"
                        "DiscordID: H3ndrik#7385\n"
                        "\n"
                        "\n"
                        "Beta 0.1"

        )

        await client.send_message(message.channel, embed=info)



    if message.content.startswith("!russia"):
        response = requests.get("https://i.ytimg.com/vi/d0z_uXA_pdI/maxresdefault.jpg", stream=True)
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="Bild.png", content="For Mother Russia")


    if message.content.lower().startswith("!help"):
        help = discord.Embed(
            title="**Hey, Ich bin der BoredBot** :)",
            color=0xe74c3c,
            description="hier kannst du alle derzeit möglichen Commands sehen: \n"
                        "https://pastebin.com/GKcrpTun"



        )
        help.set_author(
            name="*klick hier*",
            url="https://www.youtube.com/watch?v=MG9e6m_4yVY"

         )
        help.add_field(
            name="**Neuerungen bei der V0.2**",
            value="1. Custom Command bei PN\n" 
                  "2. Es wurde die Musik Funktion hinzugefügt\n",
        )




        await client.send_message(message.channel, embed=help)

    if message.content.startswith('!game') and message.author.id == hendrikid:
        game = message.content[6:]
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, "Status zu " + game + " geändert")

    if message.content.startswith("!hardbass"):
        await client.send_message(message.channel,"Ich heiße Niklas, und das ist mein Hardbass!")



    if message.content.startswith("!asmr"):
        await client.send_message(message.channel, "Autonomous Sensory Meridian Response (oft als ASMR abgekürzt) bezeichnet die Erfahrung eines statisch-ähnlichen oder kribbelnden Gefühls auf der Haut, das typischerweise auf der Kopfhaut beginnt und sich am Nacken und der oberen Wirbelsäule entlang bewegt (sogenannte Tingles)")


    if message.content.startswith("!gif"):
        gif_tag = message.content[5:]
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(
            str(rgif.get("data", {}).get('image_original_url')), stream=True
        )
        await  client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="video.gif")
        
        
    if message.content.startswith('!uptime'):
        await client.send_message(message.channel, "**Ich bin schon {0} Stunde/n und {1} Minuten online auf {2}. **".format(hour, minutes, message.server))
        
        
        
    if message.content.lower().startswith('!flip'): #Coinflip 50/50% chance kopf oder zahl
        choice = random.randint(1,2)
        if choice == 1:
            await client.add_reaction(message, '🌑')
        if choice == 2:
            await client.add_reaction(message, '🌕')
        

async def total_uptime():
    await client.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not client.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1

client.loop.create_task(total_uptime())    


OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll',
             'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass

    raise RuntimeError('Could not load an opus lib. Tried %s' %
                       (', '.join(opus_libs)))
opts = {
    'default_search': 'auto',
    'quiet': True,
}  # youtube_dl options



load_opus_lib()

   






client.run(str(os.environ.get('BOT_TOKEN')))
