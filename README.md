# Python Discord Bot

Welcome to the Python Discord Bot repository! This bot is crafted with the `discord.py` library and is ready to enhance your Discord server with a variety of commands and automated features.

## Features Overview

### General Commands
- `ping`: Check the bot's response latency.
- `source`: Retrieve the bot's source code.
- `invite`: Generate an invitation link to add the bot to other servers.

### Automation Commands
- `on_ready`: Triggered when the bot is fully operational.
- `on_member_join`: Activated upon a new member joining the server.
- `on_member_remove`: Engaged when a member departs from the server.
- `on_command_error`: Executed when a command encounters an error.
- `on_message`: Responds to messages in the forum channel.

### Fun Commands
- `slot`: Engage with a virtual slot machine.
- `reverse`: Reverse the characters in a string.
- `flip`: Simulate a coin toss.
- `roll`: Roll a virtual dice.
- `8ball`: Receive answers to your questions.
- `rps`: Play rock-paper-scissors.

## Getting Started

### Prerequisites
Ensure you have Python 3.9+ and pip available on your system. Set up a Discord bot account and invite it to your server following these [instructions](https://discord.com/developers/applications).

### Installation Without Virtual Environment
```bash
git clone https://github.com/Andronovo-bit/Discord-Bot.git
cd Discord-Bot
pip install -r requirements.txt
```

### Installation With Virtual Environment
```bash
git clone https://github.com/Andronovo-bit/Discord-Bot.git
cd Discord-Bot
python -m venv botenv
# Windows cmd.exe
botenv\Scripts\activate
# Windows PowerShell
botenv\Scripts\Activate.ps1
# macOS & Linux
source botenv/bin/activate

pip install -r requirements.txt
```

### Configuration
Create a `.env` file in the project root with the following content, replacing placeholders with your actual data:
```bash
TOKEN=your-bot-token
PREFIX=your-desired-prefix (!,/,?)
INVITE_URL=your-bot-invite-url
BOT_NAME=your-bot-name (ex: SuperDuperBot)
AUTHOR_NAME=your-name-or-company (ex: FireCamp)
PROJECT_LINK=your-project-link
DEVELOPER_NAME=your-name-or-company-name
CONTACT_EMAIL=your-contact-email
```

### Running the Bot
Execute the bot with:
```bash
python bot.py
```

Certainly! Below is an updated version of the README file with the added sections for test scenarios and instructions on how to run tests using `pytest`, `pytest_asyncio`, and `dpytest`.

## Testing

### Test Scenarios

- `test_ping`: Validates the `ping` command's response time.
- `test_echo`: Ensures the `echo` command returns the expected message.
- `test_messages`: Checks if sending messages with attachments works correctly.
- `test_add_reaction`: Tests the bot's ability to add reactions to messages.
- `test_get_channel`: Confirms that the bot can retrieve channel information accurately.
- `test_get_channel_history`: Verifies that fetching channel history is functioning as intended.
- `test_user_mention`: Tests the bot's response to user mentions.

### Test Environment Setup

Before running tests, ensure you have installed all necessary testing libraries:

```bash
pip install pytest pytest_asyncio dpytest
```

We have created fixtures for both the bot and the cog to facilitate our testing environment. These fixtures help us simulate bot and cog instances for accurate testing.

### Running Tests

To execute your tests, navigate to your project directory and run:

```bash
pytest
```

This command will automatically discover and run all test files in your project that follow the `test_*.py` naming pattern.

For asynchronous test cases, make sure to use the `@pytest.mark.asyncio` decorator before your async test functions. This allows `pytest_asyncio` to handle the event loop for you.

### Example Test Case

Here's an example of a simple test case using `dpytest`:

```python
import discord.ext.test as dpytest
import pytest

@pytest.mark.asyncio
async def test_ping(bot):
    await dpytest.message("!ping")
    assert dpytest.verify().message().contains().content("Pong!")
```

Replace `bot` with your actual bot fixture name. The above test simulates sending a `!ping` command and verifies that the bot responds with `Pong!`.


## License

This bot is released under the MIT License. For more information, refer to the [LICENSE](LICENSE) file.
