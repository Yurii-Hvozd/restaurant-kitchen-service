from django.urls import path

from kitchen import views
from kitchen.views import CookListView, IngredientListView, DishListView, DishTypeListView, CookDetailView, \
    DishDetailView, CookCreateView, CookUpdateView, CookDeleteView

urlpatterns = [
    path('', views.index, name='index'),



    path("cooks/", CookListView.as_view(), name="cook_list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook_detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook_create"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook_update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook_delete"),





    path("ingredients/", IngredientListView.as_view(), name="ingredient_list"),


    path("dishes/", DishListView.as_view(), name="dish_list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish_detail"),


    path("dish-types/", DishTypeListView.as_view(), name="dish_types_list"),
]



















app_name = 'kitchen'