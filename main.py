"""Arquivo main da API"""
from views.heroes_search import HeroSearchHandler
from views.top_heroes import TopHeroesHandler
from views.heroes import HeroHandler, HeroesHandler
from flask import Flask
from flask_restful import Resource, Api
from flask import request
from flask_cors import CORS
import firebase_admin
from firebase_admin import firestore


# Aqui iniciamos a API
app = Flask(__name__)
CORS(app)
API = Api(app)


@app.before_request
def start_request():
    """Start api request"""
    if request.method == "OPTIONS":
        return "", 200
    if not request.endpoint:
        return "Sorry, Nothing at this URL.", 404


# Nossa classe principal
class Index(Resource):
    """class return API index"""

    def get(self):
        """return API"""
        return {"API": "Heroes"}


# Nossa primeira url
API.add_resource(Index, "/", endpoint="index")
API.add_resource(HeroesHandler, "/heroes", endpoint="heroes")
API.add_resource(HeroHandler, "/hero/<hero_id>", endpoint="hero")
API.add_resource(TopHeroesHandler, "/top-heroes", endpoint="top-heroes")
API.add_resource(HeroSearchHandler, "/search", endpoint="search")


# Iniciando o firebase com as credenciais que você salvou na raiz da aplicação no passo 3.1
# Não se esqueça de colocar o nome do arquivo que você salvou, no meu caso esta com o nome de "tour-of-heroes-firebase-adminsdk-gds0n-14ebf97e39.json"

cred = firebase_admin.credentials.Certificate(
    "./angular-tour-of-heroes-5e483-firebase-adminsdk-esd2q-7a3b83d644.json"
)

firebase_admin.initialize_app(credential=cred)


if __name__ == "__main__":
    # Isso é utilizado somente para executar a aplicação local. Quando
    # realizarmos o deploy para o Google App Engine, o webserver deles ira
    # iniciar a aplicação de outra forma
    app.run(host="127.0.0.1", port=8080, debug=True)
# [END gae_python37_app]
