from jogador import borin, elara, pipkin, zaltarian, kael
from NPCs import grimbeard, baruk, bruhilda, sir_reginald
import time
import os
import keyboard
import json

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


def enviar_ficha(numero_personagem):
    if numero_personagem == 0:
        personagem = borin
    elif numero_personagem == 1:
        personagem = elara
    elif numero_personagem == 2:
        personagem = pipkin
    elif numero_personagem == 3:
        personagem = zaltarian
    elif numero_personagem == 4:
        personagem = kael

    dados = personagem.to_dict()
    dados_formatados = json.dumps(dados, ensure_ascii=False, indent=4)
    nome_arquivo = "personagem.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(dados_formatados)


def creditos():
    print('Esse jogo foi produzido por:')
    print('Giovanni Marcarini Silveira')
    print('Desenvolvedor Principal e Diretor Criativo')
    print('Arthur Contri')
    print('Modelador UML')
    input('Pressione enter para voltar ao menu principal')
    menu()
    
'''npcs = f'{grimbeard}'
npcs += f'{baruk}'
npcs += f'{bruhilda}'
npcs += f'{sir_reginald}'
mestre.mensagem(f'Aqui estão os NPCs Fixos do jogo, todos estão presentes dentro da Guilda do Machado Enferrujado\n{npcs}')'''
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

from mestre import chat_session
teste = chat_session.send_message('Após ler o arquivo me responde somente com a classe do personagem do arquivo')
print(teste.text)