#https://github.com/CraftSpider/dpytest

# Import the modules
import discord
import discord.ext.commands as commands
from discord.ext.commands import Cog, command
import pytest
import pytest_asyncio
import discord.ext.test as dpytest


# Import the auto commands cog from the bot

class Misc(Cog):
    @command()
    async def ping(self, ctx):
        await ctx.send("Pong !")

    @command()
    async def echo(self, ctx, text: str):
        await ctx.send(text)

# Create a fixture for the bot and the cog
@pytest_asyncio.fixture
async def bot():
    # Create a bot instance with intents and prefix
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    # Add the auto commands cog to the bot
    await bot._async_setup_hook()  # setup the loop
    await bot.add_cog(Misc())

    # Configure the bot for testing with dpytest
    dpytest.configure(bot)

    # Return the config object
    yield bot

    # Teardown
    await dpytest.empty_queue() # empty the global message queue as test teardown



@pytest.mark.asyncio
async def test_ping(bot):
    await dpytest.message("!ping")
    assert dpytest.verify().message().content("Pong !")


@pytest.mark.asyncio
async def test_echo(bot):
    await dpytest.message("!echo Hello world")
    assert dpytest.verify().message().contains().content("Hello")

