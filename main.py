from flask import Flask, url_for, render_template
from configuration import configure_all


# Inicialização
app = Flask(__name__)


"""
    debug=True // Significa que estamos no modo desenvolvedor
    ou seja, quando modificarmos arquivos e salvar ele vai recarregar o servidor web.
"""

configure_all(app)


app.run(debug=True)


