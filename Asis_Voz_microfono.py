# guarda archivos y manipualrlos
import io

# tomar datos generados de microfono a un archivo temporal
from pydub import AudioSegment

# nos sirve como fuente de audio para capturar el audio
import speech_recognition as sr

# motor de sst
import whisper

# nos permite generar archivos y directorios temporales
import tempfile

# nos permite jugar con el sistema operativo
import os

# reproducir la voz de windows
import pyttsx3

# generacion de directorio temporal
temp_file = tempfile.mkdtemp()
save_path = os.path.join(temp_file, 'temp.wav')
#print(f'This is the save path> {save_path}')

# Inicializar a nuestra clase de recognizer
# se almacena en la variable listener
listener = sr.Recognizer()

# Se inicializa todo lo relacionado a pytts3x
# y la voz que se va a usar
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# cambiamos la voz para que hable mas lento
# y que sea en espanol la voz
engine.setProperty('rate', 145)
# setiamos el rate mas grande mas lento habla la voz
engine.setProperty('voice', voices[2].id)
# setea la voz en nuestro caso voices, vamos 
# a usar la voz en espanol

# Esto se uso para ver todas las voces instaladas en windows
#for voice in voices:
#    print(voice)

# Vamos a usar engine el metodo de say para que diga
# lo que este en la variable text
# despues se corre ese say y esperamos a que termine
# de hablar
def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Say something...")
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
            data = io.BytesIO(audio.get_wav_data())
            audio_clip = AudioSegment.from_file(data)
            audio_clip.export(save_path, format='wav')
    except Exception as e:
        print(e)
    return save_path


def recognize_audio(save_path):
    audio_model = whisper.load_model('base')
    transcription = audio_model.transcribe(save_path, language='spanish', fp16=False)
    return transcription['text']


def main():
    response = recognize_audio(listen())
    talk(response)
    print(response)


if __name__ == '__main__':
    main()