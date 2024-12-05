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


def enviar_fichas(numero_personagem):
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
    clear_console()
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
    print('\nEsse jogo foi produzido por:')
    print('Giovanni Marcarini Silveira')
    print('Desenvolvedor 1 e Diretor Criativo\n')
    print('Arthur Contri')
    print('Desenvolvedor 2 e Modelagem\n')
    input('Pressione enter para voltar ao menu principal')
    menu()
    

#Criando arquivo dos NPCs
dados = baruk.to_dict()
dados_formatados = json.dumps(dados, ensure_ascii=False, indent=4)
nome_arquivo = "baruk.txt"
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(dados_formatados)

dados = bruhilda.to_dict()
dados_formatados = json.dumps(dados, ensure_ascii=False, indent=4)
nome_arquivo = "bruhilda.txt"
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(dados_formatados)

dados = sir_reginald.to_dict()
dados_formatados = json.dumps(dados, ensure_ascii=False, indent=4)
nome_arquivo = "sir_reginald.txt"
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(dados_formatados)
    
dados = grimbeard.to_dict()
dados_formatados = json.dumps(dados, ensure_ascii=False, indent=4)
nome_arquivo = "grimbeard.txt"
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(dados_formatados)

#Iniando o jogo
inicializando()
escolha = menu()

if escolha == 0:
    escolha = selecao_personagem()
    enviar_fichas(escolha)

elif escolha == 1:
    creditos()

elif escolha == 2:
    print('Até mais jogador!')
    exit


from mestre import chat_session
#AI AI QUE LEGAL AI AI QUE FENOMENAL AI AI SENSACIONAL A PIRIQUITA DELA NO MEU PAU
teste = chat_session.send_message('Quais os nomes dos 4 npcs fixos do jogo?')
print(teste.text)