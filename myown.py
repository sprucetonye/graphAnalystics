import networkx as nx
import matplotlib.pyplot as plt
 
G = nx.Graph()
# for single node --G.add_node(':', label='Person', name='Tonye Waribo', age=50)

G.add_nodes_from([('1', {'label': 'Person', 'name': 'Tonye Waribo', 'age': 40}), 
                 ('2', {'label': 'person', 'name': 'Samuel Ellison', 'age': 89}),
                 ('3', {'label': 'person', 'name': 'Peter George', 'age': 70})])
print(G.nodes)
pos = nx.spring_layout(G)
nx.draw(G, pos)
node_labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_labels(G, pos, labels=node_labels)

plt.show()