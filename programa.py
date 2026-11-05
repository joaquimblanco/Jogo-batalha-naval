import random
random.seed(1)
from funcoes import define_posicoes, preenche_frota, posicao_valida, faz_jogada, afundados, monta_tabuleiros, posiciona_frota
turno = 1
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
            opcao_orientacao = int(input("[1] Vertical [2] Horizontal "))
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
    if turno % 2 != 0:
        print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
        posicao_nova_jogador = False
        while not posicao_nova_jogador:
            linha_jogador = int(input("Jogador, qual linha deseja atacar? "))
            while linha_jogador not in range(10):
                print("Linha inválida!")
                linha_jogador = int(input("Jogador, qual linha deseja atacar? "))
            coluna_jogador = int(input("Jogador, qual coluna deseja atacar? "))
            while coluna_jogador not in range(10):
                print("Coluna inválida!")
                coluna_jogador = int(input("Jogador, qual coluna deseja atacar? "))
            if tabuleiro_oponente[linha_jogador][coluna_jogador] in ["X", "-"]:
                print(f"A posição linha {linha_jogador} e coluna {coluna_jogador} já foi informada anteriormente!")
            else:
                posicao_nova_jogador = True
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_jogador, coluna_jogador)
        navios_afundados_oponente = afundados(frota_oponente, tabuleiro_oponente)
        turno += 1
        if navios_afundados_oponente == 10:
            print("Parabéns! Você derrubou todos os navios do seu oponente!")
            jogando = False
            break
        elif turno % 2 == 0:
            posicao_nova_oponente = False
            while not posicao_nova_oponente:
                linha_oponente = random.randint(0, 9)
                coluna_oponente = random.randint(0, 9)
                if tabuleiro_jogador[linha_oponente][coluna_oponente] not in ["X", "-"]:
                    posicao_nova_oponente = True
            print(f"Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}")
            tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)
            navios_afundados_jogador = afundados(frota, tabuleiro_jogador)
            turno += 1
            if navios_afundados_jogador == 10:
               print("Xi! O oponente derrubou toda a sua frota =(")
               jogando = False