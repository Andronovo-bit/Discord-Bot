from discord.ext import commands
import discord
from utils.utils import create_embed

import random


class FunCommands(commands.Cog, name="Fun Commands for Users : Fun Commands"):
    """ Fun Commands

    commands:
        - slot - play a slot machine
        - reverse - reverse a string
        - flip - flip a coin
        - roll - roll a dice
    """

    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(aliases=["slots", "bet"], help="play slots")
    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.user)
    async def slot(self, ctx):
        """ Play a slot machine

        command: !slot

        **Usage**:
            `slot`: Play a slot machine
        """
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        # embed = discord.Embed(title="Slot Machine", color=discord.Color.blue())
        embed = create_embed(ctx, title="Slot Machine", color=discord.Color.blue())
        embed.add_field(name="**Result**", value=f"{a} {b} {c}", inline=False)
        await ctx.send(embed=embed)

    @commands.command(help="reverse the text")
    async def reverse(self, ctx, *text):
        """ Reverse the text

        command: !reverse <text>

        **Usage**:
            `reverse`: Reverse the text
        """
        text = " ".join(text)
        try:
            await ctx.send(text[::-1])
        except Exception as e:
            await ctx.send('**`ERROR:`** {} - {}'.format(type(e).__name__, e))

    @commands.command(aliases=["flip", "flipcoin", "coinflip"], help="Flip a coin")
    async def flip_the_coin(self, ctx):
        """ Flip the coin randomly

        command: !flipcoin

        **Usage**:
            `flipcoin`: Flip the coin randomly
        """
        coinsides = ["Heads", "Tails"]
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")

    @commands.command(aliases=["dice", "roll"], help="Roll a dice")
    async def roll_the_dice(self, ctx, dice: str):
        """Rolls a dice in NdN format.

        command: !dice NdN

        **Usage**:
            `dice`: Roll a dice in NdN format

        number of rolls-d-number of limit

        input: 6d5
        output example: 2, 1, 4, 3, 5
        """
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            return 'Format has to be in NdN!'

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        embed = self.create_embed(ctx, title="Dice Rolled", description=f"{ctx.author.mention} rolled dice(1 -{limit}) {rolls} times", color=0x00ff00)
        embed.add_field(name="Result", value=result, inline=False)
        await ctx.send(embed=embed)
    
    @commands.command(aliases=["8ball"], help="Ask a question")
    async def ask(self, ctx, *, question):
        """Ask a question

        command: !ask <question>

        **Usage**:
            `ask`: Ask a question
        """
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now...",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no...",
            "Outlook not so good...",
            "Very doubtful.",
        ]
        embed = discord.Embed(title="8ball", description=f"Question: {question}\nAnswer: {random.choice(responses)}", color=discord.Color.blue())
        await ctx.send(embed=embed)
        
    @commands.command(aliases=["rps"], help="Play rock paper scissors")
    async def rockpaperscissors(self, ctx, *, choice):
        """Play rock paper scissors

        command: !rps <choice>

        **Usage**:
            `rps`: Play rock paper scissors

        choice: rock, paper, scissors
        """
        choices = ["rock", "paper", "scissors"]
        if choice.lower() not in choices:
            await ctx.send(f"**{ctx.author.name}**, your choice must be one of these: `rock`, `paper`, `scissors`")
        else:
            bot_choice = random.choice(choices)
            if choice.lower() == bot_choice:
                await ctx.send(f"**{ctx.author.name}**, it's a tie! We both chose **{bot_choice}**.")
            elif choice.lower() == "rock":
                if bot_choice == "paper":
                    await ctx.send(f"**{ctx.author.name}**, I chose **{bot_choice}** and won!")
                else:
                    await ctx.send(f"**{ctx.author.name}**, I chose **{bot_choice}** and lost!")
            elif choice.lower() == "paper":
                if bot_choice == "scissors":
                    await ctx.send(f"**{ctx.author.name}**, I chose **{bot_choice}** and won!")
                else:
                    await ctx.send(f"**{ctx.author.name}**, I chose **{bot_choice}** and lost!")
            elif choice.lower() == "scissors":
                if bot_choice == "rock":
                    await ctx.send(f"**{ctx.author.name}**, I chose **{bot_choice}** and won!")
                else:
                    await ctx.send(f"**{ctx.author.name}**, I chose **{bot_choice}** and lost!")


async def setup(bot: commands.Bot):
    await bot.add_cog(FunCommands(bot))
