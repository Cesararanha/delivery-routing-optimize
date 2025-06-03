
# Delivery Routing Optimizer 🚚📦

**Projeto acadêmico da disciplina de Estrutura de Dados Avançada**  
Otimizador de Rede de Entregas utilizando grafos e algoritmos de fluxo máximo.

---

## 🎯 Objetivo

Desenvolver um sistema inteligente de apoio à logística de entregas, modelando a rede de distribuição como um grafo orientado com rotas de capacidade limitada.  
O sistema calcula o **fluxo máximo de entregas** entre depósitos e zonas de entrega utilizando o algoritmo **Ford-Fulkerson com estratégia Edmonds-Karp**.

---

## 🧰 Tecnologias Utilizadas

| Camada    | Ferramentas                                                |
|-----------|-------------------------------------------------------------|
| Backend   | Python, FastAPI, Algoritmos de Grafos (implementação manual)|
| Frontend  | React, Vite, Leaflet.js                                     |
| Mapa      | OpenStreetMap via TileLayer                                 |
| Deploy    | Uvicorn (local), GitHub (controle de versão)                |

---

## ⚙️ Funcionalidades

- 📍 Visualização geográfica de depósitos, hubs logísticos e zonas de entrega
- 🔁 Representação de rotas com capacidade de tráfego (pacotes/hora)
- 📈 Cálculo automático do **fluxo máximo de entregas**
- 💡 Backend dinâmico, pronto para receber dados reais (API ou JSON)
- 🧪 Estrutura preparada para simulação de cenários (ex: falhas, aumento de demanda)

---

## 🚀 Como Executar Localmente

### 📦 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/delivery-routing-optimize.git
cd delivery-routing-optimize
```
---
### ⚙️ 2. Backend (API com FastAPI)

```bash
cd backend
python -m venv venv
venv\Scripts\activate # (Windows) pip install -r requirements.txt
uvicorn main:app --reload
```
Acesse a documentação Swagger:  
[http://localhost:8000/docs](http://localhost:8000/docs)

---

### 💻 3. Frontend (Visualização com React)

```bash
cd ../frontend
npm install
npm run dev
```

Visualize no navegador:  
[http://localhost:5173](http://localhost:5173)

---

## 📌 Status Atual do Projeto

-   ✅ Visualização interativa da rede logística em mapa
    
-   ✅ Algoritmo de fluxo máximo implementado e integrado
    
-   ✅ API funcional com exemplo de grafo pré-configurado
    
-   🔄 Em desenvolvimento: Interface para inserção de pontos/rotas pelo usuário
    
-   🔜 Próximas etapas: Simulador de falhas logísticas, relatórios e persistência de dados

---

### 👤 Autor

**César**  
Projeto acadêmico — 2ª Unidade | Estrutura de Dados Avançada

---
📂 Licença: Uso acadêmico | Todos os direitos reservados ao autor.