import json
import timeit

def ReadJson():
    with open('../Graph_districts.json', 'r', encoding='utf8') as f:
        return json.load(f)

def custoTotal(graph, ciclo):
    custo = 0
    for i,vertice in enumerate(ciclo):
        if i < len(ciclo)-1:
            custo += graph[vertice][ciclo[i+1]]

    return custo

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
    inicio = timeit.default_timer()
    ciclo = VMP(graph)
    tempo = timeit.default_timer() - inicio
    custo = custoTotal(graph, ciclo)
    print("Melhor rota: ", ciclo)
    print("Custo do ciclo: ", custo)
    print("Tempo de execução: ", "%.7f" % (float(tempo)), "ms")