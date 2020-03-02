import copy
import queue
class state:
    childs = []
    poles = [[],[],[]]
    visited = False
    explored = False
    parent = -1
    index = -1
    g = 0
    h = 0
    f = 0
    def __eq__(self,other):
        if(self.poles[0] == other.poles[0] and self.poles[1] == other.poles[1] and self.poles[2] == other.poles[2]):
            return True
        return False

state_set = []


def display(state):
    i = 0
    # print('Cost: ', state.cost)
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
                    if(len(state.poles[j]) == 0 or ((len(state.poles[j]) != 0) and (state.poles[j][-1] > state.poles[i][-1]))):
                        new = deepcopy(state)
                        new.poles[j].append(state.poles[i][-1])
                        del new.poles[i][-1]
                        if new not in state_set:
                            new.index = len(state_set)
                            state_set.append(new)
                        ls.append(state_set.index(new))
    return ls

def reconstruct_path(index):
    ls = [index]
    temp = index
    while(state_set[temp].parent != -1):
        # print(temp, end=" ")
        temp = state_set[temp].parent
        ls.append(temp)
    # ls = ls.reverse()
    # print()
    return ls
ref = 0
ref1 = 0
ref2 = 0

def cost(state):
    cost = 0
    for i in range(0,3):
        for j in state.poles[i]:
            cost = cost + (i+1)*j
    return cost

def cost1(state, discs, ref1):
    cost = 0
    for i in range(0,3):
        for j in range(len(state.poles[i])):
            if i % 2 == 0:
                if discs % 2 == 0:
                    if (j == 0 and state.poles[i][j] % 2 == 0) or (j != 0 and (state.poles[i][j-1] - state.poles[i][j]) % 2 != 0):
                        # print("A ", i+1, state.poles[i][j], j+1)
                        cost = cost + (i+1)*state.poles[i][j]*(j+1)
                    else:
                        # print("B ", i+1, state.poles[i][j], j+1)
                        cost = cost - (i+1)*state.poles[i][j]*(j+1)
                else:
                    if (j == 0 and state.poles[i][j] % 2 != 0) or (j != 0 and (state.poles[i][j-1] - state.poles[i][j]) % 2 != 0):
                        # print("C ", i+1, state.poles[i][j], j+1)
                        cost = cost + (i+1)*state.poles[i][j]*(j+1)
                    else:
                        # print("D ", i+1, state.poles[i][j], j+1)
                        cost = cost - (i+1)*state.poles[i][j]*(j+1)
            else:
                if discs % 2 == 0:
                    if (j == 0 and state.poles[i][j] % 2 != 0) or (j != 0 and (state.poles[i][j-1] - state.poles[i][j]) % 2 != 0):
                        # print("E ", i+1, state.poles[i][j], j+1)
                        cost = cost + (i+1)*state.poles[i][j]*(j+1)
                    else:
                        # print("F ", i+1, state.poles[i][j], j+1)
                        cost = cost - (i+1)*state.poles[i][j]*(j+1)
                else:
                    if (j == 0 and state.poles[i][j] % 2 == 0) or (j != 0 and (state.poles[i][j-1] - state.poles[i][j]) % 2 != 0):
                        # print("G ", i+1, state.poles[i][j], j+1)
                        cost = cost + (i+1)*state.poles[i][j]*(j+1)
                    else:
                        # print("H ", i+1, state.poles[i][j], j+1)
                        cost = cost - (i+1)*state.poles[i][j]*(j+1)
            # print(state.cost)
    d = discs
    # print(state.poles)
    for j in range(len(state.poles[0])):
        if d == state.poles[0][j]:
            # print("j: ", state.poles[0][j])
            cost = cost - state.poles[0][j]*(j+1)
            d = d - 1
    if ref1 > 0:
        cost = ref1 - cost
    return cost

def cost2(state, discs, ref2):
    cost = 0
    for i in range(0,3):
        for j in range(len(state.poles[i])):
            if i % 2 == 0:
                if discs % 2 == 0:
                    if (j == 0 and state.poles[i][j] % 2 == 0) or (j != 0 and (state.poles[i][j-1] - state.poles[i][j]) % 2 != 0):
                        # print("A ", i+1, state.poles[i][j], j+1)
                        cost = cost + (j+1)
                    else:
                        # print("B ", i+1, state.poles[i][j], j+1)
                        cost = cost - (j+1)
                else:
                    if (j == 0 and state.poles[i][j] % 2 != 0) or (j != 0 and (state.poles[i][j-1] - state.poles[i][j]) % 2 != 0):
                        # print("C ", i+1, state.poles[i][j], j+1)
                        cost = cost + (j+1)
                    else:
                        # print("D ", i+1, state.poles[i][j], j+1)
                        cost = cost - (j+1)
            else:
                if discs % 2 == 0:
                    if (j == 0 and state.poles[i][j] % 2 != 0) or (j != 0 and (state.poles[i][j-1] - state.poles[i][j]) % 2 != 0):
                        # print("E ", i+1, state.poles[i][j], j+1)
                        cost = cost + (j+1)
                    else:
                        # print("F ", i+1, state.poles[i][j], j+1)
                        cost = cost - (j+1)
                else:
                    if (j == 0 and state.poles[i][j] % 2 == 0) or (j != 0 and (state.poles[i][j-1] - state.poles[i][j]) % 2 != 0):
                        # print("G ", i+1, state.poles[i][j], j+1)
                        cost = cost + (j+1)
                    else:
                        # print("H ", i+1, state.poles[i][j], j+1)
                        cost = cost - (j+1)
            # print(cost)
    d = discs
    # print(state.poles)
    for j in range(len(state.poles[0])):
        if d == state.poles[0][j]:
            # print("j: ", state.poles[0][j], j)
            cost = cost - (j+1)
            # print(state.cost)
            d = d - 1
    if ref2 > 0:
        cost = ref2 - cost
    return cost

start = state()
goal = state()

discs = int(input())

def PropagateImprovement(m):
    neighbours = movegen(m)
    for index in neighbours:
        s = state_set[index]
        new_g = m.g + s.h - m.h
        if new_g < s.g:
            s.parent = m.index
            s.g = new_g
            if s.index in CLOSED:
                PropagateImprovement(s)

for heuristic in range(2,-1,-1):
    if heuristic == 0:
        print("heuristic : monotone ")
    if heuristic == 1:
        print("heuristic : over estimate")
    if heuristic == 2:
        print("heuristic : under estimate")
    ls = []
    for i in range(0,discs):
        ls.append(i+1)

    ls.reverse()

    start.poles = [ls,[],[]]
    start.parent = -1
    goal.poles = [[],[],ls]

    state_set.append(start)
    start.index = 0

    state_set.append(goal)
    goal.index = 1

    ref = cost(goal)
    ref1 = cost1(goal, discs, ref1)
    ref2 = cost2(goal, discs, ref2)

    # print(cost(start,discs, ref), cost(goal,discs, ref))
    # print(cost1(start, discs, ref1), cost1(goal, discs, ref1))
    # print(cost2(start, discs, ref2), cost2(goal, discs, ref2))
    # print()

    # display(start)

    OPEN = []
    CLOSED = []
    if heuristic == 0:
        start.h = cost(start)
    if heuristic == 1:
        start.h = cost1(start,discs,ref1)
    if heuristic == 2:
        start.h = cost2(start,discs,ref2)

    start.f = start.h
    OPEN.append(start.index)

    path = []

    while(len(OPEN) != 0):
        OPEN.sort(key=lambda x: state_set[x].f)
        # print(OPEN)
        n = OPEN[0]
        # print("loki - ",len(OPEN))
        del OPEN[0]
        # print(n, goal.index)
        if n == goal.index:
            CLOSED.append(n)
            print("goal reached")
            path = reconstruct_path(n)
            break
        n = state_set[n]
        neighbours = movegen(n)
        
        CLOSED.append(n.index)
        for m in neighbours:
            m = state_set[m]
            # print((cost(m) - cost(n)), " ---- ", (m.h - n.h))
            if heuristic == 0:
                costi =  (m.h - n.h) + 1
            else:
                costi = (m.h - n.h)
            if m.index in OPEN:
                # print("in op")
                if(m.g > n.g + costi):
                    m.parent = n.index
                    m.g = n.g + costi
                    m.f = m.g + m.h
            if m.index in CLOSED:
                # print("in clo")
                if(m.g > n.g + costi):
                    m.parent = n.index
                    m.g = n.g + costi
                    m.f = m.g + m.h
                    if heuristic != 0:
                        PropagateImprovement(m)
            if m.index not in OPEN and m.index not in CLOSED:
                # print("not op not clo")
                if heuristic == 0:
                    m.h = cost2(m,discs,ref2)
                if heuristic == 1:
                    m.h = cost1(m,discs,ref1)
                if heuristic == 2:
                    m.h = cost2(m,discs,ref2)
                # m.h = cost1(m,discs,ref1)
                m.parent = n.index
                m.g = n.g + (m.h - n.h)
                m.f = m.g + m.h
                OPEN.append(m.index)

    path.reverse()

    print("length of path = ", len(path))
    print(path)
    print("-----------------------------------------------------")