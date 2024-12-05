from mestre import Mestre
from jogador import borin, elara, pipkin, zaltarian, kael
from NPCs import grimbeard, baruk, bruhilda, sir_reginald
import time
import os
import keyboard

def selecao_personagem():
    "Menu de escolha dos personagens do jogo"

    options = ['Borin o Bárbaro', 'Elara a Barda', 'Pipkin o Ladino', 'Zaltarian a Maga', 'Kael o Paladino']
    current_option = 0
    while True: 
        clear_console()
        print('\n"Em um mundo mágico e cheio de perigos, a taverna Rusty Axe é mais que um ponto de descanso – é o lar de uma guilda lendária. Heróis de todas as partes se reúnem aqui em busca de glória, fortuna e aventuras épicas. O destino do mundo começa a ser escrito... e você está no centro dessa história!"\n')
        print('\nPara começar nesse mundo mágico, primeiro escolha seu personagem\n')

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
            return current_option




def creditos():
    "Exibe os créditos do jogo"
    print('Créditos')

def clear_console():
    """Limpa o console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def inicializando():
    "Inicializa o jogo exibindo o nome"
    

    clear_console()
    print('BEM VINDO AO MUNDO DE')
    time.sleep(1.5)
    print("""
░█████╗░██████╗░██╗░░░██╗███████╗███╗░░██╗████████╗██╗░░░██╗██████╗░███████╗  ░█████╗░███████╗
██╔══██╗██╔══██╗██║░░░██║██╔════╝████╗░██║╚══██╔══╝██║░░░██║██╔══██╗██╔════╝  ██╔══██╗██╔════╝
███████║██║░░██║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░██║░░░██║██████╔╝█████╗░░  ██║░░██║█████╗░░
██╔══██║██║░░██║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░  ██║░░██║██╔══╝░░
██║░░██║██████╔╝░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░╚██████╔╝██║░░██║███████╗  ╚█████╔╝██║░░░░░
╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝  ░╚════╝░╚═╝░░░░░

██████╗░██╗░░░██╗░██████╗████████╗██╗░░░██╗  ░█████╗░██╗░░██╗███████╗
██╔══██╗██║░░░██║██╔════╝╚══██╔══╝╚██╗░██╔╝  ██╔══██╗╚██╗██╔╝██╔════╝
██████╔╝██║░░░██║╚█████╗░░░░██║░░░░╚████╔╝░  ███████║░╚███╔╝░█████╗░░
██╔══██╗██║░░░██║░╚═══██╗░░░██║░░░░░╚██╔╝░░  ██╔══██║░██╔██╗░██╔══╝░░
██║░░██║╚██████╔╝██████╔╝░░░██║░░░░░░██║░░░  ██║░░██║██╔╝╚██╗███████╗
╚═╝░░╚═╝░╚═════╝░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░  ╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝\n""")
    time.sleep(1.5)
    print('> Jogar')
    time.sleep(.3)
    print('  Créditos')
    time.sleep(.3)
    print('  Sair')

def menu():
    """Exibe o main menu interativo."""
    options = ["Jogar", "Créditos", "Sair"]
    current_option = 0



    while True:
        clear_console()
        print('BEM VINDO AO MUNDO DE')
        print("""
░█████╗░██████╗░██╗░░░██╗███████╗███╗░░██╗████████╗██╗░░░██╗██████╗░███████╗  ░█████╗░███████╗
██╔══██╗██╔══██╗██║░░░██║██╔════╝████╗░██║╚══██╔══╝██║░░░██║██╔══██╗██╔════╝  ██╔══██╗██╔════╝
███████║██║░░██║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░██║░░░██║██████╔╝█████╗░░  ██║░░██║█████╗░░
██╔══██║██║░░██║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░  ██║░░██║██╔══╝░░
██║░░██║██████╔╝░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░╚██████╔╝██║░░██║███████╗  ╚█████╔╝██║░░░░░
╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝  ░╚════╝░╚═╝░░░░░

██████╗░██╗░░░██╗░██████╗████████╗██╗░░░██╗  ░█████╗░██╗░░██╗███████╗
██╔══██╗██║░░░██║██╔════╝╚══██╔══╝╚██╗░██╔╝  ██╔══██╗╚██╗██╔╝██╔════╝
██████╔╝██║░░░██║╚█████╗░░░░██║░░░░╚████╔╝░  ███████║░╚███╔╝░█████╗░░
██╔══██╗██║░░░██║░╚═══██╗░░░██║░░░░░╚██╔╝░░  ██╔══██║░██╔██╗░██╔══╝░░
██║░░██║╚██████╔╝██████╔╝░░░██║░░░░░░██║░░░  ██║░░██║██╔╝╚██╗███████╗
╚═╝░░╚═╝░╚═════╝░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░  ╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝\n""")
        
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
            return current_option
        

def enviar_ficha(numero_personagem):
    if numero_personagem == 0:
        personagem = borin
    elif numero_personagem == 1:
        personagem == elara
    elif numero_personagem == 2:
        personagem == pipkin
    elif numero_personagem == 3:
        personagem == zaltarian
    elif numero_personagem == 4:
        personagem == kael
    
    mestre.mensagem(f'Ficha do personagem do jogador:\n{personagem}')


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
            pass
        else:
            #enviar para o mestre que o jogador nao fez nada
            pass

        
def dados(jogador):
    jogador.rolagens

mestre = Mestre()
npcs = f'{grimbeard}'
npcs += f'{baruk}'
npcs += f'{bruhilda}'
npcs += f'{sir_reginald}'
mestre.mensagem(f'Aqui estão os NPCs Fixos do jogo, todos estão presentes dentro da Guilda do Machado Enferrujado\n{npcs}')

#Iniando o jogo
inicializando()
escolha = menu()

if escolha == 0:
    escolha = selecao_personagem()
    enviar_ficha(escolha)

elif escolha == 1:
    creditos()

elif escolha == 2:
    print('Até mais jogador!')
    exit