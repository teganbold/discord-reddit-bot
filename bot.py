import discord
from discord.ext import commands
import os
import reddit_post
from dotenv import load_dotenv


def run_discord_bot():
    load_dotenv()
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print("Bot is now running!")

    @bot.command()
    async def reddit(ctx, arg):
        response = reddit_post.fetch_post(arg)
        await ctx.send(response)
    
    bot.run(os.getenv("DISCORD_TOKEN"))