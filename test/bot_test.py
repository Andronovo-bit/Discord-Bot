#https://github.com/CraftSpider/dpytest

# Import the modules
import discord
import discord.ext.commands as commands
from discord.ext.commands import Cog, command
import pytest
import pytest_asyncio
import discord.ext.test as dpytest
from discord.utils import get


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

@pytest.mark.asyncio
async def test_message(bot):
    """Test make_message_dict from factory.
    """
    guild = bot.guilds[0]
    author: discord.Member = guild.members[0]
    channel = guild.channels[0]
    attach: discord.Attachment = discord.Attachment(
        state=dpytest.back.get_state(),
        data=dpytest.back.facts.make_attachment_dict(
            "test.jpg",
            15112122,
            "https://media.discordapp.net/attachments/some_number/random_number/test.jpg",
            "https://media.discordapp.net/attachments/some_number/random_number/test.jpg",
            height=1000,
            width=1000,
            content_type="image/jpeg"
        )
    )
    message_dict = dpytest.back.facts.make_message_dict(channel, author, attachments=[attach])
    try:
        message: discord.Message = discord.Message(state=dpytest.back.get_state(), channel=channel, data=message_dict)  # noqa: E501,F841 (variable never used)
    except Exception as err:
        pytest.fail(str(err))
        
@pytest.mark.asyncio
async def test_add_reaction(bot):
    g = bot.guilds[0]
    c = g.text_channels[0]

    message = await c.send("Test Message")
    await message.add_reaction("😂")

    # This is d.py/discord's fault, the message object from send isn't the same as the one in the state
    message = await c.fetch_message(message.id)
    assert len(message.reactions) == 1
    
@pytest.mark.asyncio
async def test_get_channel(bot):
    guild = bot.guilds[0]
    channel_0 = guild.channels[0]

    channel_get = get(guild.channels, name=channel_0.name)

    assert channel_0 == channel_get


@pytest.mark.asyncio
async def test_get_channel_history(bot):
    guild = bot.guilds[0]
    channel_0 = guild.channels[0]

    channel_get = get(guild.channels, name=channel_0.name)

    assert channel_0 == channel_get

    test_message = await channel_get.send("Test Message")

    channel_history = [msg async for msg in channel_get.history(limit=10)]

    assert test_message in channel_history
    
@pytest.mark.asyncio
async def test_user_mention(bot):
    guild = bot.guilds[0]
    mes = await dpytest.message(f"<@{guild.me.id}>")

    assert len(mes.mentions) == 1
    assert mes.mentions[0] == guild.me

    mes = await dpytest.message("Not a mention in sight")

    assert len(mes.mentions) == 0