import itertools
import json
import timeit

# lê o grafo a partir do arquivo json Graph_districts.json
def ReadJson():
    with open('../Graph_districts.json', 'r', encoding='utf8') as f:
        return json.load(f)

# Calcula o Custo do Ciclo
def custoTotal(graph, ciclo):
    custo = 0
    for i,vertice in enumerate(ciclo):
        if i < len(ciclo)-1:
            custo += graph[vertice][ciclo[i+1]]

    return custo

def CaixeiroViajante(graph):
    # gera todas as permutações de vertices
    rotas = itertools.permutations(range(len(graph)))

    # inicializa a o melhor caminho com um arrey vazio
    melhor_caminho = []
    quant_vert = graph.__len__()
    # inicializa o menor custo com -1 indicando que o custo de nenhum caminho foi verificado
    menor_custo = -1

    # itera sobre todos as permutacões de vertices
    for rota in rotas:  
        custo = 0       # variavel para contar o custo da rota da iteração atual
        last = -1       # variavel para salvar o ultimo vertice da permutação adicionado ao caminho atual
        caminho = []    # variavel para salvar o caminho atual

        # se o vertice incial não for ponto de partida no caso a universidade, passa para a próxima permutação
        if(rota[0] != 0):
            continue

        # itera por cada vertice da permutação
        for vertice in rota:

            # adiciona o veritice ao caminho atual
            caminho.append(vertice)
            # se não for o primeiro vertice soma o custo da aresta entre o vertice atual e o anterio ao custo atual
            if(last != -1):
                custo += graph[vertice][last]
            
            # atualiza last com o vertice atual
            last = vertice

            
            # verifica se o tamanho do caminho atual já é igual ao numero de vertices
            #   se soma a custo o valor da aresta do primeiro com o ultimo vértice e o adiciona o 
            #   vertice inicial no fim do caminhao
            # print("Custo: ", custo)
            if(len(caminho) == quant_vert):
                caminho.append(caminho[0])
                custo += graph[vertice][caminho[0]]
                # se for a primeira permutação, o menor custo recebe custo do caminho atual e
                # salva o caminho atual como o melhor caminho
                if (menor_custo == -1):
                    menor_custo = custo
                    melhor_caminho = caminho
                    continue
                # se o custo atual for menor que o menor custo atualiza o menor custo e melhor caminho
                if (custo < menor_custo):
                    menor_custo = custo
                    melhor_caminho = caminho

    return melhor_caminho

if __name__ == '__main__':
    graph = ReadJson()
    inicio = timeit.default_timer()
    ciclo = CaixeiroViajante(graph)
    tempo = timeit.default_timer() - inicio
    custo = custoTotal(graph, ciclo)
    print("Melhor rota: ", ciclo)
    print("Custo do ciclo: ", custo)
    print("Tempo de execução: ", "%.7f" % (float(tempo)), "ms")