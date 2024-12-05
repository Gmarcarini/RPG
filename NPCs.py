from jogador import Personagem
from racas import dono_bar, bebado, ajudante, reginald

class NPCs(Personagem):
    def __init__(self, nome, raca, tendencia, ocupacao, aparencia, caracteristicas, motivacao, adicionais, tesouro):
        self.nome = nome
        self.raca = raca.nome
        self.classe = raca.classe.nome
        self.tendencia = tendencia
        self.ocupacao = ocupacao

        self.habilidades = raca.classe.habilidades
        self.CA = raca.classe.CA
        self.vida = raca.classe.vida
        self.deslocamento = raca.deslocamento
        self.bonus_proef = raca.classe.bonus_proef
        self.proef_pericias = raca.classe.proef_pericias
        self.atr_pericias()

        self.idiomas = raca.idiomas
        self.aparencia = aparencia
        self.caracteristicas_tracos = caracteristicas
        self.motivacao = motivacao
        self.adicionais = adicionais
        self.tesouro = tesouro

    def __str__(self):
        ficha = (
            f"=== Ficha de NPC ===\n"
            f"Nome: {self.nome}\n"
            f"Raça: {self.raca}\n"
            f"Classe: {self.classe}\n"
            f"Tendência: {self.tendencia}\n"
            f"Ocupação: {self.ocupacao}\n"
            f"CA: {self.CA}\n"
            f"Vida: {self.vida}\n"
            f"Deslocamento: {self.deslocamento} m\n"
            f"Bônus de Proficiência: {self.bonus_proef}\n"
            f"Idiomas: {', '.join(self.idiomas)}\n"
            f"Aparência: {self.aparencia}\n"
            f"Características e Traços: {self.caracteristicas_tracos}\n"
            f"Motivação: {self.motivacao}\n"
            f"Detalhes Adicionais: {self.adicionais}\n"
            f"Tesouro: {self.tesouro}\n"
        )

        habilidades = "\n".join(
            f"  {atributo.capitalize()}: {getattr(self.habilidades, atributo)}"
            for atributo in dir(self.habilidades)
            if not atributo.startswith("_") and not callable(getattr(self.habilidades, atributo))
        )

        pericias = "\n".join(
            f"  {pericia.capitalize()}: {'(proficiente)' if pericia in self.proef_pericias else ''} {getattr(self.habilidades, pericia)}"
            for pericia in dir(self.habilidades)
            if not pericia.startswith("_") and not callable(getattr(self.habilidades, pericia))
        )

        ficha += (
            f"=== Habilidades ===\n{habilidades}\n"
            f"=== Perícias ===\n{pericias}\n"
        )

        return ficha
    

grimbeard = NPCs('Grimbeard Pedra-firme', dono_bar, 'Neutro Bom', 'Dono da Taverna "Machado Enferrujado"', 'Grimbeard é um anão barrigudo, com uma barba longa e espessa que chega a seus joelhos, trançada com fios de cobre. Ele usa um avental manchado de cerveja sobre roupas simples e confortáveis. Seus olhos castanho-escuros brilham com astúcia e bom humor. Apesar de sua aparência jovial, ele tem uma presença imponente, e seus clientessabem que é melhor não se meter com ele.', 'Grimbeard é um anão acolhedor e jovial, sempre pronto para uma boa conversa e uma caneca de cerveja gelada. Ele é um fofoqueiro inveterado e parece saber de tudo o que acontece na cidade, desde os negócios escusos nos becos até os romances secretos da nobreza. Ele é um ótimo contador de histórias, mas costuma embelezar os fatos para torná-los mais interessantes. Ele está sempre disposto a trocar informações por um pouco de ouro, especialmente se a informação for escandalosa ou comprometedora. Apesar de seu bom humor, ele é um negociante astuto e não tolera trapaças em seu estabelecimento. Ele é profundamente leal à sua comunidade e aos seus amigos, e faria qualquer coisa para protegê-los.', 'Motivação: Manter sua taverna funcionando e próspera, ser um pilar da comunidade e, secretamente, juntar ouro suficiente para se aposentar em uma confortável casa nas montanhas.', 'Grimbeard possui um velho cão mastim chamado Barril, que costuma dormir perto da lareira da taverna. Ele tem uma coleção impressionante de canecas de cerveja, cada uma com uma história única. Grimbeard desconfia de aventureiros, pois eles costumam causar problemas e raramente pagam suas contas em dia. No entanto, ele os tolera, pois eles trazem boas histórias e, às vezes, até pagam suas dívidas.', 250)

baruk = NPCs('Baruk', bebado, 'Caótico Neutro', 'Bêbado', 'Baruk é um meio-orc desgrenhado e sujo, com roupas rasgadas e manchadas de bebida. Seus olhos injetados de sangue vagueiam sem foco, e seu hálito carrega o forte odor de cerveja azeda. Ele tem uma barba rala e desgrenhada, e sua pele esverdeada está coberta de cicatrizes e arranhões.', 'Baruk é um bêbado rabugento e imprevisível, sempre pronto para uma briga ou uma discussão sem sentido. Ele é um mentiroso compulsivo e um ladrão oportunista, e não hesita em enganar ou roubar aqueles ao seu redor (incluindo seus "amigos"). Apesar de sua natureza desagradável, ele possui um estranho carisma, e muitas vezes consegue convencer os outros a lhe dar dinheiro ou bebida. Ele tem um medo irracional de água e se recusa a tomar banho.', 'Nenhum. Baruk se importa apenas consigo mesmo e com sua próxima bebida.', 'Baruk já foi um guerreiro respeitado em sua tribo, mas seu vício em bebida o levou à ruína. Ele foi expulso de sua tribo e agora vive como um mendigo nas ruas da cidade, passando seus dias na taverna "Machado Enferrujado", onde ele tenta conseguir bebida de graça ou dinheiro para comprar mais. Ele se lembra vagamente de sua antiga vida, mas prefere esquecer seu passado vergonhoso.', 1)

bruhilda = NPCs('Bruhilda Stormblade', ajudante, 'Caótico Neutro', 'Ajudante da Guilda  de Aventureiros no Machado Enferrujado', 'Brunhilda é uma mulher musculosa e imponente, com uma cicatriz marcante no olho direito. Ela mantém uma expressão carrancuda e fala pouco, preferindo se comunicar com grunhidos e gestos bruscos. Suas roupas são simples e práticas, projetadas para o combate, e ela raramente é vista sem seus dois machados de guerra.', 'Brunhilda é conhecida por sua atitude rude e agressiva. Ela não  tem paciência para conversa fiada ou gentilezas, e não hesita em usar a força para resolver seus problemas. Apesar de sua natureza bruta, ela possui um forte senso de justiça e lealdade à guilda, e sempre cumpre seus contratos. Ela tem um fraco por animais, especialmente cachorros de guerra, e secretamente sonha em ter seu próprio canil.', '"Eu nunca deixarei que alguém machuque meus amigos da guilda."', 'Brunhilda cresceu em uma família pobre e aprendeu a lutar desde cedo para sobreviver. Ela se juntou à guilda de aventureiros para ganhar a vida e provar seu valor, e rapidamente se destacou por sua força e habilidade com os machados. A cicatriz em seu olho é uma lembrança de um combate particularmente brutal contra um grupo de orcs, o que a deixou ainda mais desconfiada e agressiva.', 15)

sir_reginald = NPCs('Sir Reginald', reginald, 'Leal Bom', 'Cavaleiro Errante', 'Sir Reginald é um homem imenso, com uma armadura de placas branca reluzente e detalhes em dourado. Sua presença impõe respeito, mesmo quando ele está realizando tarefas mundanas, como polir sua escada gigante (que ele carrega em suas costas, presa por um sistema de tiras e fivelas).', 'Sir Reginald é um cavaleiro devoto e honrado, seguindo rigidamente os princípios de seu juramento. Ele é educado e cortês com todos, mesmo com seus inimigos. No entanto, sua obsessão pela limpeza e ordem pode beirar o patológico. Ele passa horas polindo sua armadura, escudo e escada (que, na sua opinião, é uma ferramenta essencial para um cavaleiro), mesmo que eles já estejam impecavelmente limpos.', 'Ordem. "Tudo tem seu lugar e seu propósito. O caos é o inimigo da civilização." (Leal)', 'Sir Reginald nasceu em uma família nobre e foi treinado desde cedo para ser um cavaleiro. Ele sempre foi um perfeccionista, e essa característica se intensificou após ele fazer seu juramento de paladino. Ele acredita que a limpeza e a ordem são reflexos da pureza da alma, e se esforça para manter tudo ao seu redor impecável. Ele viaja pelo mundo como um cavaleiro errante, buscando ajudar os necessitados e combater o mal, mas sempre encontra tempo para polir sua armadura, seu escudo e, claro, sua escada gigante.', 100)