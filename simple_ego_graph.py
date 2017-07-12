# Dependencies
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

# Number of nodes and m is the connection with the last node (in the center)
n = 5
m = 4

# A graph of n nodes is grown by attaching new nodes each with m
# edges that are preferentially attached to existing nodes with high degree.
# the node with the highest degree is generally the one with the last label.
G3 = nx.generators.barabasi_albert_graph(n, m)

# Finds the node basically with the highest degree associated, and makes it the
# center,typically it is the last node.
node_and_degree = G3.degree()

# Get the node with the most degree (the label), and the degree associated with
# it
(largest_hub, degree) = sorted(node_and_degree.items(), key=itemgetter(1))[-1]

# Make an ego graph with the node with the highest degree right in the center
hub_ego = nx.ego_graph(G3, largest_hub)

# This is basically used to layout the graph in the image, like for example
# at what position to center it, and which nodes to keep fixed etc.
pos = nx.spring_layout(hub_ego)

# Set the labels for each of the nodes which will be show in the graph
labels = {0: 'harsh', 1: 'deep', 2: 'singh', 3: 'chauhan', 4: 'gino'}

# Draw the other nodes in blue color with the size associated and the labels
# and the position associated with them
nx.draw(hub_ego, pos, node_color='b', node_size=50, labels=labels, with_labels=True)

# Draw the network's nodes with the nodelist (node at the center with a much more larger size)
# and with a different color and position (which we get from spring layout)
nx.draw_networkx_nodes(hub_ego, pos, nodelist=[largest_hub], node_size=300, node_color='r')

# Save the image
plt.savefig('ego_graph.png')

# Show the image
plt.show()
