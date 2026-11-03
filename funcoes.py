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
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro
def posiciona_frota(dicionario_navio):
    tabuleiro = []
    for indice in range(10):
        linha = [0] * 10
        tabuleiro.append(linha)
    for lista_posicoes in dicionario_navio.values():
        for posicao_x_y in lista_posicoes:
            for x,y in posicao_x_y:
                tabuleiro[x][y] = 1
    return tabuleiro
def afundados(frota,tabuleiro):
    navios_afundados = 0
    for tipo_navio,lista_navios in frota.items():
        for navio in lista_navios:
            partes_atingidas = 0
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] == 'X':
                    partes_atingidas += 1
            if partes_atingidas == len(navio):
                navios_afundados += 1
    return navios_afundados
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
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto