# Aqui importe el primer pip que instale
import openai

# Se realizan nuevos imports para reconocimiento de voz
import speech_recognition as sr
import pyttsx3                      # py text to speech       

# Despues vamos a inicializar ChatGPT
# Para ello se necesita de una llave unica que genera ChatGPT
llave = ''
openai.api_key = llave

# Asignacion de personalidad
# Variable de personalida
personalidad = "personality.txt"

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

# Lo que se hace en esta parte es tomar la entrada del usuario
# mandarsela al API de OpenAI y despues leer la respuesta
# El while se agrega para que siga preguntando

while True:
    # Creamos la entrada del usuario
    entrada_usuario = input('Que pregunta deseas hacer: ')

    ## Adjuntamos la lista
    mensajes.append({"role": "user": "content": entrada_uuario})

    # Hasta donde se gtp 3.5 turbo es como el motor que usar ChatGPT para funcionar
    # La variable temperature es el porcentaje de aleatoriedad de la respuesta

    afinacion = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo-0301",   # Estos son parametros
                mensajes = mensajes             # que van a servirle
                temperature = 0.8               # a la afinacion
                )

    # Se imprime la respuesta
    respuesta = afinacion.choices[0].message.content                 # El cero es para la respuesta mas reciente
    mensajes.append({"role": "assistant", "content": respuesta})   # Se adjunta la lista de mensajes, se alamacena la conversacion
    print(f"\n(respuesta)\n")