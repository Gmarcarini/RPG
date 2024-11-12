import random

class Personagem:
    def __init__(self, nome, classe, nivel, raca, antecedente, tendencia, habilidades, bonus_proef, armadura, iniciativa,
                 deslocamento, vida, resistencias, percepcao, pericias, idiomas, proeficiencias, equipamentos, altura, 
                 peso, aliados, caracteristicas, tesouro):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.raca = raca
        self.antecedente = antecedente
        self.tendencia = tendencia
        self.habilidades = habilidades
        self.bonus_proef = bonus_proef
        self.armadura = armadura
        self.iniciativa = iniciativa
        self.deslocamento = deslocamento
        self.vida = vida
        self.resistencias = resistencias
        self.percepcao = percepcao
        self.pericias = pericias
        self.idiomas = idiomas
        self.proeficiencias = proeficiencias
        self.equipamentos = equipamentos
        self.altura = altura
        self.peso = peso
        self.aliados = aliados
        self.caracteristicas = caracteristicas
        self.tesouro = tesouro
    
    def Rolagens(self):
        pass

class Barbaro(Personagem):
    def __init__(self):
        super().__init__(
            nome='Borin Pedra-Rachada',
            classe='Bárbaro',
            nivel=1,
            raca='Anão da Montanha',
            antecedente='Forasteiro',
            tendencia='Caótico Bom',
            habilidades={
                'forca': 15,
                'destreza': 10,
                'constituicao': 14,
                'inteligencia': 8,
                'sabedoria': 12,
                'carisma': 13
            },
            bonus_proef=2,
            armadura=16,
            iniciativa=2,
            deslocamento=7.5,
            vida=15,
            resistencias={
                'força': 5,
                'constituicao': 5
            },
            percepcao=11,
            pericias={
                'atletismo': 5,
                'sobrevivencia': 3,
                'percepcao': 3,
                'adestrar_animais': 3
            },
            idiomas=['comum', 'anão', 'gigante'],
            proeficiencias=['ferramentas de ferreiro', 'instrumentos musicais de percussão'],
            equipamentos={
                'machado de batalha': 1,
                'machadinhas de arremesso': 2,
                'pacote de explorador': 1,
                'ferramentas de ferreiro': 1,
                'tambor': 1
            },
            altura=1.39,
            peso=72,
            aliados={
                'cla Pedra Rachada': 'exilado',
                'Liga dos Exploradores da Montanha Rochosa': 'iniciante'
            },
            caracteristicas={
                'descricao': 'Baixo e robusto, mesmo para os padrões de anões.Olhos castanhos, pele cor de bronze barba e bigode pretos com mechas brancas, bem cuidados e trançados com fios de cobre. Uma cicatriz profunda cruza seu olho esquerdo, lembrança de um encontro com um lobo atroz. Tatuagens representando runas anãs adornam seus braços e ombros',
                'tracos': 'Impulsivo, corajoso até a beira da imprudência, leal aos seus amigos, desconfiado de estranhos (especialmente elfos), tem um fraco por crianças e animais indefesos',
                'ideais': 'Liberdade. "Ninguém me diz o que fazer. A montanha é meu único mestre',
                'defeitos': 'Eu tenho um pavio curto e me irrito com facilidade, especialmente quando alguém questiona minha coragem ou zomba da minha altura',
                'histórico': 'Borin nasceu no clã Pedra-Rachada, conhecido por sua habilidade na mineração e metalurgia. Ele sempre foi menor que os outros anões, o que o levou a provar seu valor com atos de bravura e ousadia. Quando um gigante do gelo atacou seu vilarejo, matando seu irmão e roubando o totem sagrado do clã (uma antiga machadinha de guerra feita com ossos de dragão), Borin jurou vingança. Ele deixou sua casa nas montanhas e se juntou à Liga dos Exploradores da Montanha Rochosa para aprimorar suas habilidades de combate e rastrear o gigante'
            },
            tesouro={
                'po': 50,
                'pepita de ouro': 1,
                'cordao de dente de lobo atroz': 1
            }
        )
    
    def Rolagens(self):
        d20 = random.randint(1, 20)
        resultados = f'Teste de Força: {d20} +2'
        resultados += f'Teste de Destreza: {d20} +0'
        resultados += f'Teste de Constituição: {d20} +2'
        resultados += f'Teste de Inteligencia: {d20} -1'
        resultados += f'Teste de Sabedoria: {d20} +1'
        resultados += f'Teste de Carisma: {d20} +1'
    
    def info(self):
        info = (f"""Ficha do personagem
        Nome: {self.nome}
        Classe: {self.classe}
        Raça: {self.raca}
        Antecedente: {self.antecedente}
        Tendência: {self.tendencia}
        Habilidades: 
        Força: {self.habilidades['força']}
        Destreza: {self.habilidades['destreza']}
        Constituição: {self.habilidades['constituicao']}
        Inteligência: {self.habilidades['inteligencia']}
        Sabedoria: {self.habilidades['sabedoria']}
        Carisma: {self.habilidades['carisma']}
        Bonus de Proeficiência: +{self.bonus_proef}
        Armadura: {self.armadura}
        Vida: {self.vida}
        Iniciativa: +{self.iniciativa}
        Deslocamento: {self.deslocamento}m
        Testes de Resistência: {self.resistencias}
        Sabedoria (Percepção) Passiva: {self.percepcao}
        Perícias: {self.pericias}
        Idiomas: {self.idiomas}
        Proeficiencias: {self.proeficiencias}
        Equipamentos: {self.equipamentos}
        Altura: {self.altura}m
        Aliados: {self.aliados}
        Características: {self.caracteristicas}
        Tesouro: {self.tesouro}""")
        return info