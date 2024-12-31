# CrousBot

CrousBot is a Discord bot designed to fetch information about Crous residences in the "Ile-de-France" region and send the available ones to a specified Discord channel. It helps users stay updated on available housing options effortlessly.

## Features

- Fetches Crous residence information in "Ile-de-France."
- Sends available residences to a Discord channel.
- Easy to set up and use.

## Prerequisites

- Python 3.8 or higher installed on your system.
- A Discord bot token. You can get one by creating a bot on the [Discord Developer Portal](https://discord.com/developers/applications).
- `main.py` script implemented and ready to use.

## Installation and Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/CrousBot.git
   cd CrousBot
   ```

2. **Install required dependencies**
   Use `pip` to install the required libraries. Ensure you have a `requirements.txt` file with the necessary dependencies (e.g., `discord.py`).
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment**
   - Create a `.env` file in the project root directory.
   - Add your Discord bot token to the `.env` file:
     ```env
     DISCORD_TOKEN=your_discord_bot_token
     ```

4. **Run the bot**
   Execute the `main.py` script to start the bot:
   ```bash
   python main.py
   ```

5. **Invite the bot to your server**
   - Go to the Discord Developer Portal and navigate to your bot application.
   - Under the "OAuth2" tab, generate an invite link by selecting the required bot permissions.
   - Use the link to invite the bot to your Discord server.

6. **Set the target channel**
   Ensure the bot has permissions to post messages in the desired Discord channel. Update the channel ID in the `main.py` script or configuration file if required.

## Usage

Once the bot is running, it will automatically fetch and send updates about available Crous residences in the "Ile-de-France" region to the configured Discord channel. You can customize the fetching logic or add additional features as needed.

---

Thank you for using CrousBot! Feel free to contribute or report any issues on the GitHub repository.
