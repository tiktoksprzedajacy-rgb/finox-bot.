import discord
from groq import Groq
import asyncio
import random

# USTAWIENIA
TOKEN = "MTUwODMyODEyMDExNjE4MzEwMg.Gp5IHP.dUNCVgWoUHmttJoAauhSmhZfsss5jr1NrCnXrs"
GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)
bot = discord.Client()

# Lista ID kanałów, na których bot ma NIE odpowiadać (np. kanały z regulaminem, logi)
IGNORE_CHANNELS = [123456789012345678, 987654321098765432] 

@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user}. Tryb: Stealth/Aktywny.")

@bot.event
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Sprawdzenie czy masz uprawnienia do pisania na danym kanale
    permissions = message.channel.permissions_for(message.guild.me if message.guild else bot.user)
    
    if not permissions.send_messages:
        print(f"Brak uprawnień na kanale {message.channel.name}, pomijam.")
        return

    # ... reszta Twojego kodu z AI ...
    # 2. Ignoruj kanały z czarnej listy
    if message.channel.id in IGNORE_CHANNELS:
        return

    # 3. ZABEZPIECZENIE: "Ludzkie" opóźnienie (od 2 do 6 sekund)
    # To kluczowe, żeby nie wysyłać zapytań w mikrosekundach
    await asyncio.sleep(random.uniform(2.0, 6.0))

    try:
        # 4. Prompt dla AI, żeby był "bezpieczny" i nie pisał głupot
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Jesteś pomocnym użytkownikiem. Odpowiadaj naturalnie, krótko, unikaj spamu, nie używaj slangu botów."},
                {"role": "user", "content": message.content}
            ],
            model="llama-3.1-8b-instant",
        )
        
        reply = chat_completion.choices[0].message.content
        
        # 5. Użycie 'send' zamiast 'reply', aby mniej rzucać się w oczy
        await message.channel.send(reply)
        
    except Exception as e:
        print(f"Błąd: {e}")

bot.run(TOKEN)
