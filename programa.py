def define_posicoes(linha, coluna, orientacao, tamanho):
    indice = 0
    grid = []
    if orientacao == 'horizontal':
        while indice < tamanho:
            grid.append([linha, coluna + indice])
            indice += 1
    elif orientacao == 'vertical':
        while indice < tamanho:
            grid.append([linha + indice, coluna])
            indice += 1
    return grid

def preenche_frota(dicionario_frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in dicionario_frota:
        dicionario_frota[nome_navio] = []
    dicionario_frota[nome_navio].append(posicoes)
    return dicionario_frota

def posicao_valida(informacoes_navios,linha,coluna,orientacao,tamanho):
    novas_posicoes = define_posicoes(linha,coluna,orientacao,tamanho)
    for pos in novas_posicoes:
        l,c = pos[0],pos[1]
        if l < 0 or l > 9 or c < 0 or c > 9:
            return False
        for lista_de_navios in informacoes_navios.values():
            for navio in lista_de_navios:
                if pos in navio:
                    return False
    return True


frota = {}
configuracao_navios = [("porta-aviões",4,1),("navio-tanque",3,2),("contratorpedeiro",2,3),("submarino",1,4)]
for nome_navio,tamanho,quantidade in configuracao_navios:
    i = 0
    print(f"Insira as informacoes do navio {nome_navio} que possui tamanho {tamanho}")
    while i < quantidade:
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        if tamanho == 1:
            orientacao = 'vertical'
        else:
            opcao_orientacao = int(input("[1] Vertical [2] Horizontal >"))
            if opcao_orientacao == 1:
                orientacao = 'vertical'
            elif opcao_orientacao == 2:
                orientacao = 'horizontal'
        if posicao_valida(frota,linha,coluna,orientacao,tamanho) == True:
            if nome_navio not in frota:
                frota[nome_navio] = []
            frota[nome_navio].append(preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho).get(nome_navio))
            i += 1
        else:
            print("Esta posição não está válida!")
print(frota)