import os
import discord
import asyncio
import random
import logging
from groq import Groq

# Konfiguracja logowania
logging.basicConfig(level=logging.INFO)

# Pobieranie zmiennych środowiskowych
# Uwaga: Używamy nazwy klucza z Railway (DISCORD_TOKEN)
TOKEN = os.environ.get("MTUwODMyODEyMDExNjE4MzEwMg.G-ePWa.8voRNngCu3j-hFSObrXbPI3c9QRhFmJ5snWgog")
API_KEY = os.environ.get("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")

# Inicjalizacja klienta Groq
client = Groq(api_key=API_KEY)
bot = discord.Client()

@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user}. Bot jest aktywny.")

@bot.event
async def on_message(message):
    # Bezpieczniki
    if message.author == bot.user or message.author.bot:
        return

    # Symulacja ludzkiego zachowania
    await asyncio.sleep(random.uniform(2.0, 5.0))

    try:
        async with message.channel.typing():
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "Jesteś pomocnym użytkownikiem. Odpowiadaj krótko i naturalnie."},
                    {"role": "user", "content": message.content}
                ],
                model="llama-3.1-8b-instant",
            )
            
            reply = chat_completion.choices[0].message.content
            await message.channel.send(reply)
            
    except Exception as e:
        print(f"Błąd podczas przetwarzania wiadomości: {e}")

# KROK KLUCZOWY: Uruchomienie tylko, gdy skrypt jest wykonywany bezpośrednio
if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("BŁĄD: Zmienna DISCORD_TOKEN nie została znaleziona w środowisku!")
