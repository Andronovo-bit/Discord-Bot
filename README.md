
# Python Discord Bot

This is a simple Discord bot written in Python using the discord.py library. It can respond to commands, send messages, and perform other actions on Discord servers.

## Features

- Other: Other Commands: Other discord server commands.
	-  ping - get the latency of the bot
	- source - Get the source code of the bot
	- invite - invite the bot to your server
- Auto: The bot can commands will fire automatically.
	- on_ready -- Fires when the bot is ready.
	- on_member_join -- Fires when a member joins the server.
	- on_member_remove -- Fires when a member leaves the server.
	- on_command_error -- Fires when a command fails.
	- on_message_delete -- Fires when a message is deleted.
	- on_message_edit -- Fires when a message is edited.

- Fun: Fun Commands for Users
	 - slot - play a slot machine
	- reverse - reverse a string
	- flip - flip a coin
	- roll - roll a dice
	- 8ball - Ask a question
	- rps - Play rock paper scissors

## Installation

To install the bot, you need to have Python 3.9 or higher and pip installed on your system. You also need to create a Discord bot account and invite it to your server. You can follow the instructions [here](^1^) to do that.

Then, you need to clone this repository and install the dependencies using pip:

```bash
git clone https://github.com/Andronovo-bit/Discord-Bot.git
cd discord-bot
pip or pip3 install -r requirements.txt
```

Next, you need to create a file named `.env` in the root directory of the project and add your bot token as an environment variable:

```bash
TOKEN=your-bot-token
PREFIX=your-select-prefix (!,/,?)
INVITE_URL=your-bot-invite-url
```

Finally, you can run the bot using the following command:

```bash
python bot.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](^2^) file for more details.
