def lerGrafo(txt):
    grafo = {}
    with open(txt, 'r') as file:
        for linha in file:
            u, v = linha.strip().split()
            if u not in grafo:
                grafo[u] = []
            grafo[u].append(v)
    return grafo

def fechoTransitivoDireto(grafo, vertice, visitados):
    visitados.add(vertice)
    if vertice in grafo:
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                fechoTransitivoDireto(grafo, vizinho, visitados)

def fechoTransitivoInverso(grafo, vertice, visitados, componenteAtual):
    visitados.add(vertice)
    componenteAtual.append(vertice)
    if vertice in grafo:
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                fechoTransitivoInverso(grafo, vizinho, visitados, componenteAtual)

def componentesFortementeConexas(grafo):
    visitados = set()
    pilha = []
    for vertice in grafo.keys():
        if vertice not in visitados:
            fechoTransitivoDireto(grafo, vertice, visitados)
            pilha.append(vertice)
    grafoTransposto = {}
    for u in grafo:
        for v in grafo[u]:
            if v not in grafoTransposto:
                grafoTransposto[v] = []
            grafoTransposto[v].append(u)
    visitados.clear()
    listaFortementeConexas = []
    while pilha:
        vertice = pilha.pop()
        if vertice not in visitados:
            componenteAtual = []
            fechoTransitivoInverso(grafoTransposto, vertice, visitados, componenteAtual)
            listaFortementeConexas.append(componenteAtual)
    return listaFortementeConexas

def imprimirResultado(componentes):
    for i, componente in enumerate(componentes):
        print(f"Componentes f-conexas {i + 1}: {componente}")

if __name__ == "__main__":
    arquivo_grafo = "grafos.txt"
    grafo = lerGrafo(arquivo_grafo)
    resultados = componentesFortementeConexas(grafo)
    imprimirResultado(resultados)
