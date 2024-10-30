import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv("Token")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

#remove default help command
bot.remove_command("help")

@bot.event
async def on_ready():
    print("The bot is now ready")
    print("----------------")


async def load_extensions():
    await bot.load_extension("cogs.recruitment_cog")
    await bot.load_extension("cogs.help_cog")

async def main():
    await load_extensions()
    await bot.start(TOKEN)

if TOKEN:
    asyncio.run(main())
else:
    print("Error: DISCORD_TOKEN is not set in .env file.")
