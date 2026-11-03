from funcoes import define_posicoes, preenche_frota, posicao_valida, faz_jogada, afundados, monta_tabuleiros
frota = {}
configuracao_navios = [("porta-aviões",4,1),("navio-tanque",3,2),("contratorpedeiro",2,3),("submarino",1,4)]
for nome_navio,tamanho,quantidade in configuracao_navios:
    i = 0
    while i < quantidade:
        print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}")
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
            frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
            i += 1
        else:
            print("Esta posição não está válida!")
print(frota)