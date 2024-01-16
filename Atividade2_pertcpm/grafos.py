import networkx as nx

G = nx.read_weighted_edgelist("grafos.txt", create_using=nx.DiGraph())

def tempoInicialMaisCedo(no, G):
    if not list(G.predecessors(no)):
        return 0
    tempoMaisCedo = max(tempoInicialMaisCedo(predecessor, G) + G[predecessor][no]['weight'] for predecessor in G.predecessors(no))
    return tempoMaisCedo

duracaoProjeto = max(tempoInicialMaisCedo(no, G) for no in G)

def tempoInicialMaisTarde(no, G):
    if not list(G.successors(no)):
        return duracaoProjeto
    tempoMaisTarde = min(tempoInicialMaisTarde(successor, G) - G[no][successor]['weight'] for successor in G.successors(no))
    return tempoMaisTarde

def caminhoCritico(G):
    nos_criticos = []
    for no in G:
        if tempoInicialMaisCedo(no, G) == tempoInicialMaisTarde(no, G):
            nos_criticos.append(no)
    return nos_criticos

print("\n| Informações do grafo |")
print("\n-> Tempos mais cedo:")
for no in G:
    print("|> " + no + " -", tempoInicialMaisCedo(no, G))

print("\n-> Tempos mais tarde:")
for no in G:
    print("|> " + no + " -", tempoInicialMaisTarde(no, G))

print("\n-> Caminho crítico:")
print("|>", caminhoCritico(G))