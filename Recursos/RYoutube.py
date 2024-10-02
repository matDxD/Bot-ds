import ytm
from pprint import pprint
import asyncio 
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import yt_dlp

api = ytm.YouTubeMusic()
def Ysugerencia(song):
    try:
     suggestions =api.search_suggestions(song)  #captura el texto y traera la mejor sujerencia

     pprint(f"la cancion que intentas buscar es {suggestions[0]} ")

     return suggestions[0]
    except Exception as e:
        print (f"No se encontro la cancion{song}")
    return False

def obtenerlista(url_lista):
    
    # Configuramos las opciones de yt-dlp
    ydl_opts = {
        'quiet': True,
        #'extract_flat': True,  # No descargar, solo extraer la información de la lista
        'skip_download': True
    }

    # Creamos un diccionario para almacenar los datos de las canciones
    canciones = []

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url_lista, download=False)  # Extraemos la información

        # Verificamos si la información contiene entradas (una lista de reproducción)
        if 'entries' in info:
            playlist_entries = info['entries']
            print(f"Se encontró una lista de reproducción con {len(playlist_entries)} canciones.")
            # Iteramos sobre cada canción/video en la lista de reproducción
            for video in info['entries']:
                # Guardamos los datos relevantes en un diccionario
                if isinstance(video, dict):
                    cancion = {
                        'titulo': video.get('title'),
                        'url': f"https://www.youtube.com/watch?v={video.get('id')}",
                        'duracion': video.get('duration')
                        
                    }
                
                canciones.append(cancion)
    for index, cancion in enumerate(canciones, start=1):
        print(f"{index}. {cancion['titulo']} - {cancion['url']} - Duración: {cancion.get('duracion', 'desconocida')} segundos")
    return canciones

async def playyoutube(ctx, song):
    voice_client = ctx.guild.voice_client
    
    # Opciones de yt_dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': False,  # Permitir listas de reproducción
        'quiet': True,
        'default_search': 'ytsearch',  # Permite buscar directamente por nombre
        'source_address': '0.0.0.0'  # Para evitar problemas de red
    }
    ffmpeg_options = {
        'options': '-vn',
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 8'
    }
    try:

        # Usar yt_dlp para buscar la canción
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(song, download=False)

        
                    # No es una lista de reproducción, es una sola canción
                if 'entries' in info:
                    info = info['entries'][0]
                url2 = info['url']
                title = info['title']
                                   
                    # Cargar la URL de audio usando FFmpeg
                audio_source = discord.FFmpegOpusAudio(url2)

                if not voice_client.is_playing():
                    voice_client.play(audio_source)
                    await ctx.send(f"🎶 Reproduciendo: **{title}**")
                        
                        # Esperar a que la música termine de reproducirse
                    while voice_client.is_playing():
                        await asyncio.sleep(1)
                

            # Desconectar al bot del canal de voz después de terminar
            if not voice_client.is_playing():
                await voice_client.disconnect()
                await ctx.send("Me he desconectado del canal de voz.")
            else:
                await ctx.send("❗ Ya estoy reproduciendo música en este canal.")
           

     

    except Exception as e:
        print(f"Error durante la reproducción: {e}")
        await ctx.send("❗ Ocurrió un error al intentar reproducir la canción.")
        # Asegurarse de que el bot se desconecte en caso de error
        if voice_client.is_connected():
            await voice_client.disconnect()