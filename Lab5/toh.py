import copy
import queue
class state:
    cost = 0
    childs = []
    poles = [[],[],[]]
    visited = False
    explored = False
    parent = 0

def display(state):
    i = 0
    for pole in state.poles:
        print(i," -> ",pole)
        i = i + 1
    print()

def deepcopy(a):
    node = state()
    node.childs = copy.deepcopy(a.childs)
    node.poles = copy.deepcopy(a.poles)
    return node

def movegen(state):
    return True