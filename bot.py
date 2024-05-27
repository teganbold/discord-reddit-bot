import discord
import responses
import os
import reddit
from dotenv import load_dotenv

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

async def send_post(message, user_message, is_private):
    try:
        subreddit = user_message[13:]
        print(subreddit)
        response = reddit.fetch_post(subreddit)
        await message.author(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

    
def run_discord_bot():
    load_dotenv()
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)
    
    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said {user_message} in {channel}")

        if user_message[:12] == "/bewb_reddit":
            await send_post(message, user_message, is_private=False)
    
    client.run(os.getenv("DISCORD_TOKEN"))