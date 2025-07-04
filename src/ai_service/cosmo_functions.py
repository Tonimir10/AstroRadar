import os
from dotenv import load_dotenv
from openai import OpenAI

def cosmo_tip():
    prompt = "Dame un tip para la visualización de eventos astronómicos, relacionado con la localización, contaminación lumínica, climatología y más cosas del estilo. La respuesta no debe tener más de 10 palabras."
    
    load_dotenv()
    openai_key = os.getenv("OPENAI_API_KEY")
    
    client = OpenAI(api_key=openai_key)
    
    response = client.responses.create(
        model="gpt-3.5-turbo",
        input=prompt
    )
    
    return response.output_text