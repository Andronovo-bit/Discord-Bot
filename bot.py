import asyncio
from termcolor import colored
import discord
from discord.ext import commands
from pathlib import Path
from utils.utils import configure_logging, get_logger
from utils import loadEnviroments

BOT_NAME = loadEnviroments.BOT_NAME
PREFIX = loadEnviroments.PREFIX
AUTHOR_NAME = loadEnviroments.AUTHOR_NAME
TOKEN = loadEnviroments.TOKEN
DEVELOPER_NAME = loadEnviroments.DEVELOPER_NAME
CONTACT_EMAIL = loadEnviroments.CONTACT_EMAIL

intents = discord.Intents.all()
intents.members = True
root_dir = Path(__file__).parent
configure_logging(root_dir)
logger = get_logger(__name__)


# Define a class for the bot
class AndronovoBot(commands.Bot):
    f"""{BOT_NAME} - Open Source Discord Bot.

    Github: {AUTHOR_NAME}
    Developer: {DEVELOPER_NAME}
    Contact Email: {CONTACT_EMAIL}
    """

    def __init__(self, prefix: str, intents: discord.Intents, description: str) -> None:
        super().__init__(
            command_prefix=prefix,
            intents=intents,
            case_insensitive=True,
            description=description,
        )
        self.cog_dict = {
            "Auto Commands": "cogs.autoCommands",
            "Fun Commands": "cogs.funCommands",
            "Other Commands": "cogs.otherCommands",
        }

    async def load_cogs(self) -> None:
        """Load cogs using dictionary."""
        try:
            for key, value in self.cog_dict.items():
                logger.info(f"Loading {key} {value}")
                await self.load_extension(value)
        except Exception as e:
            print(colored(f"Error while loading cogs: {e}", "red"))
            logger.error(f"{type(e).__name__} - {e}")

    async def run_bot(self) -> None:
        """Run the bot using the token."""
        try:
            await self.load_cogs()
            logger.info(msg="Starting Bot...")
            await self.start(TOKEN)
        except Exception as e:
            logger.error(f"Error while running bot: {e}")


# Create an instance of the bot class
bot = AndronovoBot(
    prefix=PREFIX,
    intents=intents,
    description=f"""{BOT_NAME} - Open Source Discord Bot.
                    Github:-  {AUTHOR_NAME}
                    Developer:  {DEVELOPER_NAME}
                    Contact Email:- {CONTACT_EMAIL}""",
)

# Run the bot using asyncio
if __name__ == "__main__":
    asyncio.run(bot.run_bot())