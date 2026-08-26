from django.urls import path

from kitchen import views
from kitchen.views import CookListView, IngredientListView, DishListView, DishTypeListView

urlpatterns = [
    path('', views.index, name='index'),
    path("cooks/", CookListView.as_view(), name="cook_list"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient_list"),
    path("dishes/", DishListView.as_view(), name="dish_list"),
    path("dish-types/", DishTypeListView.as_view(), name="dish_types_list"),
]



















app_name = 'kitchen'