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
    print('Cost: ', state.cost)
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

def cost(state):
    for i in range(0,3):
        for j in state.poles[i]:
            state.cost = state.cost + (i+1)*j

def cost1(state, discs):
    for i in range(0,3):
        for j in range(len(state.poles[i])):
            if i % 2 == 0:
                if discs % 2 == 0:
                    if (j == 0 and state.poles[i][j] % 2 == 0) or (j != 0 and (state.poles[i][j-1] - state.poles[i][j]) % 2 != 0):
                        # print("A ", i+1, state.poles[i][j], j+1)
                        state.cost = state.cost + (i+1)*state.poles[i][j]*(j+1)
                    else:
                        # print("B ", i+1, state.poles[i][j], j+1)
                        state.cost = state.cost - (i+1)*state.poles[i][j]*(j+1)
                else:
                    if (j == 0 and state.poles[i][j] % 2 != 0) or (j != 0 and (state.poles[i][j-1] - state.poles[i][j]) % 2 != 0):
                        # print("C ", i+1, state.poles[i][j], j+1)
                        state.cost = state.cost + (i+1)*state.poles[i][j]*(j+1)
                    else:
                        # print("D ", i+1, state.poles[i][j], j+1)
                        state.cost = state.cost - (i+1)*state.poles[i][j]*(j+1)
            else:
                if discs % 2 == 0:
                    if (j == 0 and state.poles[i][j] % 2 != 0) or (j != 0 and (state.poles[i][j-1] - state.poles[i][j]) % 2 != 0):
                        # print("E ", i+1, state.poles[i][j], j+1)
                        state.cost = state.cost + (i+1)*state.poles[i][j]*(j+1)
                    else:
                        # print("F ", i+1, state.poles[i][j], j+1)
                        state.cost = state.cost - (i+1)*state.poles[i][j]*(j+1)
                else:
                    if (j == 0 and state.poles[i][j] % 2 == 0) or (j != 0 and (state.poles[i][j-1] - state.poles[i][j]) % 2 != 0):
                        # print("G ", i+1, state.poles[i][j], j+1)
                        state.cost = state.cost + (i+1)*state.poles[i][j]*(j+1)
                    else:
                        # print("H ", i+1, state.poles[i][j], j+1)
                        state.cost = state.cost - (i+1)*state.poles[i][j]*(j+1)
            # print(state.cost)
    d = discs
    # print(state.poles)
    for j in range(len(state.poles[0])):
        if d == state.poles[0][j]:
            # print("j: ", state.poles[0][j])
            state.cost = state.cost - state.poles[0][j]*(j+1)
            d = d - 1

def cost2(state,discs):
    for i in range(0,3):
        for j in range(len(state.poles[i])):
            if i % 2 == 0:
                if discs % 2 == 0:
                    if (j == 0 and state.poles[i][j] % 2 == 0) or (j != 0 and (state.poles[i][j-1] - state.poles[i][j]) % 2 != 0):
                        # print("A ", i+1, state.poles[i][j], j+1)
                        state.cost = state.cost + (j+1)
                    else:
                        # print("B ", i+1, state.poles[i][j], j+1)
                        state.cost = state.cost - (j+1)
                else:
                    if (j == 0 and state.poles[i][j] % 2 != 0) or (j != 0 and (state.poles[i][j-1] - state.poles[i][j]) % 2 != 0):
                        # print("C ", i+1, state.poles[i][j], j+1)
                        state.cost = state.cost + (j+1)
                    else:
                        # print("D ", i+1, state.poles[i][j], j+1)
                        state.cost = state.cost - (j+1)
            else:
                if discs % 2 == 0:
                    if (j == 0 and state.poles[i][j] % 2 != 0) or (j != 0 and (state.poles[i][j-1] - state.poles[i][j]) % 2 != 0):
                        # print("E ", i+1, state.poles[i][j], j+1)
                        state.cost = state.cost + (j+1)
                    else:
                        # print("F ", i+1, state.poles[i][j], j+1)
                        state.cost = state.cost - (j+1)
                else:
                    if (j == 0 and state.poles[i][j] % 2 == 0) or (j != 0 and (state.poles[i][j-1] - state.poles[i][j]) % 2 != 0):
                        # print("G ", i+1, state.poles[i][j], j+1)
                        state.cost = state.cost + (j+1)
                    else:
                        # print("H ", i+1, state.poles[i][j], j+1)
                        state.cost = state.cost - (j+1)
            # print(state.cost)
    d = discs
    # print(state.poles)
    for j in range(len(state.poles[0])):
        if d == state.poles[0][j]:
            # print("j: ", state.poles[0][j], j)
            state.cost = state.cost - (j+1)
            # print(state.cost)
            d = d - 1

st = state()
discs = 3
st.poles = [[3,2,1],[],[]]
cost2(st,discs)

display(st)
ls = movegen(st)

for i in ls:
    cost2(i,discs)
    display(i)