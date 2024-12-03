import random

class Personagem:
    def __init__(self, nome, classe, raca, antecedente, tendencia, iniciativa,
                 deslocamento, vida, resistencias, idiomas, aliados, caracteristicas, tesouro):
        self.nome = nome
        self.classe = classe
        self.nivel = classe.nivel
        self.raca = raca
        self.antecedente = antecedente
        self.tendencia = tendencia
        self.habilidades = classe.habilidades
        self.bonus_proef = classe.bonus_proef
        self.armadura = classe.CA
        self.iniciativa = iniciativa
        self.deslocamento = deslocamento
        self.vida = vida
        self.resistencias = resistencias
        self.percepcao_passiva = classe.percepcao_passiva
        self.pericias = classe.pericias
        self.idiomas = idiomas
        self.proeficiencias = classe.proef
        self.equipamentos = classe.inventario
        self.altura = raca.altura
        self.peso = raca.peso
        self.aliados = aliados
        self.caracteristicas = caracteristicas
        self.tesouro = tesouro
    
    def Rolagens(self):
        dados = f'Força: {random.randint(1,20) + self.habilidades.modificadores['forca']}'
        dados =+ f'Destreza: {random.randint(1,20) + self.habilidades.modificadores['destreza']}'
        dados =+ f'Constituicao: {random.randint(1,20) + self.habilidades.modificadores['constituicao']}'
        dados =+ f'Inteligencia: {random.randint(1,20) + self.habilidades.modificadores['inteligencia']}'
        dados =+ f'Sabedoria: {random.randint(1,20) + self.habilidades.modificadores['sabedoria']}'
        dados =+ f'Carisma: {random.randint(1,20) + self.habilidades.modificadores['carisma']}'
        return dados

