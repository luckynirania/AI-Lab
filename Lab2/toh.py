import copy
class state:
    childs = set()
    poles = [[],[],[]]

def d_s(state):
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

adj_list = []

node = state()

discs = 3
ls = []
for i in range(0,discs):
    ls.append(discs - i)
node.poles = [ls,[],[]]

adj_list.append(node)

size = 0
while(size != len(adj_list)):
    size = len(adj_list)
    for l in range(0,size):
        ref_state = adj_list[l]
        # Pole i -> j
        for i in range(0,3):
            for j in range(0,3):
                if(i != j):
                    if(len(ref_state.poles[i]) != 0):
                        if(len(ref_state.poles[j]) == 0) or (ref_state.poles[j][-1] > ref_state.poles[i][-1]):
                            temp = deepcopy(ref_state)
                            temp.poles[j].append(temp.poles[i][-1])
                            temp.poles[i].pop()
                            ind = -1
                            r = 0
                            for x in adj_list:
                                if(x.poles == temp.poles):
                                    ind = r
                                    break
                                r = r + 1
                            if(ind < 0):
                                ind = len(adj_list)
                                adj_list.append(temp)
                            ref_state.childs.add(ind)

# for x in adj_list:
#     print(x.childs)
#     d_s(x)