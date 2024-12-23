import networkx as nx
import matplotlib.pyplot as plt 

G = nx.Graph()

with open('input.txt') as f:
    for line in f:
        line = line.strip().split('-')
        G.add_edge(line[0], line[1])

# nx.draw(G)
# plt.show()

sets = set()

for node in G.nodes():
    neighbours = list(G.neighbors(node))
    for i in range(len(neighbours)):
        for j in range(i + 1, len(neighbours)):
            if G.has_edge(neighbours[i], neighbours[j]):
                sets.add(tuple(sorted(map(str, [node, neighbours[i], neighbours[j]]))))

sets = [s for s in sets if any([s_[0] == 't' for s_ in s])]
print(len(sets))
