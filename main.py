import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


def ler_grafo_de_arquivo(nome_arquivo):
    G = nx.Graph()
    with open(nome_arquivo, 'r') as arquivo:
        tipo = int(arquivo.readline())
        numero_vertices = int(arquivo.readline())
        for i in range(numero_vertices):
            vertice = arquivo.readline().split(" ")[0]
            inserir_vertice(G, vertice)

        numero_arestas = int(arquivo.readline())
        for i in range(numero_arestas):
            arestas = arquivo.readline().split(" ")[0]
            G.add_edge(arestas[0], arestas[1])
    return G
  
def gravar_grafo_em_arquivo(G, nome_arquivo,lista):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write('4\n')
        arquivo.write(f'{len(G.nodes())}\n')
        for i in lista:
            arquivo.write(f'{i[0]} {i[1]}\n')
            for k in range(20):
                arquivo.write(f'{i[0]}{k} {i[1]} Pergunta {k+1}\n')
        arquivo.write(f'{len(G.edges())}\n')
        for aresta in G.edges():
            arquivo.write(f'{aresta[0]} {aresta[1]}\n')

def inserir_vertice(G, vertice):
    G.add_node(vertice)

def inserir_aresta(G, aresta):
    G.add_edge(*aresta)

def remover_vertice(G, vertice):
    G.remove_node(vertice)

def remover_aresta(G, aresta):
    G.remove_edge(*aresta)

def mostrar_conteudo_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        print(arquivo.read())

def mostrar_grafo(G):
    print("Vértices do grafo:", G.nodes())
    print("Arestas do grafo:", G.edges())

def verificar_conexidade(G):
    if nx.is_connected(G):
        print("O grafo é conexo.")
    else:
        print("O grafo não é conexo.")
    componentes = nx.connected_components(G)
    print("Componentes conectados:", list(componentes))

def CarregarGrafo(G):
  vertices_principais = [["A","Initial Summary"],["B","Initial Report"],["C","Personas"],["D","Marketing Report"],["E","Operational Report"],["F","Final Report"]]
  for vertice in vertices_principais:
    inserir_vertice(G, vertice[0])
    for i in range(20):
      inserir_vertice(G, vertice[0]+str(i+1))
  p=0
  for vertice in vertices_principais:
    for i in range(20):
      if i == 0:
        inicio = vertice[0]
        final = vertice[0]+str(i+1)
      else:
        inicio = vertice[0]+str(i)
        final = vertice[0]+str(i+1)
      inserir_aresta(G, [inicio,final])

  inserir_aresta(G, [vertices_principais[0][0]+str(20),vertices_principais[1][0]])
  inserir_aresta(G, [vertices_principais[1][0]+str(20),vertices_principais[2][0]])
  inserir_aresta(G, [vertices_principais[1][0]+str(20),vertices_principais[3][0]])
  inserir_aresta(G, [vertices_principais[1][0]+str(20),vertices_principais[4][0]])
  inserir_aresta(G, [vertices_principais[4][0]+str(20),vertices_principais[5][0]])
  return G
  
def menu():
    G = nx.Graph()
    vertices_principais = [["A","Initial Summary"],["B","Initial Report"],["C","Personas"],["D","Marketing Report"],["E","Operational Report"],["F","Final Report"]]
    G = CarregarGrafo(G)  
        
    nome_arquivo = 'grafo.txt'
    while True:
        print("\nMenu:")
        print("a) Ler dados do arquivo grafo.txt")
        print("b) Gravar dados no arquivo grafo.txt")
        print("c) Inserir vértice")
        print("d) Inserir aresta")
        print("e) Remover vértice")
        print("f) Remover aresta")
        print("g) Mostrar conteúdo do arquivo")
        print("h) Mostrar grafo")
        print("i) Verificar conexidade do grafo")
        print("j) Plotar grafo")
        print("k) Matriz de adjacência")
        print("l) Encerrar a aplicação")
        opcao = input("Escolha uma opção: ")

        if opcao == 'a':
            G = ler_grafo_de_arquivo(nome_arquivo)
        elif opcao == 'b':
            gravar_grafo_em_arquivo(G, nome_arquivo,vertices_principais)
        elif opcao == 'c':
            vertice = input("Insira o vértice: ")
            inserir_vertice(G, vertice)
        elif opcao == 'd':
            aresta = input("Insira a aresta (formato v1,v2): ").split(',')
            inserir_aresta(G, aresta)
        elif opcao == 'e':
            vertice = input("Vertice a remover: ")
            remover_vertice(G, vertice)
        elif opcao == 'f':
            aresta = input("Aresta a remover (formato v1,v2): ").split(',')
            remover_aresta(G, aresta)
        elif opcao == 'g':
            mostrar_conteudo_arquivo(nome_arquivo)
        elif opcao == 'h':
            mostrar_grafo(G)
        elif opcao == 'i':
            verificar_conexidade(G)
        elif opcao == 'j':
          nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, edge_color='k')
          plt.show()
        elif opcao == 'k':
          matriz_adj = nx.adjacency_matrix(G)
          matriz_adj = matriz_adj.toarray()
          print(matriz_adj)
        elif opcao == 'l':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()