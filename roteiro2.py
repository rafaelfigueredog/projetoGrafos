from grafo_adj_nao_dir import *
from grafo import Grafo as G



def convertToMatrizAdj(g: G):
    N = g.N
    m = []
    coeficiente = 0
    for i in range(len(N)):
        lenVertices = len(N)
        linha = (coeficiente*['-']) + (lenVertices-coeficiente)*[0]
        coeficiente+=1
        m.append(linha)
    arestas = list(g.A.values())

    for i in range(len(arestas)):
        ligacao = arestas[i].split("-")
        indice1 = N.index(ligacao[0])
        indice2 = N.index(ligacao[1])

        if (indice1 <= indice2): 
            m[indice1][indice2] += 1
        else:
            m[indice2][indice1] += 1

    grafo = Grafo(N,m)

    return grafo

def vertices_nao_adjacentes(g: Grafo):
    listaNaoAdjacentes = []
    if ( len(g.N) == 0 ): 
        return listaNaoAdjacentes
    else:
        idxvertice = 0
        idxfinal = len(g.N)
        naoAdjacentes = ''
        for i in range(len(g.M)):
            for j in range(idxvertice, idxfinal):
                if (g.M[i][j] == 0):
                    naoAdjacentes = g.N[i] + "-" + g.N[j]
                    listaNaoAdjacentes.append(naoAdjacentes)
            idxvertice += 1
    return listaNaoAdjacentes

def ha_laco(g: Grafo):

    if (len(g.N) == 0):
        return False
    else:
        for i in range(len(g.N)):
            if (g.M[i][i] > 0):
                return True

    return False

def ha_paralelas(g: Grafo):

    if ( len(g.N) == 0 ): 
        return False
    else:
        idxvertice = 0
        idxfinal = len(g.N)
        naoAdjacentes = ''
        for i in range(len(g.M)):
            for j in range(idxvertice, idxfinal):
                if (g.M[i][j] > 1):
                    return True
            idxvertice += 1
    return False

    return

def grau(g: Grafo, vetice):
    
    print(Grafo)

    if ( len(g.N) == 0 ):
        return 0
    else:
        grau = 0
        idx = g.N.index(vetice)
        for i in range( idx, len(g.M[idx]) ):
            grau += g.M[idx][i]
        idxfixo = idx
        while ( (idx - 1) >= 0 ):
            if ( g.M[idx-1][idx] != str ):
                grau += g.M[idx-1][idxfixo]
            idx -= 1

    return grau

""" def arestas_sobre_vertice(g: Grafo, vetice):

    return """

def eh_completo(g: Grafo):
    
    if ( len(g.N) == 0 ): 
        return listaNaoAdjacentes
    else:
        idxvertice = 1
        idxfinal = len(g.N)
        naoAdjacentes = ''
        for i in range(len(g.M)):
            for j in range(idxvertice, idxfinal):
                if (g.M[i][j] == 0):
                    return False
            idxvertice += 1
    return True

def conexo(g: Grafo):



    pass


""" def main():

    g_p = G(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})
    g_p = convertToMatrizAdj(g_p)

    print(g_p)
    print(grau(g_p,"P")) 


main() """