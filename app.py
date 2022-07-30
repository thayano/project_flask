# importações
from flask import Flask

# instanciando a classe Flask.
app = Flask("flask")


# definindo rotas
# @app.route("/noticias")
@app.route("/<name>")
# @app.route("/noticias/<pais>/<estado>")
@app.route("/")
def index(name):
    if name.lower() == "bruno":
        return "Olá {}".format(name), 200
    else:
        return "Not Found", 404


# Roteamento explicito
# app.add_url_rule("/noticias/<pais>",
#             endpoint="lista_noticias",
#             view_func=lista_de_noticias)

# ativa modo debug e restart no servidor de desenvolvimento.
app.run(debug=True, use_reloader=True)