class Personagens:
    def __init__(self, nome):
        self.nome = nome
        self.nivel = 1
        self.atributos = {
            'força': 0,
            'destreza': 0,
            'constituicao': 0,
            'inteligencia': 0,
            'sabedoria': 0,
            'carisma': 0
        }
        self.vida = 0
        self.armadura = 0

class Barbaro:
    def __init__(self):
        self.nome = 'Borin Pedra-Rachada'
        self.classe = 'Bárbaro'
        self.nivel = 1
        self.raca = 'Anão da Montanha'
        self.antecedente = 'Forasteiro'
        self.tendencia = 'Caótico Bom'
        self.habilidades = {
            'forca': 17,
            'destreza': 10,
            'constituicao': 16,
            'inteligencia': 8,
            'sabedoria': 12,
            'carisma': 13
        }
        self.bonus_proef = 2
        self.armadura = 16
        self.iniciativa = 2
        self.deslocamento = 7.5
        self.vida = 15
        self.resistencias = {
            'força': 5,
            'contituicao': 5
        }
        self.percepcao = 11
        self.pericias = {
            'atletismo': 5,
            'sobrevivencia': 3,
            'percepcao': 3,
            'adestrar_animais': 3
        }
        self.idiomas = ['comum, anão, gigante']
        self.proeficiencias = ['ferramentas de ferreiro', 'instrumentos músicais de percussão']
        self.equipamentos = {
            'machado de batalha': 1,
            'machadinhas de arremesso': 2,
            'pacote de explorador': 1,
            'ferramentas de ferreiro': 1,
            'tambor': 1
        }
        self.altura = 1.39
        self.peso = 72
        self.aliados = {
            'cla Pedra Rachada': 'exilado',
            'Liga dos Exploradores da Montanha Rochosa': 'iniciante'
        }
        self.caracteristicas = {
            'descricao': 'Baixo e robusto, mesmo para os padrões de anões.Olhos castanhos, pele cor de bronze barba e bigode pretos com mechas brancas, bem cuidados e trançados com fios de cobre. Uma cicatriz profunda cruza seu olho esquerdo, lembrança de um encontro com um lobo atroz. Tatuagens representando runas anãs adornam seus braços e ombros',
            'tracos': 'Impulsivo, corajoso até a beira da imprudência, leal aos seus amigos, desconfiado de estranhos (especialmente elfos), tem um fraco por crianças e animais indefesos',
            'ideais': 'Liberdade. "Ninguém me diz o que fazer. A montanha é meu único mestre',
            'defeitos': 'Eu tenho um pavio curto e me irrito com facilidade, especialmente quando alguém questiona minha coragem ou zomba da minha altura',
            'histórico': 'Borin nasceu no clã Pedra-Rachada, conhecido por sua habilidade na mineração e metalurgia. Ele sempre foi menor que os outros anões, o que o levou a provar seu valor com atos de bravura e ousadia. Quando um gigante do gelo atacou seu vilarejo, matando seu irmão e roubando o totem sagrado do clã (uma antiga machadinha de guerra feita com ossos de dragão), Borin jurou vingança. Ele deixou sua casa nas montanhas e se juntou à Liga dos Exploradores da Montanha Rochosa para aprimorar suas habilidades de combate e rastrear o gigante'
        }
        self.tesouro = {
            'po': 50,
            'pepita de ouro': 1,
            'cordao de dente de lobo atroz': 1
        }

