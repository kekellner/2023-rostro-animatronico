# Aqui importe el primer pip que instale
import openai       

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

# Lo que se hace en esta parte es tomar la entrada del usuario
# mandarsela al API de OpenAI y despues leer la respuesta

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
mensajes = append({"role": "assistant", "content": respuesta})   # Se adjunta la lista de mensajes, se alamacena la conversacion
print(f"\n(respuesta)\n")