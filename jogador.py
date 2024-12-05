import random
from racas import anao_montanha, gnomo_floresta, tieflings, meio_elfo, draconato
from habilidades import Pericias

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
        self.proef_pericias = self.classe.proef_pericias
        self.atr_pericias()
        self.armadura = self.classe.CA
        self.deslocamento = raca.deslocamento
        self.vida = self.classe.vida
        self.percepcao_passiva = 10 + self.pericias.percepcao
        self.idiomas = raca.idiomas
        self.proeficiencias = self.classe.proef_itens
        self.equipamentos = self.classe.inventario
        self.altura = raca.altura
        self.peso = raca.peso
        self.aliados = aliados
        self.caracteristicas = caracteristicas
        self.tesouro = tesouro
        self.inventario = {**self.classe.inventario, **inventario}

    def rolagens(self):
        dados = f'Força: ({random.randint(1,20)}) + ({self.habilidades.modificadores['forca']})'
        dados += f'Destreza: {random.randint(1,20) + self.habilidades.modificadores['destreza']}'
        dados += f'Constituicao: {random.randint(1,20) + self.habilidades.modificadores['constituicao']}'
        dados += f'Inteligencia: {random.randint(1,20) + self.habilidades.modificadores['inteligencia']}'
        dados += f'Sabedoria: {random.randint(1,20) + self.habilidades.modificadores['sabedoria']}'
        dados += f'Carisma: {random.randint(1,20) + self.habilidades.modificadores['carisma']}'
        return dados
    
    def atr_pericias(self):
        self.pericias = Pericias(self.bonus_proef, self.proef_pericias, self.habilidades)

    def to_dict(self):
        """Converte o objeto em um dicionário com base no formato de __str__."""
        return {
            "nome": self.nome,
            "classe": {
                "nome": self.classe.nome,
                "nivel": self.nivel
            },
            "raca": self.raca.nome,
            "antecedente": self.antecedente,
            "tendencia": self.tendencia,
            "armadura": self.armadura,
            "vida": self.vida,
            "deslocamento": self.deslocamento,
            "percepcao_passiva": self.percepcao_passiva,
            "idiomas": self.idiomas,
            "proeficiencias": self.proeficiencias,
            "altura": self.altura,
            "peso": self.peso,
            "aliados": self.aliados if self.aliados else [],
            "caracteristicas": self.caracteristicas,
            "tesouro": self.tesouro,
            "habilidades": {
                atributo: getattr(self.habilidades, atributo)
                for atributo in dir(self.habilidades)
                if not atributo.startswith("_") and not callable(getattr(self.habilidades, atributo))
            },
            "pericias": {
                pericia: {
                    "valor": getattr(self.pericias, pericia),
                    "proficiente": pericia in self.proef_pericias
                }
                for pericia in dir(self.pericias)
                if not pericia.startswith("_") and not callable(getattr(self.pericias, pericia))
            },
            "inventario": self.inventario
        }

    def __str__(self):
        ficha = (
            f"=== Ficha do Personagem ===\n"
            f"Nome: {self.nome}\n"
            f"Classe: {self.classe.nome} (Nível {self.nivel})\n"
            f"Raça: {self.raca.nome}\n"
            f"Antecedente: {self.antecedente}\n"
            f"Tendência: {self.tendencia}\n"
            f"Armadura: {self.armadura}\n"
            f"Vida: {self.vida}\n"
            f"Deslocamento: {self.deslocamento} m\n"
            f"Percepção Passiva: {self.percepcao_passiva}\n"
            f"Idiomas: {', '.join(self.idiomas)}\n"
            f"Proeficiências: {', '.join(self.proeficiencias)}\n"
            f"Altura: {self.altura}\n"
            f"Peso: {self.peso} kg\n"
            f"Aliados: {', '.join(self.aliados) if self.aliados else 'Nenhum'}\n"
            f"Características e Traços: {self.caracteristicas}\n"
            f"Tesouro: {self.tesouro}\n"
        )

        habilidades = "\n".join(
            f"  {atributo.capitalize()}: {getattr(self.habilidades, atributo)}"
            for atributo in dir(self.habilidades)
            if not atributo.startswith("_") and not callable(getattr(self.habilidades, atributo))
        )

        # Processa perícias
        pericias = "\n".join(
            f"  {pericia.capitalize()}: {'(proficiente)' if pericia in self.proef_pericias else ''} {getattr(self.pericias, pericia)}"
            for pericia in dir(self.pericias)
            if not pericia.startswith("_") and not callable(getattr(self.pericias, pericia))
        )

        # Processa inventário
        equipamentos = "\n".join(
            f"  - {item}: {quantidade}" for item, quantidade in self.inventario.items()
        )

        ficha += (
            f"=== Habilidades ===\n{habilidades}\n"
            f"=== Perícias ===\n{pericias}\n"
            f"=== Equipamentos ===\n{equipamentos}\n"
        )

        return ficha

borin = Personagem('Borin Pedra-Rachada', anao_montanha, 'forasteiro', 'Caótico bom', {'Clã Pedra-Rachada': 'exilado', 'Liga dos Exploradores da Montanha Rochosa': 'iniciante'}, ' Impulsivo, corajoso até a beira da imprudência, leal aos seus amigos, desconfiado de estranhos (especialmente elfos), tem um fraco por crianças e animais indefesos.  Liberdade. "Ninguém me diz o que fazer. A montanha é meu único mestre." Eu devo vingança ao gigante do gelo que matou meu irmão e roubou o totem do meu clã. Eu tenho um pavio curto e me irrito com facilidade, especialmente quando alguém questiona minha coragem ou zomba da minha altura.', 50, {'pequena pepita de ouro': 1, 'Cordao de dente de lobo': 1})

elara = Personagem('Elara Whisperwind', meio_elfo, 'Artistica', 'Caótica Boa', {'Companhia Andante Melodia da Aurora': 'integrante', 'Santuário da Deusa da Música': 'Formada'}, 'Ela carrega consigo um alaúde finamente trabalhado e um escudo decorado com pinturas de cenas da natureza. Elara é gentil, compassiva e possui um talento natural para a música e a poesia. Ela encanta a todos com suas melodias suaves e suas histórias inspiradoras, e acredita que a música tem o poder de curar feridas e unir as pessoas. Ela é uma idealista incurável, sempre buscando o bem no mundo, mas também é pragmática e sabe se defender quando necessário. Ela é um pouco ingênua em relação à maldade do mundo, mas está sempre disposta a aprender e crescer.', 20,  {'Um pequeno diario de poesias': 1, 'Colar de prata com um pingente em forma de clave de sol': 1, 'kit de primeiros socorros': 1})

pipkin = Personagem('Pipkin Quickfoot', gnomo_floresta, 'Charlatão', 'Caótico Neutro', {'Trupe Circense Os Malabares da Meia-Noite': 'ex-participante', 'Guilda dos Mercadores Ambulantes': 'participante'}, 'Pipkin é um charlatão nato, sempre pronto para um bom golpe ou uma piada. Ele é inteligente, criativo e carismático, e sabe como usar suas palavras e sua lábia para manipular e enganar os outros. Ele adora pregar peças e se divertir às custas dos outros, mas também tem um bom coração e, às vezes, ajuda aqueles que precisam (especialmente se isso lhe for conveniente). Ele é um pouco covarde e prefere evitar o confronto direto, mas é um mestre em se esquivar do perigo e escapar de situações complicadas. Liberdade. "Regras são para os tolos. Eu faço minhas próprias regras." (Caótico) Eu preciso encontrar o tesouro perdido do Grande Gnomo Trapaceiro. É meu destino! Eu sou ganancioso e egoísta, e faria qualquer coisa por dinheiro (mesmo que isso signifique trair meus amigos).', 25, {'Baralho de cartas marcadas': 1, 'Pequena caixa de música gnômica': 1})

zaltarian = Personagem('Zaltarian Galdhar', tieflings, 'Sábio', 'Caótico Neutro', {'Academia Arcana de Thassilon': 'exaluno', 'Ordem dos Olhos Secretos': 'participante'}, 'Zaltarian é um estudioso dedicado e um pesquisador incansável do conhecimento arcano. Ele é inteligente, curioso e ambicioso, e acredita que a magia é a chave para desvendar os segredos do multiverso. Ele é um tanto arrogante e prepotente, e tende a subestimar aqueles que não possuem seus dons mágicos. Ele tem um fascínio pelo oculto e pelo proibido, e não hesita em se aventurar em lugares perigosos ou lidar com forças sombrias em busca de conhecimento. Conhecimento. "O conhecimento é poder. Eu irei desvendar todos os segredos do multiverso, não importa o custo." (Neutro) "Eu preciso encontrar os fragmentos perdidos do grimório de Thassilon. Ele contém conhecimentos arcanos que foram perdidos para as eras." "Minha sede por conhecimento pode me cegar para o perigo. Às vezes, eu estou disposto a arriscar tudo, até mesmo minha vida, por uma chance de descobrir algo novo."', 15, {'pequeno amuleto de obsidiana': 1, 'Livro de magias com anotações e diagramas arcanos': 1, 'kit de primeiros socorros': 1})

kael = Personagem('Kael Brassscale', draconato, 'Soldado', 'Leal Bom', {'Legião da Aurora': 'exsoldado', 'Culto de Bahamut': 'participante'}, 'Kael é um paladino devoto e disciplinado, seguindo rigidamente os princípios de seu juramento. Ele é corajoso, leal e honrado, e sempre coloca o bem-estar dos outros acima do seu próprio. Ele é um pouco sério e reservado, mas também possui um senso de humor seco e sarcástico. Ele acredita que é seu dever proteger os fracos e os inocentes, e não hesita em usar a força para combater o mal. Justiça. "Eu defenderei os fracos e punirei os ímpios, sem exceção." (Leal)  "Eu devo lealdade aos meus companheiros de armas e honrarei a memória daqueles que tombaram em batalha." "Eu sou teimoso e orgulhoso, e às vezes me recuso a recuar, mesmo quando a situação exige."', 50, {'insígnia da Legião da Aurora': 1, 'livro pequeno de orações com a capa de couro': 1, 'kit de primeiros socorros': 1})

personagem = Personagem('Borin Pedra-Rachada', anao_montanha, 'forasteiro', 'Caótico bom', {'Clã Pedra-Rachada': 'exilado', 'Liga dos Exploradores da Montanha Rochosa': 'iniciante'}, ' Impulsivo, corajoso até a beira da imprudência, leal aos seus amigos, desconfiado de estranhos (especialmente elfos), tem um fraco por crianças e animais indefesos.  Liberdade. "Ninguém me diz o que fazer. A montanha é meu único mestre." Eu devo vingança ao gigante do gelo que matou meu irmão e roubou o totem do meu clã. Eu tenho um pavio curto e me irrito com facilidade, especialmente quando alguém questiona minha coragem ou zomba da minha altura.', 50, {'pequena pepita de ouro': 1, 'Cordao de dente de lobo': 1})

