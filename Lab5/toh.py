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
    ls = []
    for i in range(0,3):
        for j in range(0,3):
            if(i != j):
                if(len(state.poles[i]) != 0):
                    if(len(state.poles[j]) == 0 or ((len(state.poles[j]) != 0) and (state.poles[j] > state.poles[i]))):
                        new = deepcopy(state)
                        new.poles[j].append(state.poles[i][-1])
                        del new.poles[i][-1]
                        ls.append(new)
    return ls

st = state()

st.poles = [[1,2,3],[],[]]

display(st)
ls = movegen(st)

for i in ls:
    display(i)