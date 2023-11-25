import pickle

def main():
    with open("backupMil.bin", "rb") as file:
        usuarios = pickle.load(file);
        conexoes = pickle.load(file);
        historico = pickle.load(file);

    print(gerarConexoes(historico, conexoes));


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

if __name__ == "__main__":
    main()