import discord
from discord.ext import commands
import logging

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

    def __init__(self, bot):
        """ Init function for AutoCommands."""
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        """ This will run when the bot is ready. """
        activity = discord.Activity(type=discord.ActivityType.watching, name="Andronovo | !help")
        await self.bot.change_presence(activity=activity)
        logging.info(f'{self.bot.user.name} is Online...')

    @commands.Cog.listener()
    async def on_member_join(self: commands.Cog, member: discord.Member):
        """ This will fire when a new member joins the server."""
        channel = member.guild.system_channel
        if channel is not None:
            embed = create_embed(title="Welcome", description=f"welcome {member.mention}, Introduce yourself to community.")
            await channel.send(embed=embed)
            logging.info(f'{member} joined the server')
            if self.bot_check(member):
                return
            await member.send("welcome to the Server! introduce yourself in server.\nUse `!help` command to get started.")

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        """ This event triggers when a member leaves the server."""
        channel = member.guild.system_channel
        if channel is not None:
            embed = create_embed(title="Good Bye", description=f"{member} has left the server.")
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



async def setup(bot: commands.Cog):
    await bot.add_cog(AutoCommands(bot))