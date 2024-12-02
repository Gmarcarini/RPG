from habilidades import Habilidades
class Classes:
    def __init__(self, habilidades_classe, vida, experiencia):
        self.habilidades = habilidades_classe
        self.experiencia = experiencia
        self.nivel = self.niveis()
        self.vida = vida + self.habilidades.modificadores['constituicao']
        self.pericias = {
            'acrobacia': self.habilidades.modificadores['destreza'],
            'adestrar animais': self.habilidades.modificadores['sabedoria'],
            'arcanismo': self.habilidades.modificadores['inteligencia'],
            'atletismo': self.habilidades.modificadores['forca'],
            'atuacao': self.habilidades.modificadores['carisma'],
            'enaganacao': self.habilidades.modificadores['carisma'],
            'furtividade': self.habilidades.modificadores['destreza'],
            'historia': self.habilidades.modificadores['inteligencia'],
            'intimidacao': self.habilidades.modificadores['carisma'],
            'intuicao': self.habilidades.modificadores['sabedoria'],
            'investigacao': self.habilidades.modificadores['inteligencia'],
            'medicina': self.habilidades.modificadores['sabedoria'],
            'natureza': self.habilidades.modificadores['inteligencia'],
            'percepcao': self.habilidades.modificadores['sabedoria'],
            'persuasao': self.habilidades.modificadores['carisma'],
            'pretidigitacao': self.habilidades.modificadores['destreza'],
            'religiao': self.habilidades.modificadores['inteligencia'],
            'sobrevivencia': self.habilidades.modificadores['sabedoria']
        }
        self.bonus_proef = 0
        self.percepcao_passiva = 10 + self.pericias['percepcao']
        self.inventario = []
        self.duracao_especial = 10


class Barbaro:
    def __init__(self, habilidades):
        self.habilidades = habilidades
        self.experiencia = 0
        self.nivel = self.niveis()
        self.vida = 12 + self.habilidades.modificadores['constituicao']
        self.proef = ['armaduras leves', 'armaduras medias', 'escudos', 'armas simples', 'armas marciais', ]
        self.pericias = {
            'acrobacia': self.habilidades.modificadores['destreza'],
            'adestrar animais': self.habilidades.modificadores['sabedoria'],
            'arcanismo': self.habilidades.modificadores['inteligencia'],
            'atletismo': self.habilidades.modificadores['forca'] + self.bonus_proef,
            'atuacao': self.habilidades.modificadores['carisma'],
            'enaganacao': self.habilidades.modificadores['carisma'],
            'furtividade': self.habilidades.modificadores['destreza'],
            'historia': self.habilidades.modificadores['inteligencia'],
            'intimidacao': self.habilidades.modificadores['carisma'] + self.bonus_proef,
            'intuicao': self.habilidades.modificadores['sabedoria'],
            'investigacao': self.habilidades.modificadores['inteligencia'],
            'medicina': self.habilidades.modificadores['sabedoria'],
            'natureza': self.habilidades.modificadores['inteligencia'],
            'percepcao': self.habilidades.modificadores['sabedoria'],
            'persuasao': self.habilidades.modificadores['carisma'],
            'pretidigitacao': self.habilidades.modificadores['destreza'],
            'religiao': self.habilidades.modificadores['inteligencia'],
            'sobrevivencia': self.habilidades.modificadores['sabedoria']
        }
        self.bonus_proef = 0
        self.percepcao_passiva = 10 + self.pericias['percepcao']
        self.inventario = {
            'machado grande': 1,
            'machadinha': 2,
            'pacote de aventureiro': 1,
            'azagaia': 4
        }
        self.CA = 10 + self.habilidades.modificadores['destreza'] + self.habilidades.modificadores['constituicao']
        self.vida_anterior = 0
        self.forca_anterior = 0
        self.duracao_especial = 10
        self.furias = 2
    
    def niveis(self):
        if self.experiencia >= 0 and self.experiencia >300:
            self.nivel = 1
            self.bonus_proef = 2
        elif self.experiencia >= 300 and self.experiencia >900:
            self.nivel = 2
            self.bonus_proef = 2
        elif self.experiencia >= 900 and self.experiencia >2700:
            self.nivel = 3
            self.bonus_proef = 2
        elif self.experiencia >= 2700 and self.experiencia >6500:
            self.nivel = 4
            self.bonus_proef = 2
        elif self.experiencia >= 6500 and self.experiencia >14000:
            self.nivel = 5
            self.bonus_proef = 3
        elif self.experiencia >= 14000 and self.experiencia >23000:
            self.nivel = 6
            self.bonus_proef = 3
        elif self.experiencia >= 23000 and self.experiencia >34000:
            self.nivel = 7
            self.bonus_proef = 3
        elif self.experiencia >= 34000 and self.experiencia >48000:
            self.nivel = 8
            self.bonus_proef = 3
        elif self.experiencia >= 48000 and self.experiencia >64000:
            self.nivel = 9
            self.bonus_proef = 4
        elif self.experiencia >= 64000 and self.experiencia >85000:
            self.nivel = 10
            self.bonus_proef = 4
        elif self.experiencia >= 85000 and self.experiencia >100000:
            self.nivel = 11
            self.bonus_proef = 4
        elif self.experiencia >= 100000 and self.experiencia >120000:
            self.nivel = 12
            self.bonus_proef = 4
        elif self.experiencia >= 120000 and self.experiencia >140000:
            self.nivel = 13
            self.bonus_proef = 5
        elif self.experiencia >= 140000 and self.experiencia >165000:
            self.nivel = 14
            self.bonus_proef = 5
        elif self.experiencia >= 165000 and self.experiencia >195000:
            self.nivel = 15
            self.bonus_proef = 5
        elif self.experiencia >= 195000 and self.experiencia >225000:
            self.nivel = 16
            self.bonus_proef = 5
        elif self.experiencia >= 225000 and self.experiencia >265000:
            self.nivel = 17
            self.bonus_proef = 6
        elif self.experiencia >= 265000 and self.experiencia >305000:
            self.nivel = 18
            self.bonus_proef = 6
        elif self.experiencia >= 305000 and self.experiencia >355000:
            self.nivel = 19
            self.bonus_proef = 6
        elif self.experiencia >= 355000:
            self.nivel = 20
            self.bonus_proef = 6

    def furia(self):
        self.vida_anterior = self.vida
        self.forca_anterior = self.habilidades.forca
        self.vida += 3*self.nivel
        self.habilidades.forca += self.nivel
        self.habilidades.bonus()

    def desf_furia(self):
        self.vida = self.vida_anterior
        self.habilidades.forca = self.forca_anterior
        self.duracao_furia = 10
        self.habilidades.bonus()

class Bardo:
    def __init__(self, habilidades):
        pass

class Bruxo

class Clerigo

class Druida

class Feiticeiro

class Guerreiro

class Ladino

class Mago

class Monge

class Paladino

class Patrulheiro





hab_barbaro = Habilidades(15, 13, 14, 8, 12, 10)
barbaro = Barbaro(hab_barbaro,1)

hab_bardo = Habilidades(10, 14, 12, 8, 13, 15)
bardo = Bardo(hab_bardo)