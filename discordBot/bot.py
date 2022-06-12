# -*- coding: cp1252 -*-
import requests
import random
import time
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

url = "https://twitter135.p.rapidapi.com/Search/"

querystring = {"q":"dream smp","count":"20","tweet_search_mode":"live"}

headers = {
	"X-RapidAPI-Host": "twitter135.p.rapidapi.com",
	"X-RapidAPI-Key": "cadd600414mshd4b4ff5b2e67303p127fb5jsn8176d849345a"
}

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = requests.request("GET", url, headers=headers, params=querystring)
    keylist = list(response.json()["globalObjects"]["tweets"].keys())
    key = keylist[random.randint(0, len(keylist)-1)]
    text = response.json()["globalObjects"]["tweets"][key]["full_text"]

    if message.content == "please kill me":
        await message.channel.send(text)

client.run(TOKEN)