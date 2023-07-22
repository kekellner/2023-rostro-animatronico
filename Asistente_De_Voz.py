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

# Hasta donde se gtp 3.5 turbo es como el motor que usar ChatGPT para funcionar
# La variable temperature es el porcentaje de aleatoriedad de la respuesta

afinacion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo-0301",   # Estos son parametros
            mensajes = mensajes             # que van a servirle
            temperature = 0.8               # a la afinacion
            )