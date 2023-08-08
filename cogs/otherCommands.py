from discord.ext import commands
import discord

from utils.utils import create_embed
from utils.utils import load_env, get_invite_link

load_env()
INVITE_URL = get_invite_link()

class OtherCommands(commands.Cog, name="Other Commands for Users : Other Commands"):
    """
        Other Commands: Other discord server commands

    Commands:
        - ping - get the latency of the bot
        - source - Get the source code of the bot
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["hi", "hello", "pong"], help="Get the ping of the bot")
    async def ping(self, ctx):
        """
            Get the ping of the bot

        command: !ping

        **Usage**
            get the latency of the bot
        """
        embed = create_embed(ctx, title="Pong", description="🏓", color=discord.Color.green())
        embed.add_field(name="Ping", value="{} ms".format(round(self.bot.latency * 1000)))
        embed.add_field(name="Status", value={"online": "🟢", "idle": "🟡", "dnd": "🔴", "offline": "⚫"}[str(ctx.author.status)])
        embed.add_field(name="User", value=ctx.author.mention)
        embed.set_thumbnail(url="https://i.pinimg.com/originals/0c/67/5a/0c675a8e1061478d2b7b21b330093444.gif")
        embed.set_footer(text="Andronovo | !help")
        await ctx.send("Hi, I am AndronovoBot, a bot made by Andronovo-bit")
        await ctx.send(embed=embed)

    @commands.command(aliases=["github", "source_code"], help="get the source code")
    async def source(self, ctx):
        """ get the bot source code

        command: !source

        **Usage**:
            `source`: Get the bot source code
        """
        try:
            source_url = "https://github.com/EvilMindDevs/hms-unity-plugin"
            await ctx.send("The bot is powered by **Huawei Mobile Services**\n\n**Source Code**: {}\n\nDon't forget to star the repo if you like it!".format(source_url))
        except Exception as e:
            await ctx.send('```{} - {}```'.format(type(e).__name__, e))
    
    @commands.command(aliases=["invite"], help="invite the bot to your server")
    async def invite_bot(self, ctx):
        """ invite the bot to your server

        command: !invite

        **Usage**:
            `invite`: invite the bot to your server
        """
        try:
            invite_url = INVITE_URL
            await ctx.send("Invite me to your server: {}".format(invite_url))
        except Exception as e:
            await ctx.send('```{} - {}```'.format(type(e).__name__, e))



async def setup(bot: commands.Cog):
    await bot.add_cog(OtherCommands(bot))
