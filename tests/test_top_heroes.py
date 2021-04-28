"""Top heroes test case"""
import unittest
from unittest.main import main
from flask_restful import Api

from mock import patch
from mockfirestore import MockFirestore

from main import app
from models.hero import Hero


class TestTopHeroesHandler(unittest.TestCase):
    """Top heroes handler"""

    def setUp(self):
        """setUp é chamado sempre no inicio de cada teste"""
        self.mock_db = MockFirestore()
        self.patcher = patch(
            "modules.main.MainModule.get_firestore_db", return_value=self.mock_db
        )
        self.patcher.start()
        # Nessa linha vamos iniciar nossa API nos testes
        self.app = app.test_client()

    def tearDown(self):
        """O tearDown é chamado no final de cada teste"""
        self.patcher.stop()
        self.mock_db.reset()

    @staticmethod
    def create_hero(hero_name, universe):
        hero = Hero()
        hero.name = hero_name
        hero.description = f"{hero_name} description"
        hero.universe = universe
        hero.save()
        return hero

    def test_get_heroes(self):
        """Test get top heroes"""
        for i in range(1, 21):
            self.create_hero(f"Hero {i} description", "marvel")

        # Fazendo a primera consulta na url e conferindo a resposta
        response = self.app.get(path="/top-heroes")
        first_hero_list = response.get_json()["heroes"]
        self.assertEqual(len(first_hero_list), 4)
        self.assertEqual(response.status_code, 200)

        # Fazendo a segunda consulta da url e conferindo a resposta
        response = self.app.get(path="/top-heroes")
        self.assertEqual(response.status_code, 200)
        second_hero_list = response.get_json()["heroes"]
        self.assertEqual(len(second_hero_list), 4)

        # Comparando as duas listas para ver se são diferentes
        # Pois essa url precisa sempre retonar herois diferentes
        self.assertNotEqual(first_hero_list, second_hero_list)


if __name__ == "__main__":
    unittest.main()
