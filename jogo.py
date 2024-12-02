from mestre import Mestre

print('Adventure of Rusty Axe Tavern')
print('Bem Vindo jogador')
print('Escolha o se personagem')
print('Borin o Bárbaro')



mestre = Mestre()
mensagem = mestre.mensagem('Começar Aventura')
print(mensagem)
continuar = True

while continuar != False:
    acao = input('')
    mensagem = mestre.mensagem(acao)
    print(mensagem)

def combate(jogador, inimigo):
    contador = 0
    print('Combate')
    while True:
        contador += 1
        print(f'Rodada: {contador}')
        print(f'{inimigo.nome}  nivel {inimigo.nivel}')
        print(inimigo.status)
        print('1. Atacar')
        print('2. Mochila')
        print('3. Conversar')
        print('4. Fugir')
        escolha = input('')
        if escolha == 1:
            acao = input('Descreva seu ataque:')
            #enviar para o mestre [...]
        elif escolha == 2:
            cont = 0
            for item in jogador.inventario:
                cont += 1
                print(f'{cont}. {item.nome}')
            acao = input('Qual item voce deseja usar: ')
            #enviar para o mestre [...]
        elif escolha == 3:
            acao = input(f'({jogador.nome}):')
            #enviar para o mestre [...]
        elif escolha == 4:
            #Narracaod o mestre da tentativa de fuga [...]
        else:
            #enviar para o mestre que o jogador nao fez nada


'''from mestre import Syntheris, Lorealis, Naratheon, Veridex


syntheris = Syntheris()
naratheon = Naratheon()
veridex = Veridex()
lorealis = Lorealis()

resposta_syntheris = syntheris.chat('começar')
acao_jogador = ''

while acao_jogador != 'sair do jogo':
    if resposta_syntheris == '1':
        prompt_lorealis = syntheris.mensagem('O que você deseja que a Lorealis faça:')
        resposta_lorealis = lorealis.mensagem(prompt_lorealis)
        syntheris.mensagem(f'Lorealis: {resposta_lorealis}')

    elif resposta_syntheris == '2':
        prompt_naratheon = syntheris.mensagem('O que você deseja que a Naratheon faça:')
        resposta_naratheon = naratheon.mensagem(prompt_naratheon)
        print(resposta_naratheon)
        acao_jogador = input('')
        syntheris.mensagem(f'Naratheon: {resposta_naratheon}\nJogador: {acao_jogador}')

    elif resposta_syntheris == '3':
        prompt_veridex = syntheris.mensagem('O que você deseja que a Veridex faça:')
        resposta_veridex = veridex.mensagem(prompt_veridex)
        syntheris.mensagem(f'Veridex: {resposta_veridex}')

    else:
        prompt_syntheris = syntheris.mensagem("lembre-se da ordem de atuação, primeiro voce responde somente somente com o número da IA que quer coordenar, depois que receber a mensagem 'O que você deseja que a IA faça:' Voce escreve o prompt com as informações")'''