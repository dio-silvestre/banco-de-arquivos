# Banco de Arquivos

Suporta diferentes tipos de arquivos (como imagens, músicas e vídeos) e permite fazer upload e download desses arquivos.
Tamanho máximo suportado: 50MB, podendo ser alterado conforme necessidade.

<br>

## Como instalar e rodar? 🚀

Para instalar o sistema, é necessário seguir alguns passos, como baixar o projeto e fazer instalação das dependências. Para isso, é necessário abrir uma aba do terminal e digitar o seguinte:

    #Este passo é para baixar o projeto
    git clone https://github.com/dio-silvestre/banco-de-arquivos.git

Depois que terminar de baixar, é necessário entrar na pasta, criar um ambiente virtual e entrar nele:

    #Entrar na pasta
    cd banco-de-imagens

    #Criar um ambiente virtual
    python -m venv venv --upgrade-deps

    #Entrar no ambiente virtual
    source venv/bin/activate

Então, para instalar as dependências, basta:

    pip install -r requirements.txt

Para rodar, basta digitar o seguinte, no terminal:

    flask run

E o sistema estará rodando em `http://127.0.0.1:5000/`

## Utilização 🖥️

Para utilizar este sistema, é necessário utilizar um API Client, como o [Insomnia](https://insomnia.rest/download)

### Rotas

### ![POST](https://i.imgur.com/Qhk9miC.png) UPLOAD FILE

```
/upload
```

Esta rota será enviado um arquivo por um Multipart Form nomeado "file", com o valor sendo o arquivo a ser enviado;

`RESPONSE STATUS -> HTTP 201 (created)`


#### ![GET](https://i.imgur.com/zH6h6cZ.png) FILES LIST

```
/files
```

Esta rota lista todos os arquivos.

`RESPONSE STATUS -> HTTP 200 (ok)`


#### ![GET](https://i.imgur.com/zH6h6cZ.png) FILES BY EXTENSION

```
/files/<extension>
```

Esta rota lista os arquivos de um determinado tipo;

`RESPONSE STATUS -> HTTP 200 (ok)`


#### ![GET](https://i.imgur.com/zH6h6cZ.png) DOWNLOAD BY FILE NAME

```
/download/<file_name>
```

Esta rota é responsável por fazer o download do arquivo solicitado em file_name;

`RESPONSE STATUS -> HTTP 200 (ok)`



## Tecnologias utilizadas 📱

- Flask, MongoDB

## Licence

MIT
