from sre_constants import IN
from utils.utils import EnvVar, load_env, get_env_var

# Load environment variables from .env file
load_env()

# Bot related environment variables
TOKEN = get_env_var(EnvVar.TOKEN)
PREFIX = get_env_var(EnvVar.PREFIX)
BOT_NAME = get_env_var(EnvVar.BOT_NAME)
INVITE_URL = get_env_var(EnvVar.INVITE_URL)

# Project related environment variables
PROJECT_LINK = get_env_var(EnvVar.PROJECT_LINK)
AUTHOR_NAME = get_env_var(EnvVar.AUTHOR_NAME)

# Developer related environment variables
DEVELOPER_NAME = get_env_var(EnvVar.DEVELOPER_NAME)
CONTACT_EMAIL = get_env_var(EnvVar.CONTACT_EMAIL)

