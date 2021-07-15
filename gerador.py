import random
graph = []
chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
n = 12

for i in range(n):
    graph.append([])
    for j in range(n):
         graph[i].append(0)

for i in range(n):
    for j in range(i, n):
        if i != j and graph[i][j] == 0:
            x = random.randrange(1,20,1)
            graph[i][j] = x
            graph[j][i] = x
        else:
            graph[i][j] = 0


for g in graph:
    print(str(g)+",")

# for i, g in enumerate(graph):
#     print("\""+str(chars[i])+"\":"+str(g)+",")
