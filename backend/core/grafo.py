# Representa um ponto na rede de entregas (depósito, hub ou zona de entrega)
class Nodo:
    def __init__(self, id, tipo, nome=None):
        self.id = id
        self.tipo = tipo  # Pode ser 'deposito', 'hub', 'zona'
        self.nome = nome
        self.vizinhos = {}  # {id_nodo_destino: capacidade}

# Representa uma rota entre dois pontos, com capacidade de entrega
class Rota:
    def __init__(self, origem, destino, capacidade):
        self.origem = origem
        self.destino = destino
        self.capacidade = capacidade

# Grafo dirigido com capacidades — base para o algoritmo de fluxo
class GrafoEntrega:
    def __init__(self):
        self.nodos = {}  # {id_nodo: Nodo}
        self.rotas = []  # Lista de objetos Rota

    def adicionar_nodo(self, id, tipo, nome=None):
        if id not in self.nodos:
            self.nodos[id] = Nodo(id, tipo, nome)

    def adicionar_rota(self, origem_id, destino_id, capacidade):
        if origem_id in self.nodos and destino_id in self.nodos:
            self.nodos[origem_id].vizinhos[destino_id] = capacidade
            self.rotas.append(Rota(origem_id, destino_id, capacidade))

    def obter_vizinhos(self, id_nodo):
        return self.nodos[id_nodo].vizinhos if id_nodo in self.nodos else {}

    def todos_nodos(self):
        return list(self.nodos.keys())

    def todas_rotas(self):
        return [(r.origem, r.destino, r.capacidade) for r in self.rotas]
