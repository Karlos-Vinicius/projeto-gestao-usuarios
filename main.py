from flask import Flask, url_for, render_template
from routes.home import home_route
from routes.cliente import cliente_route


# Inicialização
app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix="/clientes")

"""
    debug=True // Significa que estamos no modo desenvolvedor
    ou seja, quando modificarmos arquivos e salvar ele vai recarregar o servidor web.
"""



app.run(debug=True)


