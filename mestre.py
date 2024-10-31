import google.generativeai as genai

GOOGLE_GEMINI__API_KEY = "AIzaSyCY3DXvAe0c05nhu-_7__uP4VM5TMZ8014"

genai.configure(api_key=GOOGLE_GEMINI__API_KEY)

config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=config
    )

itens = ['espada curta', 'escudo de madeira']
missao = 'Matar o ork na floresta de pinheiros'

chat = model.start_chat(history=[
    {
        "role": "user",
        "parts": [
            "Você deve agir como um mestre do rpg Dungeons and Dragons em um jogo de aventura épica. Sua tarefa é escrever a história do jogador com base nas ações dele, deve manter o tom épico mas suas respostas devem ser curtas mas devem descrever fielmente as ações do jogador e serem épicas"
        ]
    },
    {
        "role": "user",
        "parts": [
            "Contexto: O jogador começa dentro do bar da guilda de aventureiros, um homem com roupa de carteiro chega ao bar e fala que 3 novas missões 1 iniciante, 1 avançada e 1 desafiadora chegaram: invente as missões mas elas devem conter, um titulo épico, nível de dificuldade, descrição e recompensa"
        ]
    },
    {
        "role": "user",
        "parts": [
            "Escreva a história contando sobre o contexto citado anteriormente"
        ]
    },
])
prompt = 'Escreva a história contando sobre o contexto citado anteriormente'
resposta = chat.send_message(prompt)
print(resposta.text)
prompt = input('Descreva sua ação: ')

while prompt != 'fim':
    resposta = chat.send_message(prompt)
    print(resposta.text)
    prompt = input('Descreva sua ação: ')

'''
Antes das ações do jogador voce vai ver se ele conseguiu ou nao, voce deve ser criativo para contar a história das ações do jogador para se adequar para se deu certo ou não.'''

'''prompt_anterior = f'Um jogador está controlando um personagem que contem os itens {itens}, e está realizando a missao {missao}. Ao chegar na floresta o ele deu de cara com o ork que aparentemente nao o viu, escreva a continuação dessa historia com base nas proximas linhas:'''