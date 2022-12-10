from discord.ext import commands

TOKEN ="MTAwNTI0Mjk2NDMxMTgwNjAwMg.GPrAYL.KpmC0HUMgdKjKNKElXTLiI8TytXNeAuD24jUbQ "

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user: 
        return
    
    if message.content == 'saif 9a7ba':
        await message.channel.send("ey saif 9a7ba")
    if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author}')

    await bot.process_commands(message)

bot.run(TOKEN)