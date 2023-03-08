import requests
import telegram

class CoinGeckoAPI:
    def __init__(self, url_base: str):
        self.url_base = url_base

    def ping(self) -> bool:#Método de verificação se a API está online
        print('Verificando se API online...')
        url = f'{self.url_base}/ping'
        return requests.get(url).status_code == 200#Código 200 garante que a API está ok

    def consulta_preco(self, id_moeda: str) -> tuple:
        print(f'Consultando preço da moeda de id: {id_moeda}...')
        url = f'{self.url_base}/simple/price?ids={id_moeda}&vs_currencies=BRL&include_last_updated_at=true'
        resposta = requests.get(url)
        if resposta.status_code == 200:#Verifica se o código obteve sucesso
            dados_moeda = resposta.json().get(id_moeda, None)
            preco = dados_moeda.get('brl', None)
            atualizado_em = dados_moeda.get('last_updated_at', None)
            return preco, atualizado_em
        else:
            raise ValueError('Código de resposta diferete de HTTP 200 ok')


class TelegramBot:
    def __init__(self, token: str, chat_id: int):
        self.bot = telegram.Bot(token=token)
        self.chat_id = chat_id

    def envia_mensagem(self, texto_markdown: str):
        self.bot.send_message(
            text=texto_markdown,
            chat_id=self.chat_id,
            parse_mode=telegram.ParseMode.MARKDOWN)
        print('Mensagem enviada com sucesso!')
