import os

import telegram
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_USER = os.getenv('TELEGRAM_USER')


def check_tokens():
    """Check the availability of environment variables."""

    return all([TELEGRAM_TOKEN, TELEGRAM_USER])


async def send_message(message):
    """Send message to Telegram user"""

    if check_tokens():
        async with telegram.Bot(token=TELEGRAM_TOKEN) as bot:
            await bot.send_message(TELEGRAM_USER, message)
