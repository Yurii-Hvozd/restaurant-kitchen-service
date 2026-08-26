from django.urls import path

from kitchen import views
from kitchen.views import CookListView, IngredientListView

urlpatterns = [
    path('', views.index, name='index'),
    path("cooks/", CookListView.as_view(), name="cook_list"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient_list"),
]



















app_name = 'kitchen'