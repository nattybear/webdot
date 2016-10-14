from pydot import Dot, Edge

def add_dot(src, dst):
    g = Dot(graph_type='digraph')
    e = Edge(src, dst)
    g.add_edge(e)
    g.write_png('result.png')
    return