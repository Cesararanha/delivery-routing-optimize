from collections import deque

# Executa BFS no grafo residual para encontrar um caminho aumentante
def bfs(grafo, origem, destino, caminho):
    visitado = set()
    fila = deque()
    fila.append(origem)
    visitado.add(origem)
    caminho.clear()

    while fila:
        atual = fila.popleft()
        for vizinho, capacidade in grafo[atual].items():
            if vizinho not in visitado and capacidade > 0:
                caminho[vizinho] = atual
                if vizinho == destino:
                    return True
                fila.append(vizinho)
                visitado.add(vizinho)
    return False

# Calcula o fluxo máximo entre uma origem e um destino usando Edmonds-Karp
def fluxo_maximo(grafo_original, origem, destino):
    grafo = {u: dict(v) for u, v in grafo_original.items()}
    caminho = {}
    fluxo_total = 0

    while bfs(grafo, origem, destino, caminho):
        fluxo_caminho = float('inf')
        atual = destino
        while atual != origem:
            anterior = caminho[atual]
            fluxo_caminho = min(fluxo_caminho, grafo[anterior][atual])
            atual = anterior

        atual = destino
        while atual != origem:
            anterior = caminho[atual]
            grafo[anterior][atual] -= fluxo_caminho
            grafo.setdefault(atual, {})
            grafo[atual][anterior] = grafo[atual].get(anterior, 0) + fluxo_caminho
            atual = anterior

        fluxo_total += fluxo_caminho

    return fluxo_total
