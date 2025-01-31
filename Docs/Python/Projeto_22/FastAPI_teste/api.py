from fastapi import FastAPI
import uvicorn


app = FastAPI()

vendas = {

    1:{"imtem": "caneta", "quantidade": 10, "valor": 7.50},
    2:{"imtem": "lapis", "quantidade": 5, "valor": 4.50},
    3:{"imtem": "caderno", "quantidade": 20, "valor": 15.00},
    4:{"imtem": "caderno", "quantidade": 20, "valor": 15.00},
}

@app.get("/")
def home():
    return{"vendas":len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    try:
        return vendas[id_venda]
    except KeyError:
        return {"Erro": "Venda não encontrada"}

