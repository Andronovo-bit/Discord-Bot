import discord


class MessageHelper:
    def __init__(self, bot, responded_users_per_channel, FORUM_CHANNEL_PARENT_IDS):
        self.bot = bot
        self.responded_users_per_channel = responded_users_per_channel
        self.FORUM_CHANNEL_PARENT_IDS = FORUM_CHANNEL_PARENT_IDS

    def is_first_message_in_channel(self, message: discord.Message) -> bool:
        """Check if the user has been responded to already in this channel."""
        return (
            self.responded_users_per_channel.get(message.channel.id) is None or
            message.author.id not in self.responded_users_per_channel[message.channel.id]
        )

    def add_user_to_responded(self, message: discord.Message):
        """Add user to the set for this specific channel if not already added."""
        if self.responded_users_per_channel.get(message.channel.id) is None:
            self.responded_users_per_channel[message.channel.id] = set()
        self.responded_users_per_channel[message.channel.id].add(message.author.id)

    def is_message_from_bot(self, message: discord.Message) -> bool:
        """Check if the message is sent by the bot."""
        return message.author == self.bot.user

    def is_message_in_forum_channel(self, message: discord.Message) -> bool:
        """Check if the message is in the specific forum channel."""
        return (message.channel.parent.type == discord.ChannelType.forum and 
                message.channel.parent_id in self.FORUM_CHANNEL_PARENT_IDS)
    
    async def is_bot_send_any_message(self, message: discord.Message) -> bool:
        """Check if the message is sent by the bot."""
        all_message_in_channel = message.channel.history(limit=100)
        results = [item async for item in all_message_in_channel]

        for msg in results:
            if msg.author == self.bot.user:
                return True
        return False