from django.test import TestCase
from django.urls import reverse

from kitchen.models import Cook, Dish, DishType, Ingredient


class ModelTests(TestCase):

    def setUp(self):
        self.cook = Cook.objects.create_user(
            username="john",
            password="test1234",
            first_name="John",
            last_name="Doe",
            years_of_experience=5,
        )

        self.dish_type = DishType.objects.create(
            name="Soup"
        )

        self.ingredient = Ingredient.objects.create(
            name="Potato"
        )

        self.dish = Dish.objects.create(
            name="Potato Soup",
            description="Tasty soup",
            price=10.50,
            dish_type=self.dish_type,
        )

        self.dish.cooks.add(self.cook)
        self.dish.ingredients.add(self.ingredient)

    def test_cook_str(self):
        self.assertEqual(
            str(self.cook),
            "John Doe (john)"
        )

    def test_dish_type_str(self):
        self.assertEqual(
            str(self.dish_type),
            "Soup"
        )

    def test_ingredient_str(self):
        self.assertEqual(
            str(self.ingredient),
            "Potato"
        )

    def test_dish_str(self):
        self.assertEqual(
            str(self.dish),
            "Potato Soup (10.5$)"
        )

    def test_dish_type_relation(self):
        self.assertEqual(
            self.dish.dish_type,
            self.dish_type
        )

    def test_dish_cooks_relation(self):
        self.assertIn(
            self.cook,
            self.dish.cooks.all()
        )

    def test_dish_ingredients_relation(self):
        self.assertIn(
            self.ingredient,
            self.dish.ingredients.all()
        )


class ViewTests(TestCase):

    def setUp(self):
        self.user = Cook.objects.create_user(
            username="john",
            password="test1234",
        )

        self.dish_type = DishType.objects.create(
            name="Soup"
        )

        self.ingredient = Ingredient.objects.create(
            name="Potato"
        )

        self.dish = Dish.objects.create(
            name="Potato Soup",
            description="Tasty soup",
            price=10.50,
            dish_type=self.dish_type,
        )

    def test_login_required(self):
        response = self.client.get(
            reverse("kitchen:cook_list")
        )

        self.assertEqual(response.status_code, 302)

    def test_cook_list_view(self):
        self.client.login(
            username="john",
            password="test1234"
        )

        response = self.client.get(
            reverse("kitchen:cook_list")
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "john")

    def test_cook_detail_view(self):
        self.client.login(
            username="john",
            password="test1234"
        )

        response = self.client.get(
            reverse(
                "kitchen:cook_detail",
                args=[self.user.id]
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "john")

    def test_dish_list_view(self):
        self.client.login(
            username="john",
            password="test1234"
        )

        response = self.client.get(
            reverse("kitchen:dish_list")
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Potato Soup")

    def test_dish_detail_view(self):
        self.client.login(
            username="john",
            password="test1234"
        )

        response = self.client.get(
            reverse(
                "kitchen:dish_detail",
                args=[self.dish.id]
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Potato Soup")

    def test_dish_search(self):
        self.client.login(
            username="john",
            password="test1234"
        )

        response = self.client.get(
            reverse("kitchen:dish_list"),
            {"name": "Potato"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Potato Soup")
