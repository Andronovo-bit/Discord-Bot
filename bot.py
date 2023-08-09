import asyncio
from termcolor import colored
import discord
from discord.ext import commands
from pathlib import Path
from utils.utils import load_env, get_token, get_prefix
from utils.utils import configure_logging, get_logger


load_env()
TOKEN = get_token()
PREFIX = get_prefix()

intents = discord.Intents.all()
intents.members = True
root_dir = Path(__file__).parent
configure_logging(root_dir)
logger = get_logger(__name__)


# Define a class for the bot
class AndronovoBot(commands.Bot):
    """Andronovo - Open Source Discord Bot.

    Github: Andronovo-bit
    Developer: Seyyid Yiğit
    Contact Email: seyyid364@gmail.com
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
    description="""Andronovo - Open Source Discord Bot.
                    Github:-  Andronovo-bit
                    Developer:  Seyyid Yiğit
                    Contact Email:- seyyid364@gmail.com""",
)

# Run the bot using asyncio
if __name__ == "__main__":
    asyncio.run(bot.run_bot())
