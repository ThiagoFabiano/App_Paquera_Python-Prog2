import pickle

def main():
    with open("backup.bin", "rb") as file:
        usuarios = pickle.load(file);
        conexoes = pickle.load(file);
        historico = pickle.load(file);
    
    conexoes_atualizadas = gerarConexoes(historico, conexoes)

    with open('dados.bin', 'wb') as file:
        pickle.dump(usuarios, file)
        pickle.dump(conexoes_atualizadas, file) 
    
    estatisticas(usuarios,  conexoes_atualizadas)


def gerarConexoes(historico, conexoes):
    for conexao in historico:
        #Verificações: 
        # 1 - verifica se a conexao ja esta no gostei de quem curtiu se não ta adiciona
        if conexao[1] not in conexoes[conexao[0]][0] :
            conexoes[conexao[0]][0].append(conexao[1])
        # 2 - verifica se a conexao ja esta no gostou de quem foi curtido
        if conexao[0] not in conexoes[conexao[1]][1]:
            conexoes[conexao[1]][1].append(conexao[0])
        # 3 - verifica se os dois se curtiram
        if conexao[1] in conexoes[conexao[0]][1] and conexao[0] in conexoes[conexao[1]][1]:
            #verifica se esta no mutuo de um
            if conexao[1] in conexoes[conexao[0]][2]:
                #se esta no mutuo remove do gostei e gostou
                    conexoes[conexao[0]][0].remove(conexao[1])
                    conexoes[conexao[0]][1].remove(conexao[1])                     
            else:
                # se não, remove e adiciona
                conexoes[conexao[0]][0].remove(conexao[1])
                conexoes[conexao[0]][1].remove(conexao[1])  
                conexoes[conexao[0]][2].append(conexao[1])
            # o mesmo pra quem foi curtido
            if conexao[0] in conexoes[conexao[1]][2]:
                #se esta no mutuo remove do gostei e gostou
                    conexoes[conexao[1]][0].remove(conexao[0])
                    conexoes[conexao[1]][1].remove(conexao[0])                     
            else:
                # se não, remove e adiciona
                conexoes[conexao[1]][0].remove(conexao[0])
                conexoes[conexao[1]][1].remove(conexao[0])  
                conexoes[conexao[1]][2].append(conexao[0])
    return conexoes;

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
    
    


def estatisticas(usuarios,  conexoes_atualizadas):
    logins = list(usuarios.keys())
    
    quickSort(logins, 0, len(logins) - 1, usuarios, conexoes_atualizadas)
    print(f"{len(logins)}")
    listaCidadeUsuario = []
    for i in logins:
        listaCidadeUsuario.append((usuarios[i][1], usuarios[i][0]))
    melhorDeCadaCidade = []
    for index in range(len(listaCidadeUsuario)-1):
        if index != 0:
            if listaCidadeUsuario[index][0] != listaCidadeUsuario[index-1][0]:
                melhorDeCadaCidade.append(listaCidadeUsuario[index])
        else: melhorDeCadaCidade.append(listaCidadeUsuario[index])
    
    for i in melhorDeCadaCidade:
        print(i)
        
        
 


if __name__ == "__main__":
    main()


