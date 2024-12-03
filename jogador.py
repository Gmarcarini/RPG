import random
from racas import anao_montanha, gnomo_floresta, tieflings, meio_elfo, draconato

class Personagem:
    def __init__(self, nome, raca, antecedente, tendencia,
                 aliados, caracteristicas, tesouro, inventario):
        self.nome = nome
        self.classe = raca.classe
        self.nivel = self.classe.nivel
        self.raca = raca
        self.antecedente = antecedente
        self.tendencia = tendencia
        self.habilidades = self.classe.habilidades
        self.bonus_proef = self.classe.bonus_proef
        self.armadura = self.classe.CA
        self.deslocamento = raca.deslocamento
        self.vida = self.classe.vida
        self.percepcao_passiva = self.classe.percepcao_passiva
        self.pericias = self.classe.pericias
        self.idiomas = raca.idiomas
        self.proeficiencias = self.classe.proef
        self.equipamentos = self.classe.inventario
        self.altura = raca.altura
        self.peso = raca.peso
        self.aliados = aliados
        self.caracteristicas = caracteristicas
        self.tesouro = tesouro
        self.inventario = {**self.classe.inventario, **inventario}

    def Rolagens(self):
        dados = f'Força: {random.randint(1,20) + self.habilidades.modificadores['forca']}'
        dados += f'Destreza: {random.randint(1,20) + self.habilidades.modificadores['destreza']}'
        dados += f'Constituicao: {random.randint(1,20) + self.habilidades.modificadores['constituicao']}'
        dados += f'Inteligencia: {random.randint(1,20) + self.habilidades.modificadores['inteligencia']}'
        dados += f'Sabedoria: {random.randint(1,20) + self.habilidades.modificadores['sabedoria']}'
        dados += f'Carisma: {random.randint(1,20) + self.habilidades.modificadores['carisma']}'
        return dados

borin = Personagem('Borin Pedra-Rachada', anao_montanha, 'forasteiro', 'Caótico bom', {'Clã Pedra-Rachada': 'exilado', 'Liga dos Exploradores da Montanha Rochosa': 'iniciante'}, ' Impulsivo, corajoso até a beira da imprudência, leal aos seus amigos, desconfiado de estranhos (especialmente elfos), tem um fraco por crianças e animais indefesos.  Liberdade. "Ninguém me diz o que fazer. A montanha é meu único mestre." Eu devo vingança ao gigante do gelo que matou meu irmão e roubou o totem do meu clã. Eu tenho um pavio curto e me irrito com facilidade, especialmente quando alguém questiona minha coragem ou zomba da minha altura.', 50, {'pequena pepita de ouro': 1, 'Cordao de dente de lobo': 1})

#Ficha barbaro
#print('Ficha Borin Pedra-Rachada')
info = f'Nome: {borin.nome}\n'
info +=  f'Classe Nível: {borin.classe.nome} {borin.classe.nivel}\n'
info +=  f'Antecendente: {borin.antecedente}\n'
info +=  f'Raça: {borin.raca.nome}\n'
info +=  f'Tendencia: {borin.tendencia}\n'
info +=  f'Ponrtos de Experiencia: {borin.classe.experiencia}\n'
info +=  f'\nHabilidades:\n'
info +=  f'Força: {borin.habilidades.forca}\n'
info +=  f'Modificador: {borin.habilidades.modificadores['forca']}\n'
info +=  f'Destreza: {borin.habilidades.destreza}\n'
info +=  f'Modificador: {borin.habilidades.modificadores['destreza']}\n'
info +=  f'Constituição: {borin.habilidades.constituicao}\n'
info +=  f'Modificador: {borin.habilidades.modificadores['constituicao']}\n'
info +=  f'Inteligencia: {borin.habilidades.inteligencia}\n'
info +=  f'Modificador: {borin.habilidades.modificadores['inteligencia']}\n'
info +=  f'Sabedoria: {borin.habilidades.sabedoria}\n'
info +=  f'Modificador: {borin.habilidades.modificadores['sabedoria']}\n'
info +=  f'Carisma: {borin.habilidades.carisma}\n'
info +=  f'Modificador: {borin.habilidades.modificadores['carisma']}\n'
info +=  f'Percepção Passiva: {borin.percepcao_passiva}\n'
info +=  f'Bônus de proeficiencia: {borin.bonus_proef}\n'
info +=  f'\nPerícias:\n'
for chave,valor in borin.pericias.items():
    info +=  f'{chave}: {valor}\n'
info +=  f'CA: {borin.armadura}\n'
info +=  f'Deslocamento: {borin.deslocamento}\n'
info += f'Vida: {borin.vida}\n'
info +=  f'\nInventário:\n'
for chave, valor in borin.inventario.items():
    info +=  f'{chave}: {valor}\n'
info += f'Aliados:{borin.aliados}\n'
info += f'Caracteristicas{borin.caracteristicas}\n'

