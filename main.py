#Integrantes: Livia Hombre e Thiago Fabiano


import pickle
import gerarConexoes
import estatisticas
def main():
    with open("backup.bin", "rb") as file:
        usuarios = pickle.load(file);
        conexoes = pickle.load(file);
        historico = pickle.load(file);
    
    gerarConexoes.gerarConexoes(historico, conexoes, usuarios)
    
    logins = estatisticas.estatisticas(usuarios, conexoes)

    quickSort(logins, 0, len(logins) - 1, usuarios, conexoes)
    listaCidadeUsuario = []
    for i in logins:
        listaCidadeUsuario.append((usuarios[i][1], usuarios[i][0]))
    melhorDeCadaCidade = []
    for index in range(len(listaCidadeUsuario)-1):
        if index != 0:
            if listaCidadeUsuario[index][0] != listaCidadeUsuario[index-1][0]:
                melhorDeCadaCidade.append(listaCidadeUsuario[index])
        else: melhorDeCadaCidade.append(listaCidadeUsuario[index])
    
    f = open("top.txt", "w")
    for i in melhorDeCadaCidade:
        f.write(f"{i[0]} {i[1]}\n")




def anterior(x,y, usuarios, conexoes_atualizadas):

    if(usuarios[x][1] < usuarios[y][1]): return True
    if(usuarios[x][1] > usuarios[y][1]): return False

    if((len(conexoes_atualizadas[x][1]) + len(conexoes_atualizadas[x][2])) > (len(conexoes_atualizadas[y][1]) + len(conexoes_atualizadas[y][2]))): return True
    if((len(conexoes_atualizadas[x][1]) + len(conexoes_atualizadas[x][2])) < (len(conexoes_atualizadas[y][1]) + len(conexoes_atualizadas[y][2]))): return False

    if( x < y): 
        return True 

    return False

def particao(l, inf , sup, usuarios, conexoes_atualizadas ): # inf sup primeiro e ultimo item
    pivot = l[inf]
    i = inf +1
    j = sup

    while i <= j:
        while i <= j and anterior( l[i] , pivot , usuarios, conexoes_atualizadas):
            i += 1
        while j >= i and not anterior( l[j] , pivot , usuarios, conexoes_atualizadas):
            j -= 1

        if i < j: l[i], l[j] = l[j], l[i]

    l[inf], l[j] = l[j], l[inf]
    return j
    
def quickSort(l, inf , sup , usuarios, conexoes_atualizadas ):
    if inf < sup: 
        pos = particao(l, inf , sup , usuarios, conexoes_atualizadas)
        quickSort(l, inf, pos-1, usuarios, conexoes_atualizadas)
        quickSort(l, pos+1, sup, usuarios, conexoes_atualizadas)
        
if __name__ == "__main__":
    main()


