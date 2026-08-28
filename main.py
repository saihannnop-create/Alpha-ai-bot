import os
import discord
from discord.ext import commands
from openai import OpenAI

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Cloud settings se Keys read karna
DISCORD_TOKEN = os.getenv("MTU0MjYwNDc2NDkyMjExODM1NA.G1SZuL.-z4sUALCc4EI7kV4w3Pu6H0oZk-U-Dj_4bdJi4")
OPENAI_API_KEY = os.getenv("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")

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = "Aap mere AI assistant hain. Jab koi mujhe tag kare, to unhe batayein ke main abhi available nahi hoon."

@bot.event
async def on_ready():
    print(f'Bot {bot.user} online ho gaya hai!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user in message.mentions:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message.content}
            ]
        )
        ai_reply = response.choices[0].message.content
        await message.channel.send(ai_reply)

    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)
