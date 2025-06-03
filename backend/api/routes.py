from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import List
from core.grafo import GrafoEntrega
from core.fluxo_maximo import fluxo_maximo

router = APIRouter()

# Entrada da API
class RotaInput(BaseModel):
    origem: str
    destino: str
    capacidade: int

class GrafoInput(BaseModel):
    depositos: List[str]
    hubs: List[str]
    zonas: List[str]
    rotas: List[RotaInput]

@router.post("/fluxo/calcular")
def calcular_fluxo(dados: GrafoInput):
    grafo = GrafoEntrega()

    # Adiciona todos os nós no grafo
    for d in dados.depositos:
        grafo.adicionar_nodo(d, "deposito")
    for h in dados.hubs:
        grafo.adicionar_nodo(h, "hub")
    for z in dados.zonas:
        grafo.adicionar_nodo(z, "zona")

    # Adiciona todas as rotas
    for rota in dados.rotas:
        grafo.adicionar_rota(rota.origem, rota.destino, rota.capacidade)

    # Constrói o grafo como dicionário para o algoritmo
    grafo_dict = {nodo: grafo.obter_vizinhos(nodo) for nodo in grafo.todos_nodos()}

    # Assumimos um único depósito e uma única zona, por simplicidade
    if not dados.depositos or not dados.zonas:
        raise HTTPException(status_code=400, detail="É necessário pelo menos um depósito e uma zona")

    origem = dados.depositos[0]
    destino = dados.zonas[0]

    fluxo = fluxo_maximo(grafo_dict, origem, destino)

    return {
        "fluxo_maximo": fluxo,
        "origem": origem,
        "destino": destino
    }

@router.get("/grafo/exemplo")
def exemplo_grafo():
    return {
        "pontos": [
            { "id": "D1", "tipo": "deposito", "lat": -23.55, "lng": -46.63 },
            { "id": "H1", "tipo": "hub", "lat": -23.56, "lng": -46.62 },
            { "id": "H2", "tipo": "hub", "lat": -23.54, "lng": -46.64 },
            { "id": "Z1", "tipo": "zona", "lat": -23.57, "lng": -46.65 },
            { "id": "Z2", "tipo": "zona", "lat": -23.53, "lng": -46.61 }
        ],
        "rotas": [
            { "origem": "D1", "destino": "H1", "capacidade": 10 },
            { "origem": "D1", "destino": "H2", "capacidade": 15 },
            { "origem": "H1", "destino": "Z1", "capacidade": 5 },
            { "origem": "H2", "destino": "Z2", "capacidade": 10 }
        ]
    }