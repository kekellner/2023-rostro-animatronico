# Aqui importe el primer pip que instale
import openai

# Se realizan nuevos imports para reconocimiento de voz
import speech_recognition as sr
import pyttsx3                      # py text to speech       
import os
import json

# Despues vamos a inicializar ChatGPT
# Para ello se necesita de una llave unica que genera ChatGPT
llave = ''
openai.api_key = llave

# Asignacion de personalidad
# Variable de personalida
personalidad = "personality.txt"
userwhisper = False               # cobro de 0.006 dolares por minuto de audio

with open(personalidad, "r") as file:
    mode = file.read()

mensajes = [
    {"role": "system", "content": f"{mode}"}
]

# Inicializamos el engine de text to speech
engine = pyttsex3.init()
voces = engine.getProperty('voces')      # Obtener todas la voces que tenemos instaladas en windows
engine.setProperty('voice', voces[1].id) # 0 para hombre y 1 para mujer

# Inicializacion del microfono
r = sr.Recognizer()
micro = sr.Microphone(device_index=0) # decive index para decidir que microfono se va a usar, 0 default
r.dynamic_energy_threshold = False    # Para que no active el microfono en todo momento
r.energy_threshold = 400

def whisper(audio):
    # entrada_usuario = r.recognize_google(audio)      # va a tratar de usar el reconocedor de google si se hablo
    # vamos a usar whisper
    with open('speech.wav', 'wb') as f:
        f.write(audio.get_wave_data())              # Esto se va a escribir a un archivo wav
    speech = open('speech.wav', 'rb')
    wcompletion = openai.Audio.transcribe(
        model = "whisper-1"
        file = speech
    )
    user_input = wcompletion['text']
    print(user_input)
    return user_input

# Definicion de funcion que se encarga de guardar la conversacion para que no exista
# una sobre escritura de folders
# En este codigo se dirige al directorio donde tenemos nuestro folder y revisa 
# que el path exista, sino existiese se encarga de crear un archivo de texto
# el cual vamos a poder editar

def save_conversation(save_foldername):
    '''
    Checks the folder for previous conversations and will get the next suffix that has not been used yet.
    it return suffix number
    
    Args:
        save_foldername (str) : Takes in the path to save the conversation to.
    '''
    os.makedirs(save_foldername, exist_ok = True)

    base_filename = 'conversation'
    suffix = 0
    filename = os.path.join(save_foldername, f'{base_filename}_{suffix}.txt')

    while os.path.exists(filename):
        suffix += 1
        filename = os.path.join(save_foldername, f'{base_filename}_{suffix}.txt')

    with open(filename, 'w') as file:
        json.dump(self.mensajes, file, indent = 4)

    return suffix


def save_inprogress(suffix, save_foldername):
    '''
    Uses the suffix number returned from save_conversation to continually update the file for this 
    instance of execution. This is so that you can save the conversation as you go so if it crashes, 
    you don't lose the conversation. Shouldn't be called from outside of the class.
    
    Args:
        suffix : Takes suffix count from save_conversation()
        '''
    
    os.makedirs(save_foldername, exist_ok = True)
    base_filename = 'conversation'
    filename = os.path.join(save_foldername, f'{base_filename}_{suffix}.txt')

# Lo que se hace en esta parte es tomar la entrada del usuario
# mandarsela al API de OpenAI y despues leer la respuesta
# El while se agrega para que siga preguntando

while True:

    # Para poder escuchar la voz generada
    with micro as source:
        print("\nEscuchando...")
        r.adjust_for_ambient_noise(source, duration = 0.5)   # Tiempo en el que se ajustara para el ruido del ambiente
        audio = r.listen(source)                             # Almace lo que escucho en esta variable
        try:
            if usewhisper:
                user_input = whisper(audio)
            else:
                user_input = r.recognize_google(audio)
        except:
            continue                                         # Sino va a pasar por alto las siguientes lineas de codigo y a volver a escuchar hasta conseguir una respuesta valdia

    # Creamos la entrada del usuario
   # entrada_usuario = input('Que pregunta deseas hacer: ')

    ## Adjuntamos la lista
    mensajes.append({"role": "user": "content": entrada_uuario})

    # Hasta donde se gtp 3.5 turbo es como el motor que usar ChatGPT para funcionar
    # La variable temperature es el porcentaje de aleatoriedad de la respuesta

    afinacion = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo-0301",   # Estos son parametros
                mensajes = mensajes             #    que van a servirle
                temperature = 0.8               # a la afinacion
                )

    # Se imprime la respuesta
    respuesta = afinacion.choices[0].message.content                 # El cero es para la respuesta mas reciente
    mensajes.append({"role": "assistant", "content": respuesta})   # Se adjunta la lista de mensajes, se alamacena la conversacion
    print(f"\n(respuesta)\n")
    engine.say(f'{respuesta}')
    engine.runAndWait()