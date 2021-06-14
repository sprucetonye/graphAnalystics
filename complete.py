import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.components import connected

G = nx.complete_graph(5, nx.Graph())
plt.subplot(121)
nx.draw(G)

G = G.to_directed()
plt.subplot(122)
nx.draw(G.to_directed())

plt.show()