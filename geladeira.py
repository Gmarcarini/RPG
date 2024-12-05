#A partir daqui começa o Jogo

def combate(jogador, inimigo):
    contexto = mestre.mensagem('O jogador entra em combate com o inimigo, escreva um pequeno, breve e introdutorio texto sobre esse embate')
    contador = 0

    options = ['Atacar', 'Conversar', 'Mochila', 'Fugir']
    current_option = 0
    while True: 
        contador += 1
        clear_console()
        print(contexto)
        print('Combate')
        print(f'Rodada: {contador}')
        print(f'{inimigo.nome}  nivel {inimigo.nivel}')

        # Mostra as opções e destaca a atual
        for i, option in enumerate(options):
            if i == current_option:
                print(f"> {option}")  # Indica a opção selecionada
                      
            else:
                print(f"  {option}")

        # Espera por eventos do teclado
        event = keyboard.read_event(suppress=True)

        if event.name == 'down' and event.event_type == 'down':
            current_option = (current_option + 1) % len(options)  # Vai para a próxima opção
        elif event.name == 'up' and event.event_type == 'down':
            current_option = (current_option - 1) % len(options)  # Vai para a opção anterior
        elif event.name == 'enter' and event.event_type == 'down':
            if current_option == 0:
                acao = input('Descreva seu ataque:')
                return mestre.mensagem(f'O jogador ataca\nDescrição:{acao}')
            elif current_option == 1:
                acao = input(f'({jogador.nome}):')
                return mestre.mensagem(f'O jogador começa a conversar:\n{acao}')
            elif current_option == 2:
                "\n".join(
                f"  - {item}: {quantidade}" for item, quantidade in jogador.inventario.items()
                )
                acao = input('Qual item voce deseja usar: ')
                return mestre.mensagem(f'O jogador abriu seu inventario e escolheu o item {acao}')
            elif current_option == 3:
                return mestre.mensagem(f'O jogador tenta realizar uma fuga')
            else:
                return mestre.mensagem(f'O jogador nao fez nada')



def dados(jogador):
    jogador.rolagens