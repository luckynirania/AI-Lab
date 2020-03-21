ls = input()
data = list(map(int, ls.split()))

N = len(data)

def test(p, n): 
    m = [[0 for x in range(n)] for x in range(n)] 
    for i in range(1, n): 
        m[i][i] = 0
         
    for L in range(2, n): 
        for i in range(1, n-L+1): 
            j = i+L-1
            m[i][j] = float('inf')
            for k in range(i, j): 
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j] 
                if q < m[i][j]: 
                    m[i][j] = q 
  
    return m[1][n-1] 

class NODE:
    contains = []
    cost = float('inf')
    sibling = None
    type = None
    parent = None
    children = []
    marked = None

def h_under(node):
    if len(node.contains) == 1:
        node.type = "terminal"
        return 0
    if len(node.contains) == 2:
        node.type = 'terminal'
        ref = node.contains[0]
        return data[ref] * data[ref + 1] * data[ref + 2]
    return data[node.contains[0]] * data[node.contains[-1] + 1]

def h_over(node):
    if len(node.contains) == 1:
        node.type = "terminal"
        return 0
    if len(node.contains) == 2:
        node.type = 'terminal'
        ref = node.contains[0]
        return data[ref] * data[ref + 1] * data[ref + 2]
    cost = N * data[node.contains[0]]
    for i in node.contains:
        cost = cost * data[i + 1]
    return cost

def gen_child(node):
    for i in range(1, len(node.contains)):
        baby_A = NODE()
        baby_B = NODE()

        baby_A.sibling = baby_B
        baby_B.sibling = baby_A

        baby_A.contains = node.contains[0:i]
        baby_B.contains = node.contains[i:]

        baby_A.parent = node
        baby_B.parent = node

        baby_A.cost = h_under(baby_A)
        baby_B.cost = h_under(baby_B)

        node.children.extend([baby_A, baby_B])
        

root = NODE()
root.contains = list(range(0, N - 1))
root.cost = h_under(root)

List = [root]

def revise(node):
    if node.type == 'terminal':
        node.type = 'solved'
        revise(node.parent)
        return
    
    mini = float('inf')
    old_marked = node.marked
    
    for i in range(0, len(node.children), 2):
        left = node.children[i]
        right = node.children[i].sibling

        # print(right == node.children[i + 1])

        cost = data[left.contains[0]] * data[right.contains[0]] * data[right.contains[-1] + 1]

        cost = cost + left.cost + right.cost

        if mini > cost:
            mini = cost
            node.marked = left

    node.cost = mini        

    if old_marked in List:
        List.remove(old_marked)

    if node.marked is not None:
        left = node.marked
        right = left.sibling
        if (left.cost >= right.cost or right.type == 'solved') and left.type != 'solved':
            List.append(left)
        if (right.cost >= left.cost or left.type == 'solved') and right.type != 'solved':
            List.append(right)
            
        if left.type == 'solved' and right.type == 'solved':
            node.type = 'solved'
            if node.parent is not None:
                revise(node.parent)

while root.type != 'solved':
    pick = List[0]
    List.remove(pick)

    if len(pick.children) == 0:
        gen_child(pick)

    revise(pick)

print('under ', root.cost, root.type) 
node = root
# while len(node.children) > 0:
#     for i in range(0, len(node.children), 2):
#         if node.children[i].type == 'solved':
#             print
print('dpsol ', test(data,N))