import random
from habilidades import Habilidades

class AnaoMontanha:
    def __init__(self, classe):
        d4 = [random.randint(1,4) for i in len(range(5))]
        d6 = [random.randint(1,6) for i in len(range(1))]
        self.altura = 1.22 + sum(d4)
        self.peso = 65 + (sum(d4) * sum(d6) / 5)
        self.idiomas = ['comum', 'anao']
        self.habilidades = classe.habilidades
        self.habilidades.constituicao += 2
        self.habilidades.forca += 2
        self.proef = ['armaduras leves', 'armaduras medias', 'machados de batalha', 'machadinhas', 'martelos leves', 'martelos de guerra']
        self.deslocamento = 7.5
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz plena, e no escuro como se fosse na penumbra.'
            }

class AnaoColina:
    def __init__(self, classe):
        d4 = [random.randint(1,4) for i in len(range(5))]
        d6 = [random.randint(1,6) for i in len(range(1))]
        self.altura = 1.12 + sum(d4)
        self.peso = 57 + (sum(d4) * sum(d6) / 5)
        self.idiomas = ['comum', 'anao']
        self.habilidades = classe.habilidades
        self.habilidades.constituicao += 2
        self.habilidades.sabedoria += 1
        self.vida += 1
        self.proef = ['machados de batalha', 'machadinhas', 'martelos leves', 'martelos de guerra']
        self.deslocamento = 7.5
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz plena, e no escuro como se fosse na penumbra.'
            }

class AltoElfo:
    def __init__(self, classe):
        d10 = [random.randint(1,10) for i in len(range(5))]
        d4 = random.randint(1,4)
        self.altura = 1.37 + sum(10)
        self.peso = 45 + (sum(10) * d4 / 5)
        self.idiomas = ['comum', 'elfico']
        self.habilidades = classe.habilidades
        self.habilidades.destreza += 2
        self.habilidades.inteligencia += 1
        self.deslocamento = 9
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz plena, e no escuro como se fosse na penumbra.',
            'Sentidos Aguçados': 'Você tem proficiência na perícia Percepção.',
            'Transe': 'Elfos podem entar em transe (meditação) para descansar durante 4 horas, equivalente a um descanso de 8 horas'
            }
        self.proef = ['espadas longas', 'espadas curtas', 'arcos longos', 'arcos curtos']
        self.truques = []



class ElfoFloresta:
    def __init__(self, classe):
        d10 = [random.randint(1,10) for i in len(range(5))]
        d4 = random.randint(1,4)
        self.altura = 1.37 + sum(10)
        self.peso = 50 + (sum(10) * d4 / 5)
        self.idiomas = ['comum', 'elfico']
        self.habilidades = classe.habilidades
        self.habilidades.destreza += 2
        self.habilidades.sabedoria += 1
        self.deslocamento = 10.5
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz plena, e no escuro como se fosse na penumbra.',
            'Sentidos Aguçados': 'Você tem proficiência na perícia Percepção.',
            'Transe': 'Elfos podem entar em transe (meditação) para descansar durante 4 horas, equivalente a um descanso de 8 horas',
            'Mascara da natureza': 'Voce pode tentar se esconder mesmo quando esta apenas levemente obscurecido'
            }
        self.proef = ['espadas longas', 'espadas curtas', 'arcos longos', 'arcos curtos']

class ElfoNegro:
    def __init__(self, classe):
        d6 = [random.randint(1,6) for i in len(range(5))]
        d_6 = random.randint(1,6)
        self.altura = 1.32 + sum(d6)
        self.peso = 48 + (sum(d6) * sum(d_6) / 5)
        self.idiomas = ['comum', 'elfico']
        self.habilidades = classe.habilidades
        self.habilidades.destreza += 2
        self.habilidades.carisma += 1
        self.deslocamento = 10.5
        self.caract_raca = {
            'Visão no escuro superior': 'enxerga na penumbra a até 36 metros como se fosse luz plena, e no escuro como se fosse na penumbra.',
            'Sentidos Aguçados': 'Você tem proficiência na perícia Percepção.',
            'Transe': 'Elfos podem entar em transe (meditação) para descansar durante 4 horas, equivalente a um descanso de 8 horas',
            'Mascara da natureza': 'Voce pode tentar se esconder mesmo quando esta apenas levemente obscurecido',
            'Sensibilidade a luz solar': 'Voce possui desvantagem em testes de percepcao se o alvo esta sob luz solar direta'
            }
        self.proef = ['rapieiras', 'espadas curtas', 'bestas de mao']

class HalflingPesLeves:
    def __init__(self, classe):
        d6 = [random.randint(1,6) for i in len(range(5))]
        self.altura = 0.78 + sum(d6)
        self.peso = 18 + (sum(d6) * 1 / 5)
        self.idiomas = ['comum', 'halfling']
        self.habilidades = classe.habilidades
        self.habilidades.destreza += 2
        self.habilidades.carisma += 1
        self.deslocamento = 7.5  
        self.caract_raca = {
            'Sortudo': 'Se voce tirar 1 natural, voce pode rolar de novo e utilizar o novo resultado da rolagem',
            'Agilidade Halfling': 'Voce pode se mover atraves do espaço de qualquer criatura que for de um tamanho maior que o seu',
            'Furtividade Natural': 'Voce pode tentar se esconder mesmo quando possuir apenas uma cobertura de uma criatura que for no minimo um tamanho maior que o seu',
            }

class HalflingRobusto:
    def __init__(self, classe):
        d6 = [random.randint(1,6) for i in len(range(5))]
        self.altura = 0.78 + sum(d6)
        self.peso = 18 + (sum(d6) * 1 / 5)
        self.idiomas = ['comum', 'halfling']
        self.habilidades = classe.habilidades
        self.habilidades.destreza += 2
        self.habilidades.constituicao += 1
        self.deslocamento = 7.5  
        self.caract_raca = {
            'Sortudo': 'Se voce tirar 1 natural, voce pode rolar de novo e utilizar o novo resultado da rolagem',
            'Bravura': 'Voce tem vantagem em testes de resistencia contra ficar amedrontado',
            'Agilidade Halfling': 'Voce pode se mover atraves do espaço de qualquer criatura que for de um tamanho maior que o seu',
            }


class Humano:
    def __init__(self, classe):
        d10 = [random.randint(1,10) for i in len(range(5))]
        d4 = [random.randint(1,4) for i in len(range(1))]
        self.altura = 1.42 + sum(10)
        self.peso = 55 + (sum(10) * sum(d4) / 5)
        self.idiomas = ['comum']
        self.habilidades = classe.habilidades
        self.habilidades.forca += 1
        self.habilidades.destreza += 1
        self.habilidades.constituicao += 1
        self.habilidades.inteligencia += 1
        self.habilidades.sabedoria += 1
        self.habilidades.carisma += 1
        self.deslocamento = 9  


class Draconato:
    def __init__(self, classe):
        d8 = [random.randint(1,8) for i in len(range(5))]
        d6 = [random.randint(1,6) for i in len(range(1))]
        self.altura = 1.67 + sum(d8)
        self.peso = 87 + (sum(d8) * sum(d6) / 5)
        self.idiomas = ['comum', 'draconico']
        self.habilidades = classe.habilidades
        self.habilidades.forca += 2
        self.habilidades.carisma += 1
        self.deslocamento = 9
        d10 = random.randint(1,10)
        ancestrais = {'Azul': 'Elétrico, Linha de 1,5 a 9m, teste de destreza',
                      'Branco': 'Frio, cone de 4,5m, teste de constituicao',
                      'Bronze': 'Eletrico, Linha de 1,5 a 9m, teste de destreza',
                      'Cobre': 'Acido, Linha de 1,5 a 9m, teste de destreza',
                      'Latao': 'Fogo, Linha de 1,5 a 9m, teste de destreza',
                      'Negro': 'Acido, Linha de 1,5 a 9m, teste de destreza',
                      'Ouro': 'Fogo, Cone de 4,5m , teste de destreza',
                      'Prata': 'Frio, Cone de 4,5m, teste de constituicao',
                      'Verde': 'Veneno, Cone de 4,5m, teste de constituicao',
                      'Vermelho': 'Fogo, Cone de 4,5m, teste de destreza'
                      }
        for i, (chave, valor) in enumerate(ancestrais.items(), start=1):
            if i == d10:
                self.ancestral = {chave: valor}
                break

class GnomoFloresta:
    def __init__(self, classe):
        d4 = [random.randint(1,4) for i in len(range(5))]
        self.altura =0.88 + sum(d4)
        self.peso = 18 + (sum(d4) * 1 / 5)
        self.idiomas = ['comum', 'gnomico']
        self.habilidades = classe.habilidades
        self.habilidades.inteligencia += 2
        self.habilidades.destreza += 1
        self.deslocamento = 7.5  
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz plena, e no escuro como se fosse na penumbra.',
            'Falar com bestas pequenas': 'atraves de sons e gestos voce consegue comunicar ideias simples para bestas pequenas ou menores'
            }
        self.truques = ['ilusao pequena']

class GnomoRochas:
    def __init__(self, classe):
        d4 = [random.randint(1,4) for i in len(range(5))]
        self.altura =0.88 + sum(d4)
        self.peso = 18 + (sum(d4) * 1 / 5)
        self.idiomas = ['comum', 'gnomico']
        self.habilidades = classe.habilidades
        self.habilidades.inteligencia += 2
        self.habilidades.constituicao += 1
        self.deslocamento = 7.5  
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz plena, e no escuro como se fosse na penumbra.',
            'Conhecimento artificie': 'Se realizar um teste de inteligencia historia, referente a itens magicos, objetos alquimicos ou mecanismos tecnologicos voce adiciona o dobro de do seu bonus de proeficiencia ',
            'Engenhoqueiro': 'Voce pode gastar 1 hora e 10 po para criar um mecanismo miúdo(CA 5, 1pv) e pode ter até 3 desses mecanismos ativos ao memso tempo, ele dura 24 horas'
            }
        self.truques = ['ilusao pequena']
        self.proef = ['ferramentas de artesao']

class MeioElfo:
    def __init__(self, classe):
        d8 = [random.randint(1,8) for i in len(range(5))]
        d4 = [random.randint(1,4) for i in len(range(1))]
        self.altura = 1.45 + sum(d8)
        self.peso = 55 + (sum(d8) * sum(d4) / 5)
        self.idiomas = ['comum', 'elfico']
        self.habilidades = classe.habilidades
        self.habilidades.carisma += 2
        self.habilidades.destreza += 1
        self.habilidades.sabedoria += 1
        self.deslocamento = 9  
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz plena, e no escuro como se fosse na penumbra.',
            }

class MeioOrc:
    def __init__(self, classe):
        d8 = [random.randint(1,8) for i in len(range(5))]
        d6 = [random.randint(1,6) for i in len(range(1))]
        self.altura = 1.47 + sum(d8)
        self.peso = 70 + (sum(d8) * sum(d6) / 5)
        self.idiomas = ['comum', 'orc']
        self.habilidades = classe.habilidades
        self.habilidades.forca += 2
        self.habilidades.constituicao += 1
        self.deslocamento = 9  
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz plena, e no escuro como se fosse na penumbra.',
            'Ataques selvagens': 'Quando atingir um ataque critico com uma arma corpo a corpo, voce rola mais um dado de dano da arma para dar dano extra'
            }
        self.proef = ['intimidacao']

class Tieflings:
    def __init__(self, classe):
        d8 = [random.randint(1,8) for i in len(range(5))]
        d4 = [random.randint(1,4) for i in len(range(1))]
        self.altura = 1.45 + sum(d8)
        self.peso = 55 + (sum(d8) * sum(d4) / 5)
        self.idiomas = ['comum', 'infernal']
        self.habilidades = classe.habilidades
        self.habilidades.inteligencia += 1
        self.habilidades.carisma += 2
        self.deslocamento = 9  
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz plena, e no escuro como se fosse na penumbra.',
            }
        self.truques = ['traumaturgia']

anao_montanha = AnaoMontanha()









































'''info = f'força: {habilidades_anao.forca}\n'
info += f'destreza: {habilidades_anao.destreza}\n'
info += f'constituição: {habilidades_anao.constituicao}\n'
info += f'inteligencia: {habilidades_anao.inteligencia}\n'
info += f'sabedoria: {habilidades_anao.sabedoria}\n'
info += f'carisma: {habilidades_anao.carisma}\n'

info += f'modificador força: {habilidades_anao.modificadores['forca']}\n'
info += f'modificador destreza: {habilidades_anao.modificadores['destreza']}\n'
info += f'modificador constituição: {habilidades_anao.modificadores['constituicao']}\n'
info += f'modificador inteligencia: {habilidades_anao.modificadores['inteligencia']}\n'
info += f'modificador sabedoria: {habilidades_anao.modificadores['sabedoria']}\n'
info += f'modificador carisma: {habilidades_anao.modificadores['carisma']}\n'

print(info)'''
        