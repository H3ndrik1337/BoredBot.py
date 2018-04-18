import discord
from discord.ext import commands
from discord.ext.commands import Bot
import Bot
import asyncio
import io
import random
import requests
import os


type = 1
client = discord.Client()

hendrikid = "227403635166806016"

@client.event
async def on_ready():
    print("Eingeloggt als BoredBot V0.1")
    print(client.user.name)
    print(client.user.id)
    print("------------")
    await client.change_presence(game=discord.Game(name="Game", url="twitch.tv/hendrigg", type=1))


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






bot.run(str(os.environ.get('BOT_TOKEN')))

