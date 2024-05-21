import discord
from DiscordToken import token  
import httpx

url = 'http://localhost:8000/postmessage/'

class DiscordScraper(discord.Client):
   
    async def on_ready(self):
        print('CoinBot in the house!')
    
    async def on_message(self, message):
        raw_message = {"message": [(str(message.content))]} #(str(message.author), str(message.content)) 

        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=raw_message)
            return response.json()
       
        

intents = discord.Intents.default()
intents.messages = True

intents.message_content = True  

client = DiscordScraper(intents=intents)
client.run(token)
 