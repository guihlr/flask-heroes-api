"""Hero search handler"""
from views import heroes
from flask_restful import Resource

from models.hero import Hero
from flask import request


class HeroSearchHandler(Resource):
    """Hero search handler"""

    def get(self):
        """Get hero"""
        try:
            heroes = Hero.search(request.args.get("name").title())
            heroes_dict = []

            for hero in heroes:
                heroes_dict.append(hero.to_dict())

            return heroes_dict

        except Exception as error:
            return {"message": "Bad request, param name is required"}, 400
