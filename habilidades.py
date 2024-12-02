class Habilidades:
    def __init__(self, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma
        self.modificadores = {
            'forca': 0,
            'destreza': 0,
            'constituicao': 0,
            'inteligencia': 0,
            'sabedoria': 0,
            'carisma': 0,
        }
        self.bonus()

    def bonus(self):
        atributos = {
            'forca': self.forca,
            'destreza': self.destreza,
            'constituicao': self.constituicao,
            'inteligencia': self.inteligencia,
            'sabedoria': self.sabedoria,
            'carisma': self.carisma,
        }

        for nome, valor in atributos.items():
            if valor == 1:
                self.modificadores[nome] = -5
            elif valor == 2 or valor == 3:
                self.modificadores[nome] = -4
            elif valor == 4 or valor == 5:
                self.modificadores[nome] = -3
            elif valor == 6 or valor == 7:
                self.modificadores[nome] = -2
            elif valor == 8 or valor == 9:
                self.modificadores[nome] = -1
            elif valor == 10 or valor == 11:
                self.modificadores[nome] = 0
            elif valor == 12 or valor == 13:
                self.modificadores[nome] = +1
            elif valor == 14 or valor == 15:
                self.modificadores[nome] = +2
            elif valor == 16 or valor == 17:
                self.modificadores[nome] = +3
            elif valor == 18 or valor == 19:
                self.modificadores[nome] = +4
            elif valor == 20 or valor == 21:
                self.modificadores[nome] = +5
            elif valor == 22 or valor == 23:
                self.modificadores[nome] = +6
            elif valor == 24 or valor == 25:
                self.modificadores[nome] = +7
            elif valor == 26 or valor == 27:
                self.modificadores[nome] = +8
            elif valor == 28 or valor == 29:
                self.modificadores[nome] = +9
            elif valor == 10:
                self.modificadores[nome] = +10
            else:
                self.modificadores[nome] = 0
