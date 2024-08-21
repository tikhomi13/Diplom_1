from praktikum.database import Database


class TestDatabase:

    def test_list_of_buns(self):

        test_database = Database()

        assert test_database.buns[0].name == 'black bun'
        assert test_database.buns[0].price == 100

        assert test_database.buns[1].name == 'white bun'
        assert test_database.buns[1].price == 200

        assert test_database.buns[2].name == 'red bun'
        assert test_database.buns[2].price == 300

    def test_list_of_ingredients(self):

        test_database = Database()

        assert test_database.ingredients[0].name == 'hot sauce'
        assert test_database.ingredients[0].price == 100

        assert test_database.ingredients[1].name == 'sour cream'
        assert test_database.ingredients[1].price == 200

        assert test_database.ingredients[2].name == 'chili sauce'
        assert test_database.ingredients[2].price == 300

        assert test_database.ingredients[3].name == 'cutlet'
        assert test_database.ingredients[3].price == 100

        assert test_database.ingredients[4].name == 'dinosaur'
        assert test_database.ingredients[4].price == 200

        assert test_database.ingredients[5].name == 'sausage'
        assert test_database.ingredients[5].price == 300
