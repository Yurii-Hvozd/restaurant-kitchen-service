from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q, QuerySet
from typing import Any, Dict

from kitchen.forms import (
    CookCreationForm,
    DishForm,
    CookSearchForm,
    DishSearchForm,
    IngredientSearchForm,
    DishTypeSearchForm,
)
from kitchen.models import Cook, Ingredient, Dish, DishType
from django.http import HttpRequest, HttpResponse


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_cooks = Cook.objects.all().count()
    num_ingredients = Ingredient.objects.all().count()
    num_dishes = Dish.objects.all().count()
    num_dish_types = DishType.objects.all().count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_ingredients": num_ingredients,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/index.html", context=context)


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()

        query = self.request.GET.get("search")

        if query:
            words = query.split()
            for word in words:
                queryset = queryset.filter(
                    Q(first_name__icontains=word) |
                    Q(last_name__icontains=word)
                )
        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict:
        context = super().get_context_data(**kwargs)
        context["search_form"] = CookSearchForm(self.request.GET)
        return context


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook_list")
    template_name = "kitchen/cook_form.html"
    form_class = CookCreationForm


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    fields = ("first_name", "last_name", "email", "years_of_experience")
    success_url = reverse_lazy("kitchen:cook_list")
    template_name = "kitchen/cook_form.html"


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook_list")
    template_name = "kitchen/cook_confirm_delete.html"


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 5

    def get_context_data(self, **kwargs: Any) -> Dict:
        context = super(IngredientListView, self).get_context_data(**kwargs)

        context["search_form"] = IngredientSearchForm(self.request.GET)
        return context

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient_list")
    template_name = "kitchen/ingredient_form.html"


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient_list")
    template_name = "kitchen/ingredient_form.html"


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen:ingredient_list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5

    def get_context_data(self, **kwargs: Any) -> Dict:
        context = super(DishListView, self).get_context_data(**kwargs)

        context["search_form"] = DishSearchForm(self.request.GET)
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Dish.objects.select_related("dish_type")
        name = self.request.GET.get("name")
        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type").prefetch_related(
        "ingredients", "cooks"
    )


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish_list")
    template_name = "kitchen/dish_form.html"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish_list")
    template_name = "kitchen/dish_form.html"
    form_class = DishForm


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish_list")


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    paginate_by = 5
    context_object_name = "dish_types"
    template_name = "kitchen/dish_types_list.html"

    def get_context_data(self, **kwargs: Any) -> Dict:
        context = super(DishTypeListView, self).get_context_data(**kwargs)

        context["search_form"] = DishTypeSearchForm(self.request.GET)
        return context

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish_types_list")
    template_name = "kitchen/dish_types_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish_types_list")
    template_name = "kitchen/dish_types_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish_types_list")
    template_name = "kitchen/dish_types_confirm_delete.html"
