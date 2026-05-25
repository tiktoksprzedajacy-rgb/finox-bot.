import discord
import os
import asyncio
import random
from groq import Groq

# 1. ZMIENNE ŚRODOWISKOWE - nigdy nie trzymaj ich w pliku!
# W Railway dodaj te wartości w zakładce 'Variables'
TOKEN = os.environ.get("MTUwODMyODEyMDExNjE4MzEwMg.Gp5IHP.dUNCVgWoUHmttJoAauhSmhZfsss5jr1NrCnXrs")
GROQ_API_KEY = os.environ.get("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")

client = Groq(api_key=GROQ_API_KEY)
bot = discord.Client()

IGNORE_CHANNELS = [123456789012345678, 987654321098765432] 

@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user}. Tryb: Stealth/Aktywny.")

@bot.event
async def on_message(message):
    # Nie reaguj na siebie
    if message.author == bot.user:
        return
    
    # Nie reaguj na boty (dobre zabezpieczenie przed pętlami)
    if message.author.bot:
        return

    if message.channel.id in IGNORE_CHANNELS:
        return

    # Symulacja "czytania" - losowe opóźnienie przed podjęciem akcji
    await asyncio.sleep(random.uniform(3.0, 8.0))

    try:
        # Symulacja pisania - Discord pokazuje "użytkownik pisze..."
        async with message.channel.typing():
            # Dodatkowe opóźnienie zależne od długości odpowiedzi
            await asyncio.sleep(random.uniform(2.0, 5.0))
            
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "Jesteś naturalnym użytkownikiem. Odpowiadaj zwięźle, bez emotek botów, używaj poprawnej polszczyzny."},
                    {"role": "user", "content": message.content}
                ],
                model="llama-3.1-8b-instant",
            )
            
            reply = chat_completion.choices[0].message.content
            await message.channel.send(reply)
        
    except Exception as e:
        print(f"Błąd: {e}")
        # Jeśli Discord wyrzuci błąd, odczekaj dłużej (np. ban na API)
        await asyncio.sleep(60)

bot.run(TOKEN)
