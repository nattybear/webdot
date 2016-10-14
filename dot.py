from networkx import DiGraph
import networkx as nx
from pickle import dump, load

def add_dot(src, dst):
    # g = DiGraph()
    g = load_dot()
    g.add_edge(src, dst)
    return g

def make_dot(g):
    p = nx.nx_pydot.to_pydot(g)
    p.write_png('result.png')
    return
    
def save_dot(g):
    f = open('graph.dump', 'wb')
    dump(g, f)
    print '[*] saved to graph.dump'
    return
   
def load_dot():
    f = open('graph.dump', 'rb')
    g = load(f)
    return g