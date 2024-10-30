import discord 
import requests
from bs4 import BeautifulSoup
import asyncio

DISCORD_TOKEN = 'MTMwMTE4NzY3Njk1MDc2MTYzMg.GpVam1.2daK3WkTxkXU2gLVRPNJS1qpOqR7m2Q3snXs9w'  # Replace with your actual Discord token
CHANNEL_ID = 1301282765597315073  # Replace with the channel ID where you want to post messages
URL_TO_CHECK = 'https://trouverunlogement.lescrous.fr/tools/36/search?bounds=1.4462445_49.241431_3.5592208_48.1201456'  # URL of the logement listings page

# Initialize bot client
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Set to store previously detected logements
previous_logements = set()

def fetch_logements():
    """Scrapes the logements from the website."""
    
    # Send the GET request
    response = requests.get(URL_TO_CHECK)
    
    print(f"Response status code: {response.status_code}")  # Debugging line
    if response.status_code != 200:
        print(f"Failed to retrieve the website data. Status Code: {response.status_code}")
        return None
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    logement_data = []
    
    # Find all the accommodation cards
    for card in soup.select('.fr-card'):
        # Extract title and link
        title_tag = card.select_one('.fr-card__title a')
        title = title_tag.text.strip() if title_tag else "No title available"
        link = title_tag['href'] if title_tag else "No link available"
        
        # Extract description
        description_tag = card.select_one('.fr-card__desc')
        description = description_tag.text.strip() if description_tag else "No description available"
        
        # Extract price
        price_tag = card.select_one('.fr-badge')
        price = price_tag.text.strip() if price_tag else "Price not listed"
        
        # Extract size
        size_tag = card.select_one('.fr-card__detail')
        size = size_tag.text.strip() if size_tag else "Size not listed"
        
        # Extract beds
        beds_tag = card.select_one('.fr-card__detail.fr-icon-group-fill')
        beds = beds_tag.text.strip() if beds_tag else "Beds not listed"

        logement_data.append((title, description, price, size, beds, link))
    
    return logement_data

async def check_for_new_logements():
    """Checks for new logements and sends notification if found."""
    global previous_logements
    current_logements = fetch_logements()
    
    if current_logements:
        # Convert list to a set of tuples for comparison
        current_logements_set = set(current_logements)
        new_logements = current_logements_set - previous_logements
        
        if new_logements:
            await send_notification(new_logements)
        
        # Update previous logements
        previous_logements = current_logements_set

async def send_notification(new_logements):
    """Sends a message to the Discord channel with each new logement."""
    channel = client.get_channel(CHANNEL_ID)
    
    # Base URL to prepend to the accommodation links
    base_url = 'https://trouverunlogement.lescrous.fr'
    
    for title, description, price, size, beds, link in new_logements:
        # Create a full link
        full_link = base_url + link
        
        # Format the message with the title as a clickable link
        message = (f"[**{title}**]({full_link})\n"  # Title as a clickable link
                   f"{description}\n"
                   f"Price: {price}\n"
                   f"Size: {size}\n"
                   f"Beds: {beds}\n")
        
        await channel.send(message)
        print(f"Notification sent to Discord channel for: {title}")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # Run the logement check every 5 minutes
    while True:
        await check_for_new_logements()
        await asyncio.sleep(300)  # Wait 5 minutes

# Run the bot
client.run(DISCORD_TOKEN)
