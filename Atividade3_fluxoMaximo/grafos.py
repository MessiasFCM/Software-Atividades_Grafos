import networkx as nx
from collections import deque

def fordFulkerson(graph, source, sink): # Função para buscar o fluxo máximo
    max_flow = 0
    while True:
        path, capacity = bfs(graph, source, sink)
        
        if path is None:
            break
        
        updateResidual(graph, path, capacity) 
        max_flow += capacity
    
    return max_flow

def bfs(graph, source, sink): # Faz a busca no grafo
    path = []
    min_capacity = float('inf')
    
    queue = deque([(source, [source], min_capacity)])
    
    visited = {vertex: False for vertex in graph.nodes}
    
    visited[source] = True
    
    while queue:
        current_vertex, current_path, current_capacity = queue.popleft()
        
        for neighbor, edge_data in graph[current_vertex].items():
            capacity = edge_data['capacity']  # Acessar a capacidade correta
            
            if ((not visited[neighbor]) and (capacity > 0)):
                visited[neighbor] = True
                
                new_path = current_path + [neighbor]
                new_capacity = min(current_capacity, capacity)
                
                if (neighbor == sink):
                    return new_path, new_capacity
                
                queue.append((neighbor, new_path, new_capacity))
                
    return None, 0

def updateResidual(graph, path, capacity): # Percorrer o caminho e subtrair a capacidade mínima da capacidade original
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]

        graph[u][v]['capacity'] -= capacity

        if graph[u][v]['capacity'] == 0:
            graph.remove_edge(u, v)

        if not graph.has_edge(v, u):
            graph.add_edge(v, u, capacity=0)

        graph[v][u]['capacity'] += capacity

def main():
    graph = readGraphFromFile("grafos.txt")
    
    source = "1" # Vértice de origem
    sink = "6" # Vértice de destino
    
    if ((source not in graph.nodes) or (sink not in graph.nodes)):
        print("Vértices de origem ou destino não estão presentes no grafo.")
        return
    
    max_flow = fordFulkerson(graph, source, sink)
    
    print(f"\n-> Fluxo Máximo: {max_flow}\n")
    print(f"-> Fluxos em cada aresta:")
    for u, v, data in graph.edges(data=True):
        print(f'- Aresta ({u} -> {v}): Fluxo = {data["capacity"]}')

def readGraphFromFile(file_path): # Fazer leitura do arquivo TXT
    graph = nx.DiGraph()
    with open(file_path, 'r') as file:
        for line in file:
            source, sink, capacity = line.split()
            graph.add_edge(source, sink, capacity=int(capacity))
    return graph

if __name__ == "__main__":
    main()