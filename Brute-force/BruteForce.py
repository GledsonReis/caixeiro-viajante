import itertools
import json

# lê o grafo a partir do arquivo json Graph_districts.json
def ReadJson():
    with open('Graph_districts.json', 'r', encoding='utf8') as f:
        return json.load(f)

def CaixeiroViajante(graph):
    # gera todas as permutações de vertices
    routes = itertools.permutations(graph)

    # inicializa a o melhor caminho com um arrey vazio
    melhor_caminho = []
    quant_vert = graph.__len__()
    # inicializa o menor custo com -1 indicando que o custo de nenhum caminho foi verificado
    menor_custo = -1

    # itera sobre todos as permutacões de vertices
    for route in routes:  
        custo = 0       # variavel para contar o custo da rota da iteração atual
        last = -1       # variavel para salvar o ultimo vertice da permutação adicionado ao caminho atual
        first = ""      # variavel para salvar o vertice inicial do caminho atual
        caminho = []    # variavel para salvar o caminho atual

        # se o vertice incial não for ponto de partida no caso a universidade passa pa
        if(list(route)[0] != 'A'):
            continue

        # itera por cada vertice da permutação
        for district in route:
            # se for o primeiro vertice da permutação inicializa as variaveis de controle a 
            # adiciona-o ao caminho atual
            if(last == -1):
                first = district
                last = district
                caminho.append(district)
                continue

            # procura na lista de arestas do vertice atual de iteração somando seu valor a 
            # custo e adicionando-o ao caminho atual e atualizando a variavel de controle last
            for i,key_district in enumerate(graph):
                if(graph[district][i] > 0 and graph[key_district] == graph[last]):
                    last = district
                    caminho.append(district)
                    custo += int(graph[district][i])
                    break
            
            # verifica se o tamanho do caminho atual já é igual ao numero de vertices
            #   se soma a custo o valor da aresta do primeiro com o ultimo vértice e o adiciona o 
            #   vertice inicial no fim do caminhao
            if(len(caminho) == quant_vert):
                caminho.append(caminho[0])
                custo += int(graph[district][list(graph.keys()).index(first)])
                # se for a primeira permutação, o menor custo recebe custo do caminho atual e
                # salva o caminho atual como o melhor caminho
                if (menor_custo == -1):
                    menor_custo = custo
                    caminho.append(custo)
                    melhor_caminho = caminho
                    continue
                # se o custo atual for menor que o menor custo atualiza o menor custo e melhor caminho
                if (custo < menor_custo):
                    menor_custo = custo
                    caminho.append(custo)
                    melhor_caminho = caminho 

    return melhor_caminho

if __name__ == '__main__':
    graph = ReadJson()
    district_routes = CaixeiroViajante(graph)
    print(district_routes)