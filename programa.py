from funcoes import define_posicoes, preenche_frota, posicao_valida, faz_jogada, afundados, monta_tabuleiros, posiciona_frota
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
jogando = True
lista_linha = []
lista_coluna = []
frota_oponente = {'porta-aviões': [[[9, 1], [9, 2], [9, 3], [9, 4]]],
    'navio-tanque': [[[6, 0], [6, 1], [6, 2]],[[4, 3], [5, 3], [6, 3]]],
    'contratorpedeiro': [[[1, 6], [1, 7]],[[0, 5], [1, 5]],[[3, 6], [3, 7]]],
    'submarino': [[[2, 7]],[[0, 6]],[[9, 7]],[[7, 6]]]}
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    posicao_nova = False
    while not posicao_nova:
        linha = int(input("Jogador, qual linha deseja atacar? "))
        while linha not in range(10):
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar? "))
        coluna = int(input("Jogador, qual coluna deseja atacar? "))
        while coluna not in range(10):
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))
        if tabuleiro_oponente[linha][coluna] in ["X", "-"]:
            print(f"A posição linha {linha} e coluna {coluna} ""já foi informada anteriormente!")
        else:
            posicao_nova = True
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
    navios_afundados = afundados(frota_oponente, tabuleiro_oponente)
    if navios_afundados == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False