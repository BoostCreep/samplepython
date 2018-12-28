import discord

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Bite my shiny,metal ass! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
	
		

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Hey {0.mention} welcome to {1.name}Wanna Kill all humans?'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NTIzNTMyMDM4NDIzNDQ1NTE1.Dva-Uw.-gK6nb2FVOslTHFcWNnb9CjQpCw')