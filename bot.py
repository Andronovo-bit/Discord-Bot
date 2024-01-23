import asyncio
from termcolor import colored
import discord
from discord.ext import commands
from pathlib import Path
from utils.utils import configure_logging, get_logger
from utils import load_enviroments

BOT_NAME = load_enviroments.BOT_NAME
PREFIX = load_enviroments.PREFIX
AUTHOR_NAME = load_enviroments.AUTHOR_NAME
TOKEN = load_enviroments.TOKEN
DEVELOPER_NAME = load_enviroments.DEVELOPER_NAME
CONTACT_EMAIL = load_enviroments.CONTACT_EMAIL

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
            "Auto Commands": "cogs.auto_commands",
            "Fun Commands": "cogs.fun_commands",
            "Other Commands": "cogs.other_commands",
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