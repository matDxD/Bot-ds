import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from Comandos.Play import *

load_dotenv()

token= os.getenv('token_discord')

intents = discord.Intents.all()
intents.messages = True  #permite interactuar con mensajes
intents.members = True #permite interactuar con miembros

bot = commands.Bot(command_prefix='|',intents = intents) #prefijo para comandos
def run_bot():
    @bot.command() # actua de acuerdo a un comando
    async def info(ctx):
        await ctx.send('en efecto estimado no hago nada mas')

    @bot.command() 
    async def puto(ctx):
        await ctx.send(f'Al parecer {ctx.author.name} quiere confesarnos algo; ya era hora que salieras de ese armario!!')
        
    
    
    
    @bot.event
    async def on_ready(): #para que haga cuando el bot se conecte
      
        await bot.change_presence(
            status= discord.Status.idle,
            activity=discord.Activity(type = discord.ActivityType.listening, name ="Musica")) #indica que actividad esta realizando 
        print ("El bot esta conectado")
        mplay(bot)

        #print (discord.VoiceChannel.voice_states)    



    @bot.event 
    async def on_message(message):
        if message.author == bot.user:
            return
        
        if 'hola' in message.content.lower():
            await message.channel.send(f'Cual hola  {message.author.name}')
            #await message.channel.send(f'Cual hola sapo hpta')

        await bot.process_commands(message)

    bot.run(token)