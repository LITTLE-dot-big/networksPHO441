import EoN
import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt
import cv2 as cv

alpha, beta, gamma, delta, omega = 0, 0, 0, 0, 0
def empty(a):
    pass
def initTrackbars():
    cv.namedWindow('trackbars')
    cv.createTrackbar('alpha', 'trackbars', 2, 10, empty)
    cv.createTrackbar('beta', 'trackbars', 2, 10, empty)
    cv.createTrackbar('gamma', 'trackbars', 2, 10, empty)
    cv.createTrackbar('delta', 'trackbars', 2, 10, empty)
    cv.createTrackbar('omega', 'trackbars', 2, 10, empty)
def readTracbars():
    global alpha, beta, gamma, delta, omega
    alpha = cv.getTrackbarPos('alpha', 'trackbars') / 10
    beta = cv.getTrackbarPos('beta', 'trackbars') / 10
    gamma = cv.getTrackbarPos('gamma', 'trackbars') / 10
    delta = cv.getTrackbarPos('delta', 'trackbars') / 10
    omega = cv.getTrackbarPos('omega', 'trackbars') / 10


N = 10000
G = nx.fast_gnp_random_graph(N, 3./(N-1))
J = nx.DiGraph()
H = nx.DiGraph()

initTrackbars()
while True:
    readTracbars()
    H.add_node('S')
    H.add_edge('S', 'E', rate=alpha)
    H.add_edge('E', 'I', rate=beta)
    H.add_edge('I', 'R', rate=gamma)
    H.add_edge('I', 'CI', rate=delta)
    H.add_edge('CI', 'R', rate=omega)
    J.add_edge(('I', 'E'), ('I', 'I'), rate=beta)
    J.add_edge(('CI', 'I'), ('CI', 'CI'), rate=delta)

    IC = defaultdict(lambda: 'S')
    for node in range(5000):
        IC[node] = 'S'

    return_statuses = ('S', 'E', 'I', 'CI', 'R')

    t, S, E, I, CI, R = EoN.Gillespie_simple_contagion(G, H, J, IC, return_statuses,
                                        tmax=float('Inf'))

    plt.plot(t, S, label='Susceptible')
    plt.plot(t, E, label='Exposed')
    plt.plot(t, I, label='Infected')
    plt.plot(t, CI, label='Chronic Infected')
    plt.plot(t, R, label='Recovered')
    plt.legend()
    plt.show()
    print("Total number of nodes: ", int(H.number_of_nodes()))
    print("Total number of edges: ", int(H.number_of_edges()))
    print("List of all nodes: ", list(H.nodes()))
    print("List of all edges: ", list(H.edges()))
    plt.savefig('SEIR.png')

print("Total number of nodes: ", int(H.number_of_nodes()))
print("Total number of edges: ", int(H.number_of_edges()))
print("List of all nodes: ", list(H.nodes()))
print("List of all edges: ", list(H.edges()))