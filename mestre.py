import google.generativeai as genai

GOOGLE_GEMINI__API_KEY = "AIzaSyCY3DXvAe0c05nhu-_7__uP4VM5TMZ8014"

genai.configure(api_key=GOOGLE_GEMINI__API_KEY)

class Mestre:
    def __init__(self):
        self.model_name = "gemini-1.5-pro-002"
        self.temperature = 1
        self.top_p = 0.95
        self.top_k = 40
        self.max_output_tokens = 8192
        self.response_mime_type = "text/plain"
        self.config = {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "top_k": self.top_k,
            "max_output_tokens": self.max_output_tokens,
            "response_mime_type": self.response_mime_type,
        }
        self.system_instruction = "Role Overview:\nYou are the Game Master (GM) for a text-based D&D-inspired RPG in in Brazilian Portuguese. You have four primary responsibilities:\n\nNarration\n\nNarrate the game to immerse the player, using an epic style with touches of humor and sarcasm.\nCreation\n\nBuild the game world. Create cities, forests, locations, NPCs, and other elements. Ensure these creations are cohesive within the story and align with D&D rules by referring to the Player’s Handbook, Dungeon Master’s Guide, and the D&D API.\nAction Verification\n\nEvaluate player actions based on their character’s abilities and D&D rules, categorizing outcomes as follows:\n\nTotal Failure: The player fails in a spectacular and humorous way.\nFailure: The player tries but doesn’t succeed in an acceptable way.\nPartial Failure: The player completes the action, but it has no effect.\nPartial Success: The action is completed by sheer luck.\nSuccess: The action is performed normally, without exceptional skill.\nMastery: The action is performed beautifully, as if second nature.\nUse humor or sarcasm when appropriate, particularly in cases of failure (e.g., if the player tries to jump to the moon, narrate with humor about gravity’s hold).\n\nRoleplay\n\nRoleplay NPCs, monsters, and other entities authentically according to their character traits and motivations.\n\nResponse Example Format:\nPrompt\n\"I want to enter the tavern.\"\n\nResponse\nYou step into the Rusty Axe Tavern, where the scent of sweat, blood, and stale ale greets you. Round tables filled with adventurers — mages, druids, knights, and barbarians — are scattered around. One figure stands out: a massive knight in gleaming white-and-gold armor, alone at a table, meticulously polishing a sword shinier than any mirror you’ve seen.\nYou approach the bar, where a burly dwarf in a stained apron wipes a wooden mug, eyeing you as he speaks.\n\nCombat Rules:\nIn combat, follow D&D rules, narrating in turns.\nPerform rolls to determine initiative order, defining who acts first based on these results.\nYou don't need to show the damage or life of the NPCs the player is fighting, they shouldn't know this, just show the damage and life of the player if they are attacked\nWhen the player rolls a natural 20, enhance the player’s action description and conclude with \"Natural 20.\"\nDon't feel sorry for the player, he must take damage and he must feel that he has difficulty in combat, if he dies in any action the adventure will end.\nExample Format for Combat:\nPrompt: \"I draw my sword and swing toward the goblin, calling him to fight.\"\n\nResponse: “You taunt the goblin, who charges with his spear. Quick on your feet, you dodge the thrust and prepare to counter.”\nPrompt: \"I want to thrust at him.\"\n\nResponse: “With a swift response, you lunge, aiming at the goblin’s chest. The goblin narrowly evades, leaving only his ragged tunic torn from your blade.”\n\nFor each player attack, include health calculations only if damage is dealt. Format as:\n\n(Total HP before attack) - (Damage taken) = (Total HP after attack)\n\nREMEMBER\nYOU MUST to play NPCs in combat in the order of initiatives\n\nSetting Details:\nStarting Scenario\n\nThe player begins as a novice adventurer, seated alone at a table in the Rusty Axe Tavern.\nAn event will prompt them with a mission (e.g., a treasure hunt, a rescue request, or a brawl leading to a quest to save the city). If they decline, introduce a different event until they accept a mission.\nFixed Elements\n\nTavern Name: Rusty Axe Tavern\nTavern Description: A noisy, grimy place filled with adventurers. Its drink is a thick, magical liquid that’s rejuvenating and very sweet.\nNPCs:\nGrimbeard Pedra-firme: Gruff and blunt, this dwarven bartender serves drinks and oversees the chaos.\nBrunhilda \"Machado Duplo\" Stormblade: A tall, scarred woman with two axes strapped to her back. She’s gruff but has a soft spot for the player.\nSir Reginald \"O Polido\" Brightshield: A towering figure in spotless white-and-gold armor, usually alone, cleaning a massive sword.\nBaruk: A regular drunk sitting by the entrance, under a dilapidated sign reading “RUSTY AXE TAVERN” with the “T” missing and lying beside him.\n\nMagic Drink Effect\n\nThe tavern’s magical drink heals the player fully, restoring all stats as if from a long rest.\n\nAdditional Guidelines:\nCurrency Tracking\n\nDisplay the player’s remaining currency only when they spend or acquire coins. Format it as:\n\n(total coins before transaction) - (cost or amount gained)\n(new total of coins)\n\nMission Suitability\n\nTailor missions to the player’s beginner status within the guild. Ensure quests are appropriate to their level.\nFormatting\n\nFormat your narration for ease of reading. Use line breaks, bold headings, or other formatting to make interactions clear and enjoyable.\n\nStarting Instructions:\nWhen the adventure is about to begin, you will receive the player’s character sheet. Wait for the prompt \"Start Adventure\" before responding.\n\nEnd of Game:\nDo not end the game unless you receive the exact prompt, “END GAME.”",
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=self.config,
            system_instruction= self.system_instruction,
            )
        self.files = [
            Mestre.upload_to_gemini("NPCs machado enferujado.pdf", mime_type="application/pdf"),
        ]
        Mestre.wait_for_files_active(self.files)
        self.chat = self.model.start_chat(history=[
            {
                "role": "user",
                "parts": [
                    "Aqui esta os npcs presentes no Machado Enferrujado",
                    self.files[0],
                    "ficha do personagem do jogador\n\nNome do Personagem: Anya Stormborn\nClasse e Nível: Bárbaro 1\nRaça: Humana Variante\nAntecedente: Herói do Povo\nTendência: Caótica Boa\n\nHabilidades:\n\nForça: 16 (+3)\n\nDestreza: 13 (+1)\n\nConstituição: 14 (+2)\n\nInteligência: 10 (+0)\n\nSabedoria: 12 (+1)\n\nCarisma: 15 (+2) - Incomum para um bárbaro, reflete sua capacidade de inspirar outros.\n\nInspiração: (em branco)\nBônus de Proficiência: +2\nClasse de Armadura: 14 (10 + DES + escudo) - Anya começa com um escudo, mas pode optar por uma armadura mais pesada se adquiri-la.\nIniciativa: +1 (DES)\nDeslocamento: 9m\nPontos de Vida Atuais/Máximo: 14 (12 + CON) Anote 1d12 como dado de vida\nPontos de Vida Temporários: 0\nPontos de Experiência: 0\nDado de Vida: 1d12\nTestes de Resistência: Força +5 (PROF +3 FOR), Constituição +4 (PROF +2 CON)\nSabedoria (Percepção) Passiva: 11\n\nPerícias:\n\nAtletismo +5 (PROF +3 FOR)\n\nSobrevivência +3 (PROF +1 SAB)\n\nPercepção +3 (PROF +1 SAB)\n\nPersuasão +4 (PROF +2 CAR) - Perícia incomum para um bárbaro, demonstra sua capacidade de inspirar outros com palavras, além de sua força bruta.\n\nOutras Proficiências e Idiomas:\n\nIdiomas: Comum e um idioma à sua escolha. Vamos supor que ela tenha aprendido Gigante em suas viagens, o que dá a ela uma vantagem tática contra essas criaturas.\n\nProficiência em Ferramentas: Veículos (terrestres) - reflete sua habilidade de conduzir carroças e outros veículos, uma perícia valiosa em suas viagens.\n\nEquipamento:\n\nEspada Grande\n\n2 Azagaias\n\nPacote de Explorador\n\n(Página 2 da Ficha)\n\nIdade: 20\n\nAltura: 1,75m\n\nPeso: 70kg\n\nOlhos: Verdes esmeralda, intensos e penetrantes.\n\nPele: Bronzeada, com algumas sardas no rosto.\n\nCabelo: Ruivo flamejante, longo e selvagem, muitas vezes trançado com miçangas e penas.\n\nAliados e Organizações: Tribo do Falcão Ascendente (sua tribo natal), Círculo dos Protetores da Floresta (um grupo de druidas e patrulheiros que ela conheceu em suas andanças).\n\nAparência do Personagem: Anya é uma jovem impressionante, com um físico atlético e uma presença imponente. Suas roupas são feitas de couro e peles de animais, e ela usa um colar feito com dentes de lobo e garras de urso. Uma tatuagem espiral adorna seu braço esquerdo, representando a força da natureza selvagem que ela canaliza em suas fúrias.\n\nCaracterísticas e Traços: Anya é corajosa, impulsiva e ferozmente leal àqueles que ama. Ela tem um senso de justiça inabalável e não hesita em defender os fracos e oprimidos. Ela tem um temperamento explosivo e pode ser teimosa, mas também possui um grande coração e um senso de humor afiado. Ela ama a natureza e os animais, e se sente mais em casa nas florestas e montanhas do que nas cidades e vilas.\n\nIdeais: Liberdade. \"Ninguém tem o direito de controlar a vida de outro. Todos merecem ser livres.\" (Caótico)\n\nVínculos: \"Eu irei proteger minha tribo e honrar a memória daqueles que foram perdidos para as forças das trevas.\"\n\nDefeitos: \"Minha raiva pode me controlar. Às vezes, eu luto para diferenciar meus inimigos dos meus amigos.\"\n\nHistórico do Personagem: Anya cresceu na Tribo do Falcão Ascendente, um povo nômade que vivia nas florestas. Desde jovem, ela demonstrou uma afinidade incomum com a natureza e uma habilidade nata para o combate. Quando sua tribo foi atacada por um grupo de goblins saqueadores, Anya lutou bravamente para defender seu povo, inspirando outros com sua coragem e ferocidade. Após a batalha, ela foi aclamada como uma heroína e recebeu a bênção dos espíritos da floresta. Desde então, ela viaja pelo mundo como uma protetora do povo, combatendo o mal e defendendo os inocentes.\n\nTesouro: 10 po, um amuleto de madeira entalhado com a figura de um falcão, uma faca de caça, um kit de primeiros socorros.",
                ],
            },
        ]
        )
        self.chat = self.model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        "Aqui esta os npcs presentes no Machado Enferrujado",
                        self.files[0],
                        "ficha do personagem do jogador\n\nNome do Personagem: Anya Stormborn\nClasse e Nível: Bárbaro 1\nRaça: Humana Variante\nAntecedente: Herói do Povo\nTendência: Caótica Boa\n\nHabilidades:\n\nForça: 16 (+3)\n\nDestreza: 13 (+1)\n\nConstituição: 14 (+2)\n\nInteligência: 10 (+0)\n\nSabedoria: 12 (+1)\n\nCarisma: 15 (+2) - Incomum para um bárbaro, reflete sua capacidade de inspirar outros.\n\nInspiração: (em branco)\nBônus de Proficiência: +2\nClasse de Armadura: 14 (10 + DES + escudo) - Anya começa com um escudo, mas pode optar por uma armadura mais pesada se adquiri-la.\nIniciativa: +1 (DES)\nDeslocamento: 9m\nPontos de Vida Atuais/Máximo: 14 (12 + CON) Anote 1d12 como dado de vida\nPontos de Vida Temporários: 0\nPontos de Experiência: 0\nDado de Vida: 1d12\nTestes de Resistência: Força +5 (PROF +3 FOR), Constituição +4 (PROF +2 CON)\nSabedoria (Percepção) Passiva: 11\n\nPerícias:\n\nAtletismo +5 (PROF +3 FOR)\n\nSobrevivência +3 (PROF +1 SAB)\n\nPercepção +3 (PROF +1 SAB)\n\nPersuasão +4 (PROF +2 CAR) - Perícia incomum para um bárbaro, demonstra sua capacidade de inspirar outros com palavras, além de sua força bruta.\n\nOutras Proficiências e Idiomas:\n\nIdiomas: Comum e um idioma à sua escolha. Vamos supor que ela tenha aprendido Gigante em suas viagens, o que dá a ela uma vantagem tática contra essas criaturas.\n\nProficiência em Ferramentas: Veículos (terrestres) - reflete sua habilidade de conduzir carroças e outros veículos, uma perícia valiosa em suas viagens.\n\nEquipamento:\n\nEspada Grande\n\n2 Azagaias\n\nPacote de Explorador\n\n(Página 2 da Ficha)\n\nIdade: 20\n\nAltura: 1,75m\n\nPeso: 70kg\n\nOlhos: Verdes esmeralda, intensos e penetrantes.\n\nPele: Bronzeada, com algumas sardas no rosto.\n\nCabelo: Ruivo flamejante, longo e selvagem, muitas vezes trançado com miçangas e penas.\n\nAliados e Organizações: Tribo do Falcão Ascendente (sua tribo natal), Círculo dos Protetores da Floresta (um grupo de druidas e patrulheiros que ela conheceu em suas andanças).\n\nAparência do Personagem: Anya é uma jovem impressionante, com um físico atlético e uma presença imponente. Suas roupas são feitas de couro e peles de animais, e ela usa um colar feito com dentes de lobo e garras de urso. Uma tatuagem espiral adorna seu braço esquerdo, representando a força da natureza selvagem que ela canaliza em suas fúrias.\n\nCaracterísticas e Traços: Anya é corajosa, impulsiva e ferozmente leal àqueles que ama. Ela tem um senso de justiça inabalável e não hesita em defender os fracos e oprimidos. Ela tem um temperamento explosivo e pode ser teimosa, mas também possui um grande coração e um senso de humor afiado. Ela ama a natureza e os animais, e se sente mais em casa nas florestas e montanhas do que nas cidades e vilas.\n\nIdeais: Liberdade. \"Ninguém tem o direito de controlar a vida de outro. Todos merecem ser livres.\" (Caótico)\n\nVínculos: \"Eu irei proteger minha tribo e honrar a memória daqueles que foram perdidos para as forças das trevas.\"\n\nDefeitos: \"Minha raiva pode me controlar. Às vezes, eu luto para diferenciar meus inimigos dos meus amigos.\"\n\nHistórico do Personagem: Anya cresceu na Tribo do Falcão Ascendente, um povo nômade que vivia nas florestas. Desde jovem, ela demonstrou uma afinidade incomum com a natureza e uma habilidade nata para o combate. Quando sua tribo foi atacada por um grupo de goblins saqueadores, Anya lutou bravamente para defender seu povo, inspirando outros com sua coragem e ferocidade. Após a batalha, ela foi aclamada como uma heroína e recebeu a bênção dos espíritos da floresta. Desde então, ela viaja pelo mundo como uma protetora do povo, combatendo o mal e defendendo os inocentes.\n\nTesouro: 10 po, um amuleto de madeira entalhado com a figura de um falcão, uma faca de caça, um kit de primeiros socorros.",
                        "Agora uma treinamento para voce para situações de conversa e introdução da história",
                        "Eu quero entrar na taverna",
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "Voce adentra a taverna Machado Enferrujado e antes de conseguir ouvir qualquer pessoa, um cheiro desagradavel para te receber, um cheiro de suor com sangue e muita bebida. Em seguida voce ve diversas mesas redondas com varios aventureiros, voce ve magos, druidas, barbaros, cavaleiros, mas um aventureiro chama sua atenção, um cavaleiro com a armadura branca com detalher em ouro, completamente limpa. Ele esta sentado sozinho em uma mesa limpando sua espada que estramentente esta mais reluzente que o espelho que voce se ajeitou ao sair de casa. voce se direciona ao bar para pegar uma bebida e ao passar por ele nota que alem da armadura muito limpa, ele é absurdamente grande, ele deve ter entre 2,30m e 2,50m e perto dos 160kg. Voce chega ao balcao e um anão barrigudo usando um avental chega para te atender enquanto seca uma caneca de madeira que deveria estar mais limpa do que está",
                    ],
                },
                {
                    "role": "user",
                    "parts": [
                        "Senhor, me ve uma bebida. e arrasto 3 moedas de bronze na mesa",
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "Voce pede uma bebida e antes de voce terminar a frase ja tem uma caneca de um liquido viscoso escuro na sua frente, voce bebe e ele é extramente doce, muito saboroso, voce se sente rejuvenecido e sente que poderia enfrentar um exercicito de demonios agr mesmo, quase como se esse liquido tivesse magia nele. O Grimbeard Pedra-firme responde\n\n[Grimbeard Pedra-firme]: Eai aventureiro, novo por aqui? Voce pode pegar uma missao no painel de madeira ali no fundo, so tente nao morrer na missao de iniciante, é um jeito triste de morrer, se bem que acho que ninguem ligaria muito",
                    ],
                },
                {
                    "role": "user",
                    "parts": [
                        "Agora um treinando de cenas de combate",
                        "Eu tiro minha espada e balanço em direção ao goblin, o chamando para combate",
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "Voce chama o goblin para batalha que dispara correndo na sua direção e desfere um ataque com sua lança. Com um reflexo rapido, voce pula para o lado e escapa do ataque",
                    ],
                },
                {
                    "role": "user",
                    "parts": [
                        "Eu quero tentar dar uma estocada nele",
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "Voce dispara instantaneamente após o goblin tentar te acertar e, e tenta fincar sua espada no peito dele, mas o goblin, por resposta de ter errado o seu ataque, se move segundo antes da sua lamida passar raspando e cortar somente o trapo que esta vestindo\n\nEle tenta novamente estocar voce, e consegue acertar entre as placas da sua armadura, furando seu ombro profundamente. Voce sente o seu sangue escorrendo e uma dor absurda em sua ombro esquerdo. Doeu mas nao o sufciente para mata-lo\n16PV - 6\n14PV",
                    ],
                },
                {
                    "role": "user",
                    "parts": [
                        "Quero pular em acima da cabeça dele e com um giro frontal desferir um ataque em seu pescoço",
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "Não instante em que a lança toca seu peito voce pula acima do goblin, acima da cabeça dele voce faz um giro frontal e utilizando a força do giro voce acerta o pescoço do goblin cortando sua cabeça tao facilmente que voce passa direto e enterra sua espada no chao\n20 NATURAL",
                    ],
                },
                {
                    "role": "user",
                    "parts": [
                        "Agora um treinamento de combate com mais de um inimigo",
                        "Quero chamar os goblins com minha espada ",
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "O goblin 1 avança em sua direção cravando sua estaca em sua perna\n14PV - 5\n9PV",
                    ],
                },
                {
                    "role": "user",
                    "parts": [
                        "Quero agarrar a lança dele puxar ele e dar um soco na sua cara",
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "Voce tenta puxar a lança do goblin mas ele recua rapidamente \nvoltando para onde estava antes de te atacar. Ele fica olhando fixamente para sua bolsa de moedas\nO goblin 2 avança em sua direçao mirando seu peito",
                    ],
                },
                {
                    "role": "user",
                    "parts": [
                        "Quero esquivar para o lado, e cortar sua perna com um golpe limpo",
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "Voce esquiva cambaleando, o goblin arranha sua armadura antes de voce se mover para o lado dele e realizar um corte profundo em uma de suas pernas. Ele cai no chao, nao morto mas com muita dor\n\nO goblin 1 avaça novamente mas dessa vez com mais raiva no olhar, após ver seu amigo sendo machucado. ele esta mirando em seu pescoço e ele avança muito mais rapido do que da ultima vez",
                    ],
                },
                {
                    "role": "user",
                    "parts": [
                        "Eu quero usar minha espada para desviar a lança dele e com um ataque certeiro atraver seu peito",
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "Voce com um movimento limpo desvia a lança, que passa cortando a direita da sua cabeça cortando alguns fios de cabelo, e com sua espada atravessa o peito do gonlin 1 deixando morto no chao\n\nAgora o goblin 2 com suas ultimas chances se levanta e corre para a floresta devolta para sua vila\nO combata acabou\nO que voce quer fazer?",
                    ],
                },
                {
                    "role": "user",
                    "parts": [
                        "Certo agora com base nesses treinamentos vamos começar uma aventura",
                    ],
                },
            ]
        )

    
    def upload_to_gemini(path, mime_type=None):
        file = genai.upload_file(path, mime_type=mime_type)
        print(f"Uploaded file '{file.display_name}' as: {file.uri}")
        return file

    def wait_for_files_active(files):
        for name in (file.name for file in files):
            file = genai.get_file(name)
            while file.state.name == "PROCESSING":
                file = genai.get_file(name)
                if file.state.name != "ACTIVE":
                    raise Exception(f"File {file.name} failed to process")
        
    def mensagem(self, prompt):
        mensagem = self.chat.send_message(prompt) 
        return mensagem

'''class IAs:
    def __init__(self, config, modelo, inicio_chat):
        self.config = config
        self.model = modelo
        self.inicio_chat = inicio_chat



class Syntheris(IAs):
    def __init__(self, config, modelo, inicio_chat):
        super().__init__(config, modelo, inicio_chat)

    def mensagem(self, prompt):
        mensagem = self.inicio_chat.send_message(prompt) 
        return mensagem.text
    

class Naratheon(IAs):
    def __init__(self, config, modelo, inicio_chat):
        super().__init__(config, modelo, inicio_chat)

    def mensagem(self, prompt):
        mensagem = self.inicio_chat.send_message(prompt)
        return mensagem.text
 

class Veridex(IAs):
    def __init__(self, config, modelo, inicio_chat):
        super().__init__(config, modelo, inicio_chat)
        
    def mensagem(self, prompt):
        mensagem = self.inicio_chat.send_message(prompt)
        return mensagem.text

class Lorealis(IAs):
    def __init__(self, config, modelo, inicio_chat):
        super().__init__(config, modelo, inicio_chat)
        
    def mensagem(self, prompt):
        mensagem = self.inicio_chat.send_message(prompt)
        return mensagem.text

class Figuris(IAs):
    def __init__(self, config, modelo, inicio_chat):
        super().__init__(config, modelo, inicio_chat)
        
    def mensagem(self, prompt):
        mensagem = self.inicio_chat.send_message(prompt)
        return mensagem.text'''