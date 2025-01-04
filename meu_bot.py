import discord
import os




    


intents = discord.Intents.default()
intents.message_content = True  # Ativa eventos de mensagens

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        response = None
        
        saudacoes = ['Olá','ola','Oi','oi','Hello','Eai','opa']    

        # Dicionário de comandos e respostas
        responses = {
            'PEberkas':(





            ),

            '!PE':(
               '**Pedras Épicas** são adquiridas através de eventos, caixas, em lojas do jogo e por meio do sistema de crafting.\n'
               'As pedras podem ser aprimoradas e evoluídas (+0 ~ +18) para ganhar propriedades ainda melhores mas **CUIDADO: Após o nível +9 a pedra pode quebrar!** .\n\n'
               'Use pergaminhos de proteção para evitar que a pedra quebre.\n\n'
            ),

            '!PEvoid': (
               '**EFEITOS RECOMENDADOS PARA EQUIPAMENTO DO VOID**:\n '
               '\n'
               '**Elmo**: Efeito da pedra: **600 de Ataque**.\n'
               '**Armadura**: Efeito da pedra: **800 de Ataque Especial**.\n'
               '**Calça**: Efeito da pedra: **10% MP recuperado**.\n'
               '**Luvas**: Efeito da pedra: **Ataque do pet 10%**.\n'
               '**Botas**: Efeito da pedra: **800 de Ataque especial**.\n'
               '**Capa**: Efeito da pedra:  **600 de Ataque**.\n'

            ),
            '!comandos': (
                'Esta é a lista de comandos: \n'
                '**!PE: O que são as pedras épicas**\n'
                '**!PEvoid**: Guia sobre pedras épicas do conjunto Void\n'
                '!**PEberkas**: Guia sobre pedras épicas do conjunto Berkas\n'
                '!**comandos**: Mostra os comandos\n'
                '**!Cartas**: Guia sobre cartas para equipamentos\n'
                '**!CLV**: Guia sobre Chase Level\n'
            ),
        }
        
        
        print(f'Message from {message.author}: {message.content}')

        if message.content in responses:
            response = responses[message.content]

        # Verifica se a mensagem contém uma saudação.
        #  saudacao.lower(): Converte cada saudação definida na lista (saudacoes) para letras minúsculas.
        elif any(saudacao.lower() == message.content.lower() for saudacao in saudacoes):
            response = ('Olá, Chaser! Eu sou a Comandante Lothus e estou aqui para te guiar, no que posso te ajudar? Esta é a lista de comandos:\n '
           ' **!PEvoid**: Guia sobre pedras épicas do conjunto void\n '
            '**!comandos**: Mostra os comandos\n '
            '**!Cartas**: Guia sobre cartas\n '
            '**!CLV**: Guia sobre Chase Level ')
     

        # Verifica se há uma resposta correspondente

        if response:
            await message.channel.send(f'{message.author.mention}, {response}')
        else:
            await message.channel.send(
         
                "Desculpe, não entendi. Digite !comandos para ver a lista de comandos válidos"
            )

        
      

TOKEN = 'seu token aqui'



client = MyClient(intents=intents)
client.run(TOKEN)

