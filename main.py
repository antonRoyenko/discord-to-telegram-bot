from telegram import Bot, Update
from keys import *
import discord

dc = discord.Client()
tg = Bot(token=TELEGRAM_TOKEN)

@dc.event
async def on_message(message):
    try:
        serverName = message.guild.name
        channelName = message.channel.name
    except AttributeError:
        pass
    if message.channel.id in DISCORD_CHANNELS:
        toSend = f"{message.guild}/{message.channel}/{message.author.name}: {message.content}"
        print(toSend)
        tg.sendMessage(chat_id=TELEGRAM_CHAT_ID, text=toSend)

def main():
    try:
        print("Running, waiting for messages...")
        dc.run(DISCORD_TOKEN)
    except errors.HTTPException:
        print("Invalid discord token or network down!")
        quit()

if __name__ == '__main__':
    main()

