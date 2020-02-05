import discord 
from discord.ext import commands
from discord.utils import get

tt = os.environ.get("TOKEN")

client = commands.Bot(command_prefix = "K!")
client.remove_command("help")

@client.event
async def on_message(message):
    if message.author.id == 453811092389494785:
        if ":" in message.content:
            await message.channel.purge(limit=1)
    await client.process_commands(message)

client.run(tt)