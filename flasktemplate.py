from flask import Flask

nombre = Flask(__name__)

@nombre.route("/")
def haz():
    return 'hola, has llegado a la pagina web de nicolita<br>\
<a href="/segunda">segunda</a><br><a href="tercera">tercera</a>'

@nombre.route("/segunda")
def haga():
    return 'felicitaciones por haber encontrado esta pagina <br>\
<a href="/">regresar</a>'

@nombre.route("/tercera")
def hazla():
    return 'esta es la ultima pagina -- no hay nada aqui<br>\
<a href="/">regresar</a>'

if __name__ == '__main__':
    nombre.run()

