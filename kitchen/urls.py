from django.urls import path

from kitchen import views
from kitchen.views import CookListView

urlpatterns = [
    path('', views.index, name='index'),
    path("cooks/", CookListView.as_view(), name="cook_list"),
]



















app_name = 'kitchen'