import asyncio 
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import yt_dlp
from Recursos.RYoutube import *
from Recursos.PlaylistBot import *




def mplay(bot):
    try:
        @bot.command()
        async def p(ctx, *args):
            
            listaP = list(args)
            lis=listaP.copy()
            # Verifica si el usuario está en un canal de voz
            if ctx.author.voice is not None:
                channel = ctx.author.voice.channel  # Obtiene el canal de voz en el que está el usuario
                
                if len(args) == 0:
                   await ctx.send(f"cual es la cancion tarado")
                else:
                    nombrec =' '.join(listaP)
                    print(f"{nombrec}")
                    
                    if 'http' in nombrec and not 'list' in nombrec:
                        print("la cancion es un link")
                        song = nombrec
                    
                    else:    
                        song=Ysugerencia(nombrec)

                    if "list" in nombrec:
                        print(f"la cancion es una lista")
                        List=obtenerlista (nombrec)

                 
                        song = False    
                    
                    if song is False:
                        await ctx.send(f"esa webada si existe?, ni yo pude encontrar: {nombrec}")
                    else:
                        print(f" la cancion que buscara sera {song}")

                        if channel.guild.voice_client and channel.guild.voice_client.is_connected():
                            print(f" la canción que se añadirá a la lista es: {song}")
                            lis = listamusica(song)  # Aseguramos que song tiene valor
                            print(f" la lista va asi: \n")
                            print(' '.join(lis))
                        else:
                         
                            await channel.connect()  # El bot se conecta al canal de voz
                           

                        
                        await playyoutube(ctx,song)
                        

                        

                    
                        
                       
                    
            else:
                 await ctx.send(f"Si no estas en un canal de voz, que esperas escuchar? ")
                    
                
    

        @bot.command()
        async def q(ctx):
            # Verifica si el bot está en un canal de voz
            if ctx.voice_client is not None:
                await ctx.voice_client.disconnect()  # Desconecta al bot del canal de voz
                await ctx.send("Me he desconectado del canal de voz.")
            else:
                await ctx.send("No estoy en un canal de voz.")

    except Exception as e:
        print ("error")

        
        