import discord
import os
from dotenv import load_dotenv
import logging
from pathlib import Path
from enum import Enum


class EnvVar(Enum):
    TOKEN = "TOKEN"
    PREFIX = "PREFIX"
    INVITE_URL = "INVITE_URL"
    BOT_NAME = "BOT_NAME"
    AUTHOR_NAME = "AUTHOR_NAME"
    PROJECT_LINK = "PROJECT_LINK"
    DEVELOPER_NAME = "DEVELOPER_NAME"
    CONTACT_EMAIL = "DEVELOPER_EMAIL"


def load_env() -> None:
    """Load environment variables from .env file."""
    load_dotenv()
    # You can also add some validation or error handling here
    # For example, raise an exception if TOKEN or PREFIX is missing
    # Or use some default values if they are not provided


def get_env_var(var: EnvVar) -> str:
    """Get the specified environment variable."""
    return os.getenv(var.value)


def create_embed(ctx=None, title=None, description="", color=None):
    """Create an embed with the given title, description and color

    Args:
        title (str): The title of the embed
        description (str): The description of the embed
        color (int): The color of the embed

    Returns:
        embed (discord.Embed): The embed created
    """
    embed = discord.Embed(title=title, description=description, color=color)
    embed.set_thumbnail(
        url="https://i.pinimg.com/originals/0c/67/5a/0c675a8e1061478d2b7b21b330093444.gif"
    )
    if ctx is not None:
        embed.set_author(name=ctx.author.name)
    return embed


def configure_logging(root_dir: Path) -> None:
    """Configure logging for the bot."""

    logging.basicConfig(
        format="%(levelname)s - %(asctime)s - %(name)s - %(message)s",
        encoding="utf-8",
        datefmt="%d/%m/%Y %I:%M:%S %p",
        handlers=[
            logging.FileHandler(root_dir / "logs" / "bot.log"),
            logging.StreamHandler(),
            logging.NullHandler(),
        ],
        level=logging.INFO,
    )


def get_logger(name: str) -> logging.Logger:
    """Get a logger with the given name."""
    return logging.getLogger(name)