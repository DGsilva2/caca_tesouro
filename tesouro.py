import numpy as np

#criando mapa 5x5
mapa=np.random.randint(1, 10, size=(5,5))

#esconder o tesouro no nosso mapa
while True:
    tesouro_linha, tesouro_coluna = np.random.randint(0, 5, size=2)
    if (tesouro_linha, tesouro_coluna)!=(0,0):
        break
    
#definir posição inicial e pontuação
posicao_jogador=(0,0)
pontuacao = 0

#loop principal do jogo
while True:
    mapa_com_jogador = np.copy(mapa)
    mapa_com_jogador[posicao_jogador]=0
    print(mapa_com_jogador)
    
    
    # Escolhemos a movimentação atraves do input
    direcao = input('Digite a direcao que deseja se mover (cima, baixo, esquerda, direita): ')
    if direcao == 'cima' or direcao == 'c':
        nova_posicao = (posicao_jogador[0] - 1, posicao_jogador[1])
    elif direcao == 'baixo' or direcao == 'b':
        nova_posicao = (posicao_jogador[0] + 1, posicao_jogador[1])
    elif direcao == 'esquerda' or direcao == 'e':
        nova_posicao = (posicao_jogador[0], posicao_jogador[1] - 1)
    elif direcao == 'direita' or direcao == 'd':
        nova_posicao = (posicao_jogador[0], posicao_jogador[1] + 1)
        
    if nova_posicao[0] < 0 or nova_posicao[0]>=mapa.shape[0] or nova_posicao[1] < 0 or nova_posicao[1]>= mapa.shape[1]:
        print('Posição inválida')
        continue
    
    #atualzar a posição real do jogador
    posicao_jogador = nova_posicao
    pontuacao += 1
    
    #verificar se o jogador encontrou o tesouro
    if posicao_jogador == (tesouro_linha, tesouro_coluna): 
        mapa_com_jogador = np.copy(mapa)
        mapa_com_jogador[posicao_jogador]=0
        print(mapa_com_jogador)
        break
    
print('\n\n==== Parabéns, você encontrou o tesouro ===')
print(f'PONTUAÇÃO FINAL: {pontuacao}')
print(f'O tesouro estav em {(tesouro_linha, tesouro_coluna)}')