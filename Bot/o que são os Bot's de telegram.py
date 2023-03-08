'''
 >> O QUE SÃO BOTS? <<
Os bots de telegram são aplicações que rodam dentro do telegram onde os usuários conseguem interagir através de mensagens
e comandos, e os devs conseguem por meio dessas entradas dos usuários controlar esses bots através de requisições à API
de bots do telegram.

 >> COMO CRIAR UM BOT? <<
 Para criarmos um bot será necessário interagir com um bot, o que é o pai de todos, o @BotFather. Para que iso seja possivel
 teremos que configurar nosso bot e logo após isso nos será fornecido um Token.

    ----->> IMPORTANTE <<-----
ESTE TOKEN DÁ TOTAL ACESSO AO BOT QUE CRIAREMOS, LOGO, DEVEMOS GUARDÁ-LO E NÃO FORNECÊ-LO A NINGUEM.
Outro dado importante é o "chat_id" para realização de requsts.

 >> O QUE CONSIGO FAZER COM UM BOT? <<
 - Criação de notificações customizadas e feed de notícias(o que é o caso desse projeto)
 - Interagir com outros serviços, como GmailBot, GifBot, YoutTubeBot, GitHubBot entre outros, existe uma gama de outros
 bots que podemos interagir para buscar dados.
 - Aceitar pagamentos de usários do Telegram, mostrar produtos em uma vitrine e os usuários comprarem e fazer o pagamento
 pelo bot.
 - Criar ferramentas customizadas (alertas, previsões do tempo, traduções etc.)
 - Construir jogos single e multiplayer(@gameee)
 - Integração de ferramentas de Webscraping.
 - Monitorar notícias sobre determinadas empresas
 - Integração com API do Twitter para monitiração de assuntos, hashtags e monitoração de sentimento
 - Integração com sistemas para rastreamento de dados(Correios, Sistemas Judiciários, Diário Oficial, etc.)

 É possivel fazer integração com sensores de arduino/raspberryPy por exemplo, para monitoração de dados.
 Um exemplo é a interação utilizando arduino para monitorar a umidade das plantas com utilização de sensores, conectanto
 um bot do telegram com o arduino.

 >> APIs e Protocolo HTTP <<
 --> API:
    - A sigla vem de Aplication Programing Interface(Interface de Programação de Aplicações).
    - Serve para facilitar a integração entre diferentes sistemas.
    - API's são criadas quando a empresa desenvolvedora de um sistema quer disponibilizar uma maneira para que outros
    desenvolvedores possam acoplar/plugar/estender/conectar/integrar outros sistemas.
    - Existem diversos tipos de APIs: de Sistemas Operacionais, se Sistemas Embarcados, de Microcontroladores, e as mais
    famosas: as API's Web.
    - As APIs Web utilizam um dos principais protocolos da internet: o Protocolo HTTP

--> Protocolo HTTP:
É o protocolo de troca de dados dainternet.
    - HTTP vem de Hypertext Transfer Protocol(Protocolo de transferência de Hipertexto)
    - É um protocolo que especifica como será a comunicação entre um navegador(Cliente) e um servidor web(Servidor)
A Internet foi construida em cima de uma estrutura Cliente <-> Servidor:
-> Cliente é a parte que faz as requisições, por meio de um navegador(por exemblo)
-> Servidor é a parte que processa as requizições feitas por esses clientes, fornecendo "respostas".

 >> Requisição HTTP
  As requisições tem uma "especificação", uma estrutura que contém:

  MÉTODO / URL / VERSÃO HTTP
          HEADERS
      (Cabeçalho HTTP)
           BODY
    (Corpo da Requisição)

Ao acessar um site pelo browser(exemplo real) acontece o seguinte:

  GET / /blog / HTTP/1.1
  Host: pythonacademy.com.br
  Acept: */*
  Connection: keep-alive

 >> Resposta HTTP
  As respostas tem uma "especificação", uma estrutura que contém:

  VERSÃO HTTP / CÓDIGO DA RESPOSTA
           HEADERS
       (Cabeçalho HTTP)
            BODY
     (Corpo da Requisição)

Ao acessar um site pelo browser(exemplo real) acontece o seguinte:

  HTTP/1.1   /   200 OK
  Date: Sat, 12 Feb 2022 04:03:19 GMT
  Content-Type: text/html; charset=utf-8
  Last-Modified: Thu, 10 Feb 2022 14:30:19 GMT

  <DOCTYPE html>
  <html lang="pt-BR">
    <head>
    .
    .
    .

 >> Requisição HTTP: URL
 Os recursos nesse protocolo são localizados através de uma URL(Uniform Resourse Locutor)

 Por exemplo: http://pythonacademy.com.br/blog/funcoes-no-python/
 - Schema: http
 - Host: pythonacademy.com.br(DNS -> 172.67.223.111)
 - Path: /blog/funcoes-no-python/

* Schema é a parte da estrutura que vai dizer qual será a forma de troca de dados, aqui o protocolo http.
* Host(do inglês: hospedeiro) é onde estão hospedadas dados, aqui é necessário tradução e quem faz isso é um serviço
chamado DNS(Domain Name System - Sistema de Nomes de Domínio) através de um Endereço de IP(Internet Protocol) que a grosso
modo é o CEP do servidor da pyuthon academy, o IP é um endereço exclusivo que identifica um dispositivo na internet ou
em uma rede local.
* Path diz ao servidor o que o cliente está querendo acessar.

Além disso, pode-se adicionar outros campos à URL através das Query Strings
Exemplo:http:kabum.com.br/busca?query=rtx+3090&page_number=1
* ? masrca o início das Query Strings
* & separa Query Strings
* Seu formato é nome=valor
Uma Query String é um pedido de uma informação ou de um dado.

 >> Métodos HTTP
 - Métodos diferenciam as operações no protocolo HTTP:
    - Para busca de dados, utilizamos o método GET
    - Para envio de dados, utilizamos o método POST
    - Para deleção de dados, utilizamos o método DELETE
    - Para utilização de dados utilizamos o método PUT
    - Para utilização parcial de dados utilizamos o método PATCH
Existem outros métodos, oprém, estes são os mais importantes para integração de sistemas web.

A junção do Protocolo HTTP com o conceito de integração de sistemas via APIs é chamado de APIs REST
 ** Protocolo HTTP + API = APIs REST **

Existem outras formas de integração na web, mas os mais utilizados são APIs REST.

 >> APIs REST <<
 - REST vem de REpresentation State Transfer(Transferência de Estado Representacional) e foi um conceito introduzido em
 2000 pelo Cientista da Computação Norte-Americano Roy Fielding em sua Tese de Doutorado
 - É um estilo arquitetural de software que define um conjunto de restrições a serem usadas para a criação de serviços
 Web(Web Services), são regras para o desenvolvedor do que ele deve e não fazer quando está dispondo um serviço na internet.
 - Estado Representasional pode ser traduzido como a "forma que representamos os dados". Atualmente, a forma mais utilizada
 é a JavaScript Object Notation, ou JSON.

  >> Operações CRUD <<
 - O padrão REST define as melhores práticas para que um Web Service suporte as famosas Operações CRUD
 - CRUD
    * Create: Criação de recursos ................... HTTP POST
    * Retrieve: Busca de recursos ................... HTTP GET
    * Update: Atualização de recursos ............... HTTP PUT
    * Delete: Deleção de recursos ................... HTTP DELETE

  >> CÓDIGOS DE STATUS <<
  O Protocolo HTTP possui codigos de resposta muito úteis que auxiliam na interpretação da resposta do servidor:
    * Resposta de informação(100-199)
    * Resposta de sucesso (200-299)
    * Redirecionamento (300-399)
    * Erros de cliente (400-499)
    * Erros do servidor (500-599)
Por ser uma lista mito extensa existem alguns códigos mais conhecidos:
    * 200 ok - código de sucesso
    * 201 CREATED - código de resposta de quando utilizamos um POST e a requisição foi criada
    * 400 BAD REQUEST - quando o cliente formulou uma requisição mal formatada
    * 401 UNAUTHORIZED - quando o cliente não tem autorização para acessar determinado recurso
    * 403 FORBIDDEN - cliente tem autorização mas não tem autorização para manipular determinado recurso
    * 404 NOT FOUND - quando o cliente está tentando acessar um endpoint inexistente naquele servidor
    * 500 INTERNAL SERVER ERROR - informa ao cliente que algum erro ocorreu do lado do servidor


 '''


