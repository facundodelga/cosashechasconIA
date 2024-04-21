from pytube import YouTube

# Ingresa la URL del video de YouTube
url = input("Ingresa la URL del video: ")

# Crea un objeto YouTube desde la URL
yt = YouTube(url)

# Obtener todos los streams de video disponibles
streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

# Muestra las opciones de resolución disponibles
for i, stream in enumerate(streams):
    print(f"{i+1}. {stream.resolution}")

# Pide al usuario que elija una resolución
index = int(input("Ingresa el número de la resolución deseada: "))
selected_stream = streams[index-1]

# Pide al usuario la ruta de descarga
download_path = input("Ingresa la ruta de descarga (dejar en blanco para descargar en el directorio actual): ")

# Si no se ingresa una ruta, se descarga en el directorio actual
if not download_path:
    download_path = os.getcwd()

# Descarga el video
print(f"Descargando video en {download_path}...")
selected_stream.download(output_path=download_path)
print("¡Video descargado exitosamente!")
# Descarga el video
print("Descargando video...")
selected_stream.download()
print("¡Video descargado exitosamente!")