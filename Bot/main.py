import locale
from datetime import datetime
from time import sleep
from classes import CoinGeckoAPI, TelegramBot

'''
Descobrindo o chat_id:
 ANTES DE ESCREVER TODO O CÓDIGO abra a conversa com o bot criado e mande uma mensagem(qualquer mensagem, pode ser um oi,) 
 para que seja possível fazer a busca do id do chat. em seguida execute o seguinte código no debugger:

        import telegram
        bot = telegram.Bot(token='TOKEN_DO_SEU_BOT')
        atualizacoes = bot.get_updates()
        pass(inclua um breakpoint)
        
Feito isso no debugger percorra:
    atualizações > 0={update} > effective_message > chat_id
'''

id_moeda = input('ID da moeda a ser rastreada: ')
valor_minimo = int(input('Qual o valor mínimo para iniciar rastramento: '))
valor_maximo = int(input('Qual o valor máximo para iniciar rastramento: '))
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

api = CoinGeckoAPI(url_base='https://api.coingecko.com/api/v3')
bot = TelegramBot(token='TOKEN_DO_SEU_BOT', chat_id=201665409)

while True:
    if api.ping():# Verifica se API está online
        print('API online!')
        preco, atualizado_em = api.consulta_preco(id_moeda=id_moeda)
        print('Consulta realizada com sucesso!')
        data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')# trasnforma um inteiro em data do python
        mensagem = None

        if preco < valor_minimo:# Verifica se a mensagem será enviada ao usuário
            mensagem = f'*Cotação do Ethereum*\n\t*Preço:* R${preco}' \
                       f'\n\t*Horário*: {data_hora}\n\t*Motivo:* Valor menor que o mínimo'
        elif preco > valor_maximo:
            mensagem = f'*Cotação do Ethereum*\n\t*Preço:* R${preco}' \
                       f'\n\t*Horário*: {data_hora}\n\t*Motivo:* Valor maior que o máximo'

        if mensagem:
            bot.envia_mensagem(texto_markdown=mensagem)

    else:
        print(f'API offline.\nTente novamente mais tarde')
    sleep(10)
