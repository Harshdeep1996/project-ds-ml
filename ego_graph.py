import networkx as nx
from math import cos, sin, pi
import matplotlib.pyplot as plt


def get_mappings(content):
    all_mappings = [
        sentence for sentence in content.split() if '-->' in sentence
    ]
    all_key_values = [
        (m.split('-->')[0], m.split('-->')[1]) for m in all_mappings
    ]
    result = {}
    for key, value in all_key_values:
        result.setdefault(key, [])
        result[key].append(value)
    return result


def build_graph(central_name, content):
    services = content[central_name]
    coordinates = generate_coordinates_n_shape(len(services))
    pos_serv_initial = {}
    for n in range(0, len(services)):
        pos_serv_initial[services[n]] = coordinates[n]

    G = make_graph(central_name, services)
    for s in services:
        GS = make_graph(s, content[s], content)
        G = nx.compose(G, GS)
    pos = nx.spring_layout(G, pos=pos_serv_initial)

    plt.figure(3, figsize=(17, 17))
    plt.axis('off')
    # node_size=[len(v) * 400 for v in G.nodes()])
    nx.draw_networkx(G, pos)
    plt.savefig('initial_graph.png')
    plt.show()


def make_graph(central_node, dependent_nodes, content=None):
    G = nx.Graph()
    for d in dependent_nodes:
        G.add_edge(central_node, d)
    return G


def generate_coordinates_n_shape(N):
    coordinates = []
    for n in range(0, N):
        coordinates.append((cos(2 * pi * n / N), sin(2 * pi * n / N)))
    return coordinates


if __name__ == '__main__':
    f = open('./content.txt')
    result = get_mappings(f.read())
    org_name = 'Cloudant'
    build_graph(org_name, result)
