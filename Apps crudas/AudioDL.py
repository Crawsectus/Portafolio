import yt_dlp

def descargar_audio(url):
    opciones = {
        'format': 'bestaudio/best', 'noplaylist': True,
        'outtmpl': '%(title)s.%(ext)s',  # guarda con el nombre del video
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # o 'wav', 'aac', etc.
            'preferredquality': '192',  # calidad de audio
        }],
        'quiet': False,  # Muestra el progreso
        'ffmpeg_location': 'C:/ffmpeg/ffmpeg.exe',
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])

enlace = input("Introduce el enlace del video: ")
descargar_audio(enlace)
