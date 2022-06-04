import EoN
import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt
import random

N = 10000
G = nx.fast_gnp_random_graph(N, 5./(N-1))

#We have defined our network ( which is a random graph) with N number of nodes
#5 is the number that decides how densely the nodes are connected

#We show how node and edge attributes in the contact network 'G' can be used
#to scale the transmission rates.

#Let us define H for the spotaneous transitions
H = nx.DiGraph()
H.add_node('S')
#
H.add_edge('I', 'R', rate=0.5)
#  The line above states that the I to 'R' transition occurs with rate 0.5
#
#Let us define J for the induced transitions
#
J = nx.DiGraph()
J.add_edge(('I', 'S'), ('I', 'I'), rate=0.6)
#  The line above states that an 'I' individual will cause an 'S' individual
#  to transition to 'I' with rate equal to 0.6

#Defining initial conditions
IC = defaultdict(lambda: 'S')
for node in range(5000):
    IC[node] = 'I'

return_statuses = ('S', 'I', 'R')

t, S, I, R = EoN.Gillespie_simple_contagion(G, H, J, IC, return_statuses,
                                        tmax=float('Inf'))

plt.plot(t, S, label='Susceptible')
plt.plot(t, I, label='Infected')
plt.plot(t, R, label='Recovered')
plt.legend()
plt.show()
# plt.savefig('SIR.png')

#FOR TRYING OUT SIR MODEL, THE SAME CODE WOULD WORK IF YOU MODFIY ACCORDINGLY. THE ONLY CHANGE YOU NEED IS SET tmax=20 INSTEAD OF tmax = float('Inf'). THIS DICTATES THE FINISHING TIME AND DOES NOT LOOK FOR AN AUTOMATIC SATURATION. THINK ABOUT WHY THIS IS NEEDED IN SIR.
