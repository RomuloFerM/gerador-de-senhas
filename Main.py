from flask import Flask, jsonify
from random import randint, choice, shuffle
from string import ascii_letters

app = Flask(__name__)


# funcionalidades
@app.route('/')
def homepage():
    return 'Está é a página inicial do gerador de senhas, aqui as senhas são geradas a patir de letras, números e simbolos.<br>\
          <br> Para gerar senhas de 32 caracteres, adicione na URL "/gerarsenha".<br>\
          Você também pode usar "/gerarsenhajson" para receber a senha em json.<br>\
          <br> Usando "/gerarsenha/numero" (sendo o numero um valor qualquer entre 0 e 1000), você pode escolher o tamanho da senha.<br>\
          Exemplos:<br>\
          "/gerarsenha/8" para gerar senhas de 8 caracteres<br>\
          "/gerarsenha/50" para gerar uma senha de 50 caracteres<br>\
          <br>Você também pode usar o "/gerarsenhajson/numero", semelhante ao exemplo acima, para gerar a senha do tamanho que deseja e receber em json.'


@app.route('/gerarsenha/', methods=['GET'])
def gerar_senha(tamanho=32):
    if tamanho < 0 or tamanho > 1000:
        return 'por favor, informar um número entre 0 e 1000.'
    simbolos = '?@#$%&*()_-+=!'

    quantidadeLetras = randint(int(tamanho / 3), int(tamanho / 2))
    quantidadeNumeros = randint(int((tamanho - quantidadeLetras) / 3), int((tamanho - quantidadeLetras) / 2))
    quantidadeSimbolos = tamanho - quantidadeNumeros - quantidadeLetras

    senha = ''

    for i in range(0, quantidadeLetras):
        letra = choice(ascii_letters)
        senha += str(letra)

    for i in range(0, quantidadeNumeros):
        numero = randint(0, 9)
        senha += str(numero)

    for i in range(0, quantidadeSimbolos):
        simbolo = choice(simbolos)
        senha += str(simbolo)

    listaSenha = list(senha)
    shuffle(listaSenha)
    senha = ''
    for caracter in listaSenha:
        senha += caracter
    return senha


@app.route('/gerarsenha/<int:tamanho>', methods=['GET'])
def gerar_senha_tamanho(tamanho):
    return gerar_senha(tamanho)


@app.route('/gerarsenhajson', methods=['GET'])
def gerar_senha_json():
    return jsonify(gerar_senha())


@app.route('/gerarsenhajson/<int:tamanho>', methods=['GET'])
def gerar_senha_json_tamanho(tamanho):
    return jsonify(gerar_senha(tamanho))


# rodar a api
app.run(host='localhost')

