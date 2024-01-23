import discord
from discord.ext import commands
import logging
import utils.load_enviroments as load_enviroments
from utils.message_helper import MessageHelper
from utils.utils import create_embed

class AutoCommands(commands.Cog, name="Auto Commands"):
    """ These commands will fire automatically.

    Arguments:
        bot {discord.Cog} -- The bot object.

    Commands:
        on_ready -- Fires when the bot is ready.
        on_member_join -- Fires when a member joins the server.
        on_member_remove -- Fires when a member leaves the server.
        on_command_error -- Fires when a command fails.
        on_message_delete -- Fires when a message is deleted.
        on_message_edit -- Fires when a message is edited.
        on_command_error -- Fires when a command fails.
    """
    FORUM_CHANNEL_PARENT_IDS = [1198883785496875068] # List of forum channel IDs
    FORUM_CHANNEL_IDS:list[int] = [] # List of channel IDs in the forum category
    ADMIN_ID = [460870992131260416] # List of Admin or Mod IDs
    DOCS_WEBSITE = 'https://evilminddevs.gitbook.io/hms-unity-plugin_/support/faq'
    BOT_NAME = load_enviroments.BOT_NAME
   
    def __init__(self, bot):
        """ Init function for AutoCommands."""
        self.bot = bot        
        # Replace YOUR_FORUM_CHANNEL_IDS with the actual Discord channel IDs you want to monitor
        self.responded_users_per_channel = {channel_id: set() for channel_id in self.FORUM_CHANNEL_IDS}
        # Create a helper object
        self.helper = MessageHelper(bot, self.responded_users_per_channel, self.FORUM_CHANNEL_PARENT_IDS)
    
    @commands.Cog.listener()
    async def on_ready(self):
        """ This will run when the bot is ready. """
        activity = discord.Activity(type=discord.ActivityType.watching, name=f"{self.BOT_NAME} | !help")
        await self.bot.change_presence(activity=activity)
        logging.info(f'{self.bot.user.name} is Online...')

    @commands.Cog.listener()
    async def on_member_join(self: commands.Cog, member: discord.Member):
        """ This will fire when a new member joins the server."""
        channel = member.guild.system_channel
        if channel is not None:
            embed = create_embed(
                title="Welcome",
                description=f"Welcome {member.mention}, Introduce yourself to the community.\n"
                            f"Use `!help` command to get started."
            )
            await channel.send(embed=embed)
            logging.info(f'{member} joined the server')
            if self.bot_check(member):
                return
            await member.send("Welcome to the Server! Introduce yourself in the server.\n"
                              "Use `!help` command to get started.")

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        """ This event triggers when a member leaves the server."""
        channel = member.guild.system_channel
        if channel is not None:
            embed = create_embed(
                title="Good Bye",
                description=f"{member} has left the server."
            )
            await channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """ This event triggers when a command fails."""
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not found.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing required argument.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to use this command.")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I don't have permission to do that.")
        elif isinstance(error, commands.NotOwner):
            await ctx.send("You are not the owner of this bot.")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("You don't have permission to use this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Bad argument.")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"Command on cooldown. Try again in {error.retry_after:.2f}s.")
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send("This command cannot be used in private messages.")
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send("This command is disabled and cannot be used.")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send("Error while invoking command.")
        elif isinstance(error, commands.TooManyArguments):
            await ctx.send("Too many arguments.")
        elif isinstance(error, commands.UserInputError):
            await ctx.send("User input error.")
        elif isinstance(error, commands.CommandError):
            await ctx.send("Command error.")
        else:
            await ctx.send("Unknown error.")
        logging.error(f"{error} - {ctx.author} - {ctx.guild}")
    
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        """ This event triggers when a message is sent on forum channel."""        
        if (
            self.helper.is_message_in_forum_channel(message) and 
            self.helper.is_first_message_in_channel(message) and 
            not await self.helper.is_bot_send_any_message(message)
        ):
            self.helper.add_user_to_responded(message)
            await self.handle_forum_message(message)


    # Helper functions

    async def handle_forum_message(self, message: discord.Message):
        """Handle the message sent in the forum channel."""
        print(message.content)
        await message.add_reaction('👍')
        await self.send_response_message(message)
        await self.notify_admin(message)

    async def send_response_message(self, message: discord.Message):
        """Send a response message to the user."""
        response = (
            f'Thank you for raising this issue. We will reply as soon as possible. '
            f'In the mean time you are waiting, you can review our FAQ page: '
            f'<{self.DOCS_WEBSITE}>'
        )
        await message.channel.send(response)

    async def notify_admin(self, message: discord.Message):
        """Notify the admin about the new message."""
        try:
            notifications = ' '.join(f'<@{admin_id}>' for admin_id in self.ADMIN_ID)
            await message.channel.send(notifications)
        except Exception as e:
            print(e)
            logging.error(f"{type(e).__name__} - {e}")

async def setup(bot: commands.Cog):
    await bot.add_cog(AutoCommands(bot))