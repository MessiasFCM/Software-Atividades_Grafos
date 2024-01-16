import networkx as nx
import matplotlib.pyplot as plt

def cobertura_minima_esquinas(graph):
    ordered_nodes = sorted(graph.nodes(), key=lambda node: graph.degree(node), reverse=True)
    esquinas_cobertas = set()

    for node in ordered_nodes:
        if set(graph.edges()) <= set(graph.edges(esquinas_cobertas)):
            break

        esquinas_cobertas.add(node)
        esquinas_cobertas.update(graph.neighbors(node))

    return esquinas_cobertas

def plot_graph_with_cameras(graph, esquinas_cobertas):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_edges(graph, pos, edge_color='gray', width=1.5)
    vertices_nao_cobertos = set(graph.nodes()) - esquinas_cobertas
    
    nx.draw_networkx_nodes(graph, pos, nodelist=vertices_nao_cobertos, node_color='skyblue', node_size=300)
    nx.draw_networkx_nodes(graph, pos, nodelist=esquinas_cobertas, node_color='salmon', node_size=300)
    nx.draw_networkx_labels(graph, pos, font_size=8, font_color='black', font_family='sans-serif')
    edge_labels = nx.get_edge_attributes(graph, 'name')
    
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='darkgray', font_size=6)
    plt.show()

graph = nx.read_gml("sjdr.gml")

solucao_esquinas = cobertura_minima_esquinas(graph)

print("-> Esquinas com câmeras:", solucao_esquinas)

plot_graph_with_cameras(graph, solucao_esquinas)