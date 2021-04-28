"""Hero module"""
import urllib
from models.hero import Hero
from urllib.parse import urlparse


class HeroModule(object):
    """Hero module"""

    @staticmethod
    def create(params):
        """
        Create a new hero
        :param dict: Request dict params
        # return Hero: Hero created
        """
        hero = Hero()
        hero.name = params["name"]
        hero.description = params["description"]
        hero.imageUrl = params["imageUrl"]
        hero.universe = params["universe"]
        HeroModule.format_hero_params(hero)
        HeroModule.valid_hero_params(hero)
        hero.save()
        return hero

    @staticmethod
    def update(hero, params):
        """Update hero"""
        hero.name = params["name"]
        hero.description = params["description"]
        hero.imageUrl = params["imageUrl"]
        hero.universe = params["universe"]
        HeroModule.format_hero_params(hero)
        HeroModule.valid_hero_params(hero)
        hero.save()

    @staticmethod
    def valid_hero_params(hero):
        """Valid hero params"""
        if not hero.name:
            raise Exception("Bad request, name is required")

        if hero.universe != "dc" != "marvel":
            raise Exception("Bad request, invalid universe")
            # print(
            #     hero.universe,
            #     "<=<<=<<=<<=<<=<<=<<=<<=<<=<<=<<=<<=<<=<<=<<=<<=<<=<<=<<=<<=<<=<<=<<=<<=<<=<",
            # )

        # reg = "(https?://)?([\\da-z.-]+)\\.([a-z.]{2,6})[/\\w .-]*/?"

        if not urlparse(hero.imageUrl):
            raise Exception("Bad request, invalid url")

    @staticmethod
    def format_hero_params(hero):
        """Format hero params"""
        hero.name = hero.name.title().strip()
        hero.description = hero.description.title().strip()
