import copy
import time
class state:
    h_value = 0
    poles = [[],[],[]]
    parent = 0
    def __eq__(self,other):
        return self.poles == other.poles
    def disp(self):
        i = 0
        for pole in self.poles:
            print(i," --> ",pole)
            i = i + 1
        print() 

start = state()
discs = 3
ls = []
for i in range(0,discs):
    ls.append(discs - i)
start.poles = [ls,[],[]]
# start.disp()

goal = state()
goal.poles = [[],[],ls]
# goal.disp()

hue = -1

def movegen(STATE):
    ls = []
    for i in range(0,3):
        for j in range(0,3):
            if(i != j):
                node = state()
                node.h_value = STATE.h_value
                node.poles = copy.deepcopy(STATE.poles)
                if(len(node.poles[i]) != 0):
                    if((len(node.poles[j]) == 0) or (node.poles[j][-1] > node.poles[i][-1])):
                        temp = node.poles[i][-1] 
                        node.poles[i].pop()
                        node.poles[j].append(temp)
                        if(hue == 1):
                            node.h_value = heuristic_1(node)
                        if(hue == 2):
                            node.h_value = heuristic_2(node)
                        ls.append(node)
    return ls

def goaltest(TEST):
    if TEST.poles == goal.poles:
        return True
    return False

h1_offset = 3 * ((discs)*(discs + 1)) / 2
h2_offset = 3 * ((discs)*(discs + 1)) / 2

def heuristic_1(node):
    value = 0
    for i in range(0,3):
        for j in range(0,len(node.poles[i])):
            value = value + ((i + 1) * node.poles[i][j])
    return h1_offset - value

def heuristic_2(node):
    value = 0
    for i in range(0,3):
        for j in range(0,len(node.poles[i])):
            value = value + ((i + 1) * node.poles[i][j])
    return value

# BFS

print("BEST FIRST SEARCH\n")
for q in range(0,3):
    hue = q

    OPEN = []
    CLOSED = []

    OPEN.append(start)
    states = 1
    path = []
    while(len(OPEN) != 0):
        temp = OPEN[0]
        CLOSED.append(temp)
        if(goaltest(temp)):
            break
        del OPEN[0]
        states = states + 1
        neighbours = movegen(temp)
        new_list = list(item for item in neighbours if (item not in CLOSED) and (item not in OPEN))
        for item in new_list:
            item.parent = len(CLOSED) - 1
        OPEN.extend(new_list)
        OPEN.sort(key=lambda x: x.h_value)

    path = []
    path.append(CLOSED[-2])

    while(path[-1] != start):
        path.append(CLOSED[path[-1].parent])
        
    path.reverse()
    path.append(goal)

    if(hue == 0):
        print("No Heuristic\t",states,"\t",len(path))
    else:
        print("Heuristic ",hue,"\t",states,"\t",len(path))

    # for item in path:
    #     item.disp()

print("\n")

# Hill Climb

print("HILL CLIMB")
hue = 1

node = start
node.h_value = heuristic_1(start)
neighbours = movegen(node)
neighbours.sort(key=lambda x: x.h_value)

new_node = neighbours[0]
print(node.h_value," ",new_node.h_value)
new_node.disp()


while(node.h_value > new_node.h_value):
        node = new_node

        neighbours = movegen(node)
        neighbours.sort(key=lambda x: x.h_value)
        
        new_node = neighbours[0]
        print(node.h_value," ",new_node.h_value)
        new_node.disp()
