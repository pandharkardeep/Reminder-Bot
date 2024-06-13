import discord
import requests
import datetime
import asyncio
import os

# Replace with your actual API key and bot token
CLIST_API_KEY = os.getenv('CLIST_API_KEY')
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID'))  # Replace with your Discord server ID
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))  # Replace with the channel ID where you want to send reminders

client = discord.Client(intents=discord.Intents.default())

def get_upcoming_codeforces_contests():
    url = 'https://clist.by/api/v1/contest/'
    params = {
        'resource__name': 'codeforces.com',
        'start__gt': datetime.datetime.now().isoformat(),
        'order_by': 'start',
        'limit': 5
    }
    headers = {
        'Authorization': f'ApiKey {CLIST_API_KEY}'
    }
    response = requests.get(url, params=params, headers=headers)
    return response.json().get('objects', [])

async def send_contest_reminders():
    await client.wait_until_ready()
    channel = client.get_channel(int(CHANNEL_ID))
    while True:
        contests = get_upcoming_codeforces_contests()
        if contests:
            for contest in contests:
                start_time = datetime.datetime.fromisoformat(contest['start'])
                time_until_start = (start_time - datetime.datetime.now()).total_seconds()
                if 0 < time_until_start < 3600:  # If the contest starts in less than an hour
                    await channel.send(
                        f"Reminder: The Codeforces contest **{contest['event']}** starts at {start_time} UTC!"
                    )
        await asyncio.sleep(3600)  # Check every hour

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

client.loop.create_task(send_contest_reminders())
client.run(DISCORD_BOT_TOKEN)
