import discord
import asyncio
import random

TOKEN = 'BOT_TOKEN' #Enter Bot token
Serverid = 1234567890 #Enter server id
Rainbowrolename = "ROLE_NAME" #Enter Role name
delay = 3 #Seconds Brfore the role change color

#List of Colors for the role
client = discord.Client()
colours = [
    discord.Color.dark_orange(),
    discord.Color.orange(),
    discord.Color.dark_gold(),
    discord.Color.gold(),
    discord.Color.dark_magenta(),
    discord.Color.magenta(),
    discord.Color.red(),
    discord.Color.dark_red(),
    discord.Color.blue(),
    discord.Color.dark_blue(),
    discord.Color.teal(),
    discord.Color.dark_teal(),
    discord.Color.green(),
    discord.Color.dark_green(),
    discord.Color.purple(),
    discord.Color.dark_purple()
]

async def rainbow(role):
    for role in client.get_guild(Serverid).roles:
        if str(role) == str(Rainbowrolename):
            print("Detected role")
            while not client.is_closed():
                try:
                    await role.edit(color=random.choice(colours))
                except Exception:
                    print("Can't edit role, Make sure that the role is above all of the roles")
                    pass
                await asyncio.sleep(delay)
    print('The role  "' + Rainbowrolename +'" is invalid')
    try:
        await client.get_guild(Serverid).create_role(reason="Created rainbow role", name=Rainbowrolename)
        print("role created!")
        await asyncio.sleep(2)
        client.loop.create_task(rainbow(Rainbowrolename))
    except Exception as e:
        print("couldn't create the role. Make sure the bot have the perms to edit roles")
        print(e)
        pass
        await asyncio.sleep(10)
        client.loop.create_task(rainbow(Rainbowrolename))

@client.event
async def on_ready():
    client.loop.create_task(rainbow(Rainbowrolename))

client.run(TOKEN)