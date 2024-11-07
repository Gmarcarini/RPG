class Itens:
    def __init__(self, nome, descricao, dano, defesa, acao):
        self.nome = nome
        self.descricao = descricao
        self.dano = dano
        self.defesa = defesa 
        self.acao = acao 
        
class Melees(Itens):
    def __init__(self, nome, descricao, dano, defesa, acao, preforca, predex, preinteligencia, precarisma):
        super().__init__(nome, descricao, dano, defesa, acao)
        self.preforca = preforca
        self.predex = predex
        self.preinteligencia = preinteligencia
        self.precarisma = precarisma

adaga = Melees('Adaga','Lâmina curta e leve, perfeita para ataques rápidos e furtivos, especialmente eficaz nas mãos de assassinos e ladinos')
maca_ferro = Melees('Maça de Ferro','Arma de impacto com uma cabeça pesada de ferro, ótima para esmagar armaduras e infligir danos contundentes.' )
espada = Melees('Espada','Lâmina de alcance médio, versátil e confiável, adequada para diversos estilos de combate.')
machado_guerra = Melees('Machado de Guerra','Machado robusto com uma lâmina pesada, ideal para golpes devastadores que podem partir armaduras.')
lanca = Melees('Lança','Arma de longo alcance com uma ponta afiada, excelente para manter inimigos à distância ou em ataques montados.')
foice = Melees('Foice','Ferramenta adaptada para combate, com lâmina curva que pode desferir cortes profundos e rasgar carne com facilidade.')
katana = Melees('Katana','Espada com uma lâmina curva e afiada, famosa pela precisão e cortes rápidos.')
manopla = Melees('Manopla','Proteção para as mãos que também serve como arma de impacto, ideal para esmurrar adversários com força.')
martelo_guerra = Melees('Martelo de Guerra', 'Arma poderosa e pesada, projetada para esmagar e desestabilizar, especialmente eficaz contra armaduras.')
porrete = Melees('Porrete','Bastão simples de madeira, uma arma contundente e acessível, útil em combates improvisados.')
banjo = Melees('Banjo', 'Instrumento musical de cordas, muitas vezes companheiro de bardos em aventuras, capaz de encantar ou animar com suas melodias.')


class Cajados(Itens):
    def __init__(self, nome, descricao, dano, defesa, acao, preinteligencia, predex):
        super().__init__(nome, descricao, dano, defesa, acao)
        self.preinteligencia = preinteligencia
        self.predex = predex

cajado = Cajados('Cajado','Vara de madeira simples e confiável, canaliza energia mágica para feitiços básicos.')
cajado_bruxo = Cajados('Cajado de Bruxo','Versão aprimorada do cajado, ornamentado e imbuído com magias mais poderosas para encantamentos sombrios.')
cajado_mestre = Cajados('Cajado de Mestre', 'Um cajado lendário, com runas e adornos mágicos, usado por mestres em artes arcanas para feitiços de grande poder.')


class Armaduras(Itens):
    def __init__(self, nome, descricao, dano, defesa, acao, preforca, preconst):
        super().__init__(nome, descricao, dano, defesa, acao)
        self.preforca = preforca
        self.preconst = preconst 

class Escudos(Itens):
    def __init__(self, nome, descricao, dano, defesa, acao, preforca):
        super().__init__(nome, descricao, dano, defesa, acao)
        self.preforca = preforca 

#Escudos
escudo_leve = Escudos('Escudo de couro', 'Um escudo de madeira pequeno')
escudo_medio = Escudos()
escudo_pesado = Escudos()

class Spells(Itens):
    def __init__(self, nome, descricao, dano, defesa, acao, preinteligencia):
        super().__init__(nome, descricao, dano, defesa, acao)
        self.preinteligencia = preinteligencia

#Spells
Fireball = Spells('Bola de Fogo','Explosão de fogo devastadora, causando dano em uma área ao redor do alvo.')
Healing_word = Spells('Cura Arcana', 'Feitiço de cura rápida, restaura a saúde de aliados com uma palavra mágica.')
Mage_hand = Spells('Mão mágica','Mão espectral que pode manipular objetos a distância, útil para tarefas rápidas e seguras.')
Shield= Spells('Escudo','Conjura um escudo mágico instantâneo, protegendo contra ataques iminentes.')
Invisibility = Spells('Sumiu','Encantamento que torna o usuário invisível por tempo limitado, útil para infiltração e fuga.')
Lightning_Bolt = Spells('Trovoada','Feixe de eletricidade concentrada que atravessa inimigos em linha reta, causando grande dano.')
Hold_Person = Spells('Paralise!','Paralisia mágica que imobiliza o alvo, impedindo qualquer movimento.')
Counterspell = Spells('Hoje não','Anula magias lançadas por outros, dissipando feitiços antes que surtam efeito.')

#geral
pocao_cura = Itens('Poção de Cura',' Frasco com líquido revitalizante, restaura pontos de vida ao ser ingerido.')
pocao_dano = Itens('Poção de Dano','Bebida mortal que, ao ser usada contra inimigos, causa envenenamento ou dano direto.')
pocao_defesa = Itens('Poção de Defesa','Proporciona uma proteção temporária, aumentando a resistência do usuário.')
anel_protecao = Itens('Anel Proteção','Anel encantado que cria uma barreira mágica, aumentando a defesa contra ataques.')
talisma_sorte = Itens('Talisma da Sorte','Amuleto raro que proporciona um leve aumento na sorte do portador.')
pergaminho_magia = Itens('Pergaminho de Magia',' Contém um feitiço selado, podendo ser lido para lançar a magia inscrita.')
orelha_fada = Itens('Orelha de fada','Rara e mística, contém resquícios de magia, usada em poções e rituais arcanos.')
fruta_magica = Itens('Fruta mágica', 'Uma fruta encantada que concede habilidades temporárias ao ser consumida.')
cabeça_tarrasque  = Itens('Cabeça de Tarrasque','Troféu monstruoso, prova de uma vitória épica contra uma das mais temidas criaturas.')