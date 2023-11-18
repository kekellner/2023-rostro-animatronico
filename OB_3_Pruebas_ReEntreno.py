
# OBJETIVO 3
# Entrenar a la inteligencia artificial con datos relevantes de la Universidad
# y el Departamento de Ingeniería Electrónica, Mecatrónica y Biomédica.


import os
import sys

import openai   
import INFO_U

# de la librería langchain
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

# Aqui es donde se verifica la llave creada por nuestra cuenta en ChatGPT
os.environ["OPENAI_API_KEY"] = INFO_U.APIKEY

# Me indica que debo tener algo escrito al momento de ejecutar el programa
# Es decir que escribo la pregunta que deseo y consecutivamente ejecuto el programa
query = sys.argv[1]

# cargar un documento tipo texto 
loader = TextLoader('data.txt')

# Aqui vectoriza, es decir que analiza y esctrutura
# la informacion del documento tipo texto
index = VectorstoreIndexCreator().from_loaders([loader])

# Imprime la respuesta a nuestra pregunta
print(index.query(query, llm=ChatOpenAI()))