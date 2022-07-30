from flask import redirect, abort

@app.route("/shortener/<tiny_url>")
def url_shortener(tiny_url):
    try:
        url = banco_de_dados.select(shortened=tiny_url).url
    except AttributeError:
        # objeto NoneType não tem o atributo url, ou seja, não existe
        abort(404)
    except ConnectionError:
        # não conseguiu conectar no MySQL # TODO: Use o PostGres :)
        abort(503)  # ServiceUnavailable
    else:
        redirect(url)