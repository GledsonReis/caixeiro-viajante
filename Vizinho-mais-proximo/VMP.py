import json

def ReadJson():
    with open('Graph_districts.json', 'r', encoding='utf8') as f:
        return json.load(f)

def menorVerticeAdjacente(u, graph, Q):
    custo = -1
    vertice = -1
    for i in Q:
        if custo == -1 and vertice != u:
            custo = graph[u][i]
            vertice = i
            continue
        if custo > graph[u][i] and vertice != u:
            custo = graph[u][i]
            vertice = i

    print(custo)
    return vertice

def VMP(graph):
    u = 0
    S = [u]
    Q = list(range(len(graph)))
    Q.remove(u)

    while len(Q) != 0:
        v = menorVerticeAdjacente(u, graph, Q)
        S.append(v)
        Q.remove(v)
        u = v

    S.append(S[0])
    return S

if __name__ == '__main__':
    graph = ReadJson()
    ciclo = VMP(graph)
    print(ciclo)