import copy
import queue
class state:
    childs = []
    poles = [[],[],[]]
    visited = False
    explored = False
    parent = 0
    g = 0
    h = 0
    f = 0
    def __eq__(self,other):
        if(self.poles[0] == other.poles[0] and self.poles[1] == other.poles[1] and self.poles[2] == other.poles[2]):
            return True
        return False


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
                    if(len(state.poles[j]) == 0 or ((len(state.poles[j]) != 0) and (state.poles[j] > state.poles[i]))):
                        new = deepcopy(state)
                        new.poles[j].append(state.poles[i][-1])
                        del new.poles[i][-1]
                        ls.append(new)
    return ls

def reconstruct_path(state):
    ls = [state]
    temp = state
    while(temp.parent != temp):
        ls.append(temp.parent)
        temp = temp.parent
    # ls = ls.reverse()
    return ls

def cost(state,discs):
    cost = 0
    for i in range(0,3):
        for j in state.poles[i]:
            cost = cost + (i+1)*j
    if discs == 1:
        cost = 3 - cost
    if discs == 2:
        cost = 9 - cost
    if discs == 3:
        cost = 18 - cost
    if discs == 4:
        cost = 30 - cost
    if discs == 5:
        cost = 45 - cost
    if discs == 6:
        cost = cost
    if discs == 7:
        cost = cost
    if discs == 8:
        cost = cost    
    return cost

def cost1(state, discs):
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
    if discs == 1:
        cost = 3 - cost
    if discs == 2:
        cost = 12 - cost
    if discs == 3:
        cost = 30 - cost
    if discs == 4:
        cost = 60 - cost
    if discs == 5:
        cost = 105 - cost
    if discs == 6:
        cost = cost
    if discs == 7:
        cost = cost
    if discs == 8:
        cost = cost  
    return cost

def cost2(state,discs):
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
    if discs == 1:
        cost = 1 - cost
    if discs == 2:
        cost = 3 - cost
    if discs == 3:
        cost = 6 - cost
    if discs == 4:
        cost = 10 - cost
    if discs == 5:
        cost = 15 - cost
    if discs == 6:
        cost = cost
    if discs == 7:
        cost = cost
    if discs == 8:
        cost = cost  
    return cost

start = state()
goal = state()

discs = int(input())

ls = []
for i in range(0,discs):
    ls.append(i+1)

ls.reverse()

start.poles = [ls,[],[]]
start.parent = start
goal.poles = [[],[],ls]

print(cost(start,discs), cost(goal,discs))
print(cost1(start,discs), cost1(goal,discs))
print(cost2(start,discs), cost2(goal,discs))
print()

# ls = movegen(start)

# for i in ls:
#     print(cost(i,discs))
#     display(i)

OPEN = []
CLOSED = []

def PropagateImprovement(m):
    neighbours = movegen(m)
    for s in neighbours:
        if s in OPEN:
            s = OPEN[OPEN.index(s)]
            new_g = m.g + s.h - m.h
            if new_g < s.g:
                s.parent = m
                s.g = new_g
                if s in CLOSED:
                    PropagateImprovement(s)
        if s in CLOSED:
            s = CLOSED[CLOSED.index(s)]
            new_g = m.g + s.h - m.h
            if new_g < s.g:
                s.parent = m
                s.g = new_g
                if s in CLOSED:
                    PropagateImprovement(s)

start.h = cost1(start,discs)
start.f = start.h
OPEN.append(start)

path = []

while(len(OPEN) != 0):
    OPEN.sort(key=lambda x: x.h)
    n = OPEN[0]
    del OPEN[0]
    if n == goal:
        print("goal reached")
        path = reconstruct_path(n)
        break
    neighbours = movegen(n)
    CLOSED.append(n)
    for m in neighbours:
        if m in OPEN:
            m = OPEN[OPEN.index(m)]
            # print("in op")
            if(m.g > n.g + (m.h - n.h)):
                m.parent = n
                m.g = n.g + (m.h - n.h)
                m.f = m.g + m.h
        if m in CLOSED:
            m = CLOSED[CLOSED.index(m)]
            # print("in clo")
            if(m.g > n.g + (m.h - n.h)):
                m.parent = n
                m.g = n.g + (m.h - n.h)
                m.f = m.g + m.h
                PropagateImprovement(m)
        if m not in OPEN and m not in CLOSED:
            # print("not op not clo")
            m.h = cost1(m,discs)
            m.parent = n
            m.g = n.g + (m.h - n.h)
            m.f = m.g + m.h
            OPEN.append(m)
path.reverse()

for item in path:
    display(item)

print("length of path = ", len(path))
