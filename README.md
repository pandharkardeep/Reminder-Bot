# Discord Bot for Codeforces Contest Reminders

This Discord bot sends reminders about upcoming Codeforces contests to a specified channel. The bot uses the Clist API to fetch contest details.

## Features

- Periodically checks for upcoming Codeforces contests.
- Sends a reminder to a specified Discord channel if a contest is starting within the next hour.

## Prerequisites

- Python 3.10 or later
- Docker (for deployment)
- A Clist API key. You can find it [here](https://clist.by/api/v1/doc/) after creating an account.
- A Discord bot token. You can find it [here](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)
- The ID of the Discord channel where you want to send reminders

## Setup

### Local Development
#### Follow these steps to run the bot locally on your own pc
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/Reminder-Bot.git
   cd Reminder-Bot
   ```
2. **Install the Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set up the Environment Variables:**
   Create a .env file in the project root and add the following:
   ```env
   CLIST_API_KEY=your_clist_api_key
   DISCORD_BOT_TOKEN=your_discord_bot_token
   CHANNEL_ID=your_discord_channel_id
   ```
4. **Run the Bot:**
   ```sh
   python bot.py
   ```

### Deployment on a cloud service
The Dockerfile will take care of everything, just give all the files and define the environment variables. 
