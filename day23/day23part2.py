import networkx as nx
import matplotlib.pyplot as plt 

G = nx.Graph()

with open('input.txt') as f:
    for line in f:
        line = line.strip().split('-')
        G.add_edge(line[0], line[1])

# nx.draw(G)
# plt.show()

print(G)

largest = []

to_search = [tuple([node]) for node in G.nodes()]
added = set(to_search)
while to_search:
    nodes = list(to_search.pop())
    # get nodes which are directly connected to current nodes
    neighbours = set(G.nodes())
    for node in nodes:
        neighbours &= set(G.neighbors(node))
        if len(nodes) + len(neighbours) <= len(largest):
            break
    if len(nodes) + len(neighbours) <= len(largest):
        continue
    if len(neighbours) == 0:
        if len(nodes) > len(largest):
            largest = nodes
    for neighbour in neighbours:
        new_nodes = tuple(sorted(nodes + [neighbour]))
        if new_nodes in added:
            continue
        to_search.append(new_nodes)
        added.add(new_nodes)
print(','.join(largest))
