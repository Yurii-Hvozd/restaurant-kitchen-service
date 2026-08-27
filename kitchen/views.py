from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View, generic

from kitchen.models import Cook, Ingredient, Dish, DishType

@login_required
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


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 5


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type").prefetch_related("ingredients", "cooks")


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    paginate_by = 5
    context_object_name = 'dish_types'
    template_name = "kitchen/dish_types_list.html"


