from django.urls import path

from kitchen import views
from kitchen.views import (
    CookListView,
    IngredientListView,
    DishListView,
    DishTypeListView,
    CookDetailView,
    DishDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
)

urlpatterns = [
    path("", views.index, name="index"),
    path("cooks/", CookListView.as_view(), name="cook_list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook_detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook_create"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook_update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook_delete"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient_list"),
    path(
        "ingredients/create/", IngredientCreateView.as_view(), name="ingredient_create"
    ),
    path(
        "ingredients/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient_update",
    ),
    path(
        "ingredients/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredient_delete",
    ),
    path("dishes/", DishListView.as_view(), name="dish_list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish_detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish_create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish_update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish_delete"),
    path("dish-types/", DishTypeListView.as_view(), name="dish_types_list"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish_types_create"),
    path(
        "dish-types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish_types_update",
    ),
    path(
        "dish-types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish_types_delete",
    ),
]


app_name = "kitchen"
