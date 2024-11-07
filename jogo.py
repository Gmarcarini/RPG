from mestre import Syntheris, Lorealis, Naratheon, Veridex


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
        prompt_syntheris = syntheris.mensagem("lembre-se da ordem de atuação, primeiro voce responde somente somente com o número da IA que quer coordenar, depois que receber a mensagem 'O que você deseja que a IA faça:' Voce escreve o prompt com as informações")