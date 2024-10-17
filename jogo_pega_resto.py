from random import randint
import sys

#jogada e verificação do jogdor 01
def usuario_escolhe_jogada(n, m):
    peca = -1
    while peca > m or peca < 1 or peca > n:
        try:
            peca = int(input(f'\n{jogador01}! Quantas peças você vai tirar? '))
            if peca == 99:
                break
            elif peca > m or peca < 1 or peca > n:
                print(f'\nOops {jogador01}! Jogada inválida! Tente de novo.')
        except:
            print(f'\nOops {jogador01}! Jogada inválida! Tente de novo.')
    if peca == 99:
        fim()
    if peca == 1:
        print(f'{jogador01} tirou uma peça.')
    else:
        print(f'{jogador01} tirou {peca} peças.')
    return peca

#jogada e verificação do jogdor 02
def usuario2_escolhe_jogada(n , m):
    peca = 0
    while peca > m or peca < 1 or peca > n:
        try:
            peca = int(input(f'\n{jogador02}! Quantas peças você vai tirar? '))
            if peca == 99:
                break
            elif peca > m or peca < 1 or peca > n:
                print(f'\nOops {jogador02}! Jogada inválida! Tente de novo.')
        except:
            print(f'\nOops {jogador02}! Jogada inválida! Tente de novo.')
    if peca == 99:
        fim()   
    if peca == 1:
        print(f'{jogador02} tirou uma peça.')
    else:
        print(f'{jogador02} tirou {peca} peças.')
    return peca

#partida 
def partida():
    n = 0
    m = 0
    while n < 1 or m < 1 or n < m:
        try:
            n = int(input('\nEscolha quantas peças iniciarão no tabuleiro? '))
            if n == 99:
                break
            elif n < 1:
                print('\nOops! Jogada inválida! Tente de novo.')
                continue
            m = int(input('Escolha o limite de peças retiradas por jogada? '))
            if m == 99:
                break
            elif m < 1:
                print('\nOops! Jogada inválida! Tente de novo.')
                continue
            elif n < m:
                print('\nOops! Jogada inválida, peças no tabuleiro deve ser maior que limite de peças por jogada! Tente de novo.')
                continue
        except:
            print('\nOops! Jogada inválida! Tente de novo.')
    if n == 99:
        fim()
    if m == 99:
        fim() 
    #sorteio do jogador que irá iniciar a partida
    primeira_jogada = randint(1, 10)
    if primeira_jogada % 2 == 0:
        print(f'\n*** {jogador01} começa! ***')
        peca = usuario_escolhe_jogada(n, m)
        n -= peca
        if n <= 0:
            print(f'\n*** Fim do jogo! {jogador01} ganhou! ***\n')
            return -1
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
        else:
            print(f'Agora restam {n} peças no tabuleiro.')
    else:
        print(f'\n*** {jogador02} começa! ***')
    while n !=0:
        peca = usuario2_escolhe_jogada(n, m)
        n -= peca
        if n <= 0:
            print(f'\n*** Fim do jogo! {jogador02} ganhou! ***\n')
            return -2
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
        else:
            print(f'Agora restam {n} peças no tabuleiro.')
        peca = usuario_escolhe_jogada(n, m)
        n -= peca
        if n <=0:
            print(f'\n*** Fim do jogo! {jogador01} ganhou! ***\n')
            return -1
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
        else:
            print(f'Agora restam {n} peças no tabuleiro.')

def campeonato():
    count = 1
    usuario2 = 0
    usuario = 0
    while count < 4:
        print(f'\n*** Rodada {count} ***')
        res = partida()
        if res == -2:
            usuario2 += 1
        elif res == -1:
            usuario += 1
        count += 1
    print('\n**** Final do campeonato ****')
    print(f'\nPlacar: {jogador01} {usuario} x {usuario2} {jogador02} \n')
    

def inicio():
    print('\nBem-vindo ao Jogo do Pegue o Resto!')
    print('*** O jogador que retirar as últimas peças ganha a partida!')
    print('*** 99 para sair')
    global jogador01
    global jogador02
    jogador01 = input('Digite o nome do Jogador 01: ')
    if jogador01 == '99':
        fim()
    jogador02 = input('Digite o nome do Jogador 02: ')
    if jogador02 == '99':
        fim()
    escolha = 0
    while escolha != 1 and escolha !=2:
        try:
            print('\nEscolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato')
            escolha = int(input())
            if escolha == 99:
                break
            elif escolha != 1 and escolha !=2:
                print('\nOops! Escolha inválida! Tente de novo.')
        except:
            print('\nOops! Escolha inválida! Tente de novo.')
    if escolha == 1:
        print('\nVocê escolheu uma partida isolada!')
        partida()
    elif escolha == 99:
        fim()
    else:
        print('\nVocê escolheu um campeonato!')
        campeonato()

def fim():
    print('\nEspero que tenha gostado do jogo! Até breve!\n')
    sys.exit()
         
inicio()
