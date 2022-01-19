from cProfile import run
from email import message
from re import A
import discord
import os
LENNART = 0
client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))#gives you a log if login was succsesfull


@client.event
async def on_message(message, count = ["","","","","","","","",""]):#the mini game code
    for number in range (1,2):
        if message.author == client.user:
            return
        if message.content.startswith('-start'):
            await message.channel.send('(Vill påpeka att detta inte är min kod)Your journey has just started, young padawan. Which planet would you like to travel to. Write a for Tatooine, b for Coruscant, c for Hoth')
            count.insert(0, 1)
        if message.content.startswith('-a') and 1 == count[0] and "a" != count[1]:
            await message.channel.send("On your way to Tatooine you meet a star destroyer, you were lucky to escape but your ship has now a damadged hyperdrive. What do you want to do? Write a to send a distress signal, b to try to find some junk in space and repair the ship, c to to land on a ice planet nearby")
            count.insert(1, "a")
            continue
        if message.content.startswith("-a") and 1 == count[0] and "a" == count[1]:
            await message.channel.send("you sent your distress signal, a few days later an unknown ship appears out of hyperspace. What do you want to do?. Write a to heil them to tell them that they are welcome,b to heil them and tell them you are armed so don't come closer, c for turn of all systems in the ship aka play dead")
            continue
        if message.content.startswith("-b") and 1 == count[0] and "a" == count[1]:
            await message.channel.send("You are scotting the neighboring area and find an asteroid field and find some damaged ship you can scavenge some parts from, when you bring the junk in your ship you notice something moving. What do you do? write a to shot against where it moved, b for go and look what it was")
            continue
        if message.content.startswith("-c") and 1 == count[0] and "a" == count[1]:
            await message.channel.send("You landed on the ice planet and your scanners were broken so you couldn't search for life signs, What do you want to do? write a to go on the plains and look for a civilization, b to go to a creator where you can find perhaps find junk, c to go to a cave where you can find perhaps find some junk")
        if message.content.startswith("-reset"):
            count = ["","","","","","","","",""]
    print(count)
  
    

client.run('')#put your discord developer api token here