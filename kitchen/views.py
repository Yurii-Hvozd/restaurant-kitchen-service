from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View, generic

from kitchen.models import Cook, Ingredient, Dish, DishType


# Create your views here.
def index(request):
    num_cooks = Cook.objects.all().count()
    num_ingredients = Ingredient.objects.all().count()
    num_dishes = Dish.objects.all().count()
    num_dish_types = DishType.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_cooks': num_cooks,
        'num_ingredients': num_ingredients,
        'num_dishes': num_dishes,
        'num_dish_types': num_dish_types,
        'num_visits': num_visits + 1,
    }

    return render(request, 'kitchen/index.html', context=context)


class CookListView(generic.ListView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy('kitchen:cook_list')
    paginate_by = 5


class IngredientListView(generic.ListView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient_list")
    paginate_by = 5