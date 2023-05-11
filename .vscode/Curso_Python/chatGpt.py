import openai

openai.api_key="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"

modelo ="text-davinci-003"
pergunta = "Crie um código python para ler um geopackage"
resposta = openai.Completion.create(
                    engine=modelo,
                    prompt=pergunta,
                    max_tokens=1024)

print(resposta.choices[0].text) # type: ignore
    
    
    
    