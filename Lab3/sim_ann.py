import math
import random

euc = True
file_name = input()
data = open(file_name)
data = data.read()
data = data.split("\n")

if data[0] != "euclidean":
    euc = False
n = int(data[1])

class cities:
    index = int(0)
    x = int(0)
    y = int(0)
    distance = []

city = []

for i in range(0,100):
    temp = cities()
    row = data[i + 2].split()
    temp.x = float(row[0])
    temp.y = float(row[1])
    temp.index = int(i)
    temp.distance = data[i + n + 2].split()
    city.append(temp)
    
def delta_E(a,b):
    return(float(a.distance[b.index]))

def prob(E,T):
    return( 1 / ( 1 + ( math.exp( (-1)*(E)/(T) ) ) ) )

T = 9999
pos = 0       # start from jth city

T_list = []
path = []

while(T > 0):       # varying T from 500 to 1
    pos = 0
    visited = []
    path_length = float(0)
    for i in range(0,99):
        visited.append(pos)
        while(True):
            while(True):
                dest = random.randrange(0,100,1)
                if(dest not in visited):
                    break        

            prob_dest = prob(delta_E(city[pos],city[dest]),T)
            prob_mine = random.random()
            if(prob_dest > prob_mine):
                path_length = path_length + float(city[pos].distance[dest])
                pos = dest
                break

    T_list.append(path_length)
    path.append(visited)
    print("T: ",T," ",visited,"\t",path_length)
    T = T - 1

temp = min(T_list)
print(T_list.index(temp),"\t",temp)
# print("Path\t",path[T_list.index(temp)])













# print("Start\tT\tpath")
# for j in range(0,100):
#     T = 9999
#     pos = j        # start from jth city

#     T_list = []

#     while(T > 0):       # varying T from 500 to 1
#         visited = []
#         path_length = float(0)
#         for i in range(0,99):
#             visited.append(pos)
#             while(True):
#                 while(True):
#                     dest = random.randrange(0,100,1)
#                     if(dest not in visited):
#                         break        

#                 prob_dest = prob(delta_E(city[pos],city[dest]),T)
#                 prob_mine = random.random()
#                 if(prob_dest > prob_mine):
#                     path_length = path_length + float(city[pos].distance[dest])
#                     pos = dest
#                     break

#         T_list.append(path_length)
#         # print("T: ",T," ",path_length)
#         T = T - 1

#     temp = min(T_list)
#     print(j,"\t",T_list.index(temp),"\t",temp)