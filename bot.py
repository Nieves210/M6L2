# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
from config import TOKEN
from AIGenerator import generate_image_from_text
from AIGenerator import FusionBrainAPI
from config import API_KEY, SECRET_KEY
import os
import asyncio




intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):
    if message.author== bot.user:
        return
    
    api_url='https://api-key.fusionbrain.ai/'
    api= FusionBrainAPI(api_url, API_KEY, SECRET_KEY)
    file_path="generated_image.jpg"
    prompt=message.content
    string= generate_image_from_text(prompt, api_url, API_KEY,SECRET_KEY)
    api.save_image(string[0], file_path)
    with open(file_path, "rb") as photo:
        await message.channel.send(file=discord.File(photo, filename="generated_image.jpg"))

    os.remove(file_path)


@bot.command(name="start")
async def start(ctx):
    await ctx.send("Merhaba! Ben bir AI görsel üretim botuyum. `!generate [açıklama]` yazarak bir görüntü üretebilirsin!")

@bot.command(name="help")
async def help_command(ctx):
    await ctx.send("Kullanım: `!generate bir uzaylı manzarası`\nBot, açıklamaya uygun bir görsel üretir ve sana yollar.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "şarkı söyle" in message.content.lower():
        async with message.channel.typing():
            await message.reply("La la laaa... (favori şarkını mırıldanıyormuşum gibi yaparsan sevinirim)")

    await bot.process_commands(message)  






bot.run(TOKEN)