from habilidades import Habilidades
class Classes:
    def __init__(self, nome, habilidades):
        self.nome = nome
        self.experiencia = 0
        self.habilidades = habilidades
        self.nivel = 0
        self.pericias = {
            'acrobacia': self.habilidades.modificadores['destreza'],
            'adestrar animais': self.habilidades.modificadores['sabedoria'],
            'arcanismo': self.habilidades.modificadores['inteligencia'],
            'atletismo': self.habilidades.modificadores['forca'],
            'atuacao': self.habilidades.modificadores['carisma'],
            'enganacao': self.habilidades.modificadores['carisma'],
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
        self.duracao_especial = None
        self.inventario = {}
        self.CA = 0

    def niveis(self):
        if self.experiencia >= 0 and self.experiencia < 300:
            self.nivel = 1
            self.bonus_proef = 2
        elif self.experiencia >= 300 and self.experiencia <900:
            self.nivel = 2
            self.bonus_proef = 2
        elif self.experiencia >= 900 and self.experiencia <2700:
            self.nivel = 3
            self.bonus_proef = 2
        elif self.experiencia >= 2700 and self.experiencia <6500:
            self.nivel = 4
            self.bonus_proef = 2
        elif self.experiencia >= 6500 and self.experiencia <14000:
            self.nivel = 5
            self.bonus_proef = 3
        elif self.experiencia >= 14000 and self.experiencia <23000:
            self.nivel = 6
            self.bonus_proef = 3
        elif self.experiencia >= 23000 and self.experiencia <34000:
            self.nivel = 7
            self.bonus_proef = 3
        elif self.experiencia >= 34000 and self.experiencia <48000:
            self.nivel = 8
            self.bonus_proef = 3
        elif self.experiencia >= 48000 and self.experiencia <64000:
            self.nivel = 9
            self.bonus_proef = 4
        elif self.experiencia >= 64000 and self.experiencia <85000:
            self.nivel = 10
            self.bonus_proef = 4
        elif self.experiencia >= 85000 and self.experiencia <100000:
            self.nivel = 11
            self.bonus_proef = 4
        elif self.experiencia >= 100000 and self.experiencia <120000:
            self.nivel = 12
            self.bonus_proef = 4
        elif self.experiencia >= 120000 and self.experiencia <140000:
            self.nivel = 13
            self.bonus_proef = 5
        elif self.experiencia >= 140000 and self.experiencia <165000:
            self.nivel = 14
            self.bonus_proef = 5
        elif self.experiencia >= 165000 and self.experiencia <195000:
            self.nivel = 15
            self.bonus_proef = 5
        elif self.experiencia >= 195000 and self.experiencia <225000:
            self.nivel = 16
            self.bonus_proef = 5
        elif self.experiencia >= 225000 and self.experiencia <265000:
            self.nivel = 17
            self.bonus_proef = 6
        elif self.experiencia >= 265000 and self.experiencia <305000:
            self.nivel = 18
            self.bonus_proef = 6
        elif self.experiencia >= 305000 and self.experiencia <355000:
            self.nivel = 19
            self.bonus_proef = 6
        elif self.experiencia >= 355000:
            self.nivel = 20
            self.bonus_proef = 6

class Barbaro(Classes):
    def __init__(self, nome, habilidades):
        super().__init__(nome, habilidades)
        self.niveis()
        self.vida = 12 + self.habilidades.modificadores['constituicao']
        self.proef = ['armaduras leves', 'armaduras medias', 'escudos', 'armas simples', 'armas marciais', ]
        self.pericias['atletismo'] = self.pericias['atletismo'] + self.bonus_proef
        self.pericias['intimidacao'] = self.pericias['intimidacao'] + self.bonus_proef
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


    def especial(self):
        #furia
        self.vida_anterior = self.vida
        self.forca_anterior = self.habilidades.forca
        self.vida += 3*self.nivel
        self.habilidades.forca += self.nivel
        self.habilidades.bonus()

    def desf_furia(self):
        self.vida = self.vida_anterior
        self.habilidades.forca = self.forca_anterior
        self.habilidades.bonus()

class Bardo(Classes):
    def __init__(self, nome, habilidades):
        super().__init__(nome, habilidades)
        self.niveis()
        self.vida = 8 + self.habilidades.modificadores['constituicao']
        self.proef = ['armaduras leves' , 'armas simples', 'besta de mao', 'espadas longas', 'rapieiras', 'espadas curtas', 'banjo', 'flauta', 'batuque' ]
        self.pericias['persuasao']+= self.bonus_proef
        self.pericias['atuacao'] += self.bonus_proef
        self.pericias['enganacao'] += self.bonus_proef
        self.percepcao_passiva = 10 + self.pericias['percepcao']
        self.inventario = {
            'espada longa': 1,
            'flauta': 1,
            'armadura de couro': 1
        }
        self.CA = 10 + self.habilidades.modificadores['destreza'] + self.habilidades.modificadores['constituicao']
        self.truques = ['globo de luz', 'zombaria viciosa']
        self.magias = ['enfeiticar pessoa', 'detectar magia', 'palavra curativa', 'onda trovejante']
        self.espacos_magia = 2


    def especial(self):
        #inspiracao bardica
        return f'A criatura aliada mais próxima do jogador ganha um d6 a mais na proxima rolagem'


class Ladino(Classes):
    def __init__(self, nome, habilidades):
        super().__init__(nome, habilidades)
        self.niveis()
        self.vida = 8 + self.habilidades.modificadores['constituicao']
        self.proef = ['armaduras leves', 'armas simples', 'besta de mao', 'espadas longas', 'rapieiras', 'espadas curtas', 'ferramentas de ladrão']
        self.pericias['atuacao'] += self.bonus_proef
        self.pericias['acrobacia'] += self.bonus_proef
        self.pericias['furtividade'] += self.bonus_proef
        self.pericias['intuicao'] += self.bonus_proef
        self.percepcao_passiva = 10 + self.pericias['percepcao']
        self.inventario = {
            'rapieira': 1,
            'arco curto': 1,
            'aljava com 20 flechas': 1,
            'kit de assaltante': 1,
            'ferramentas de ladrão': 1
        }
        self.CA = 11 + self.habilidades.modificadores['destreza']
        self.ataque_furtivo = self.nivel + self.habilidades.modificadores['destreza']

    def especial(self):
       #ataquefurtivo
        return f'Uma vez por turno, voce pode adicionar 1d6 na jogada de dano'

class Mago(Classes):
    def __init__(self, nome, habilidades):
        super().__init__(nome, habilidades)
        self.niveis()
        self.vida = 6 + self.habilidades.modificadores['constituicao']
        self.proef = [ 'adagas', 'dardos', 'fundas', 'bastões', 'bestas leves']
        self.pericias['arcanismo'] += self.bonus_proef
        self.pericias['historia'] += self.bonus_proef
        self.percepcao_passiva = 10 + self.pericias['percepcao']
        self.inventario = {
            'grimório': 1,
            'bolsa de componentes': 1,
            'kit de estudioso':1,
            'bastao': 1,
            'adaga':1

        }
        self.CA = 10 + self.habilidades.modificadores['destreza']
        self.truques = ['luz', 'prestidigitação', 'raio de gelo', 'toque chocante']
        self.magias = ['misseis mágicos', 'escudo arcano','sono']

    def especial(self):
        #recuperacao arcana
        return f'Uma vez por dia, após um descanso curto, o jogador pode recuperar espacos de magia gastos'
    
class Paladino(Classes):
    def __init__(self, nome, habilidades):
        super().__init__(nome, habilidades)
        self.niveis()
        self.vida = 10 + self.habilidades.modificadores['constituicao']
        self.proef = ['todas as armaduras' , 'escudos', 'armas simples', 'armas marciais' ]
        self.pericias['intuicao'] += self.bonus_proef
        self.pericias['medicina'] += self.bonus_proef
        self.percepcao_passiva = 10 + self.pericias['percepcao']
        self.inventario = {
            'espada longa': 1,
            'escudo': 1,
            '5 azagaias': 5,
            'kit de sacerdote': 1,
            'simbolo sagrado': 1
        }
        self.CA = 18 #armadura de placas completa
        self.magias = ['auxilio divino','bencao']
        self.cura_maos = 5


    def especial(self):
        #cura pelas maos
        return f'O jogador pode curar uma criatura com um toque'

hab_barbaro = Habilidades(15, 13, 14, 8, 12, 10)
barbaro = Barbaro('Barbaro', hab_barbaro)

hab_bardo = Habilidades(10, 14, 12, 8, 13, 15)
bardo = Bardo('Bardo', hab_bardo)

hab_ladino = Habilidades(12, 15, 8, 14, 13, 10)
ladino = Ladino('Ladino', hab_ladino)

hab_mago = Habilidades(8, 12, 10, 15, 14, 13)
mago = Mago('Mago', hab_mago)

hab_paladino = Habilidades(15, 12, 13, 10, 8 ,14)
paladino = Paladino('Paladino', hab_paladino)

print(bardo.bonus_proef)
