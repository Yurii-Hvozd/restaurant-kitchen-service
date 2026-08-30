from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from kitchen.models import Cook, Dish, Ingredient
from django.forms import ModelForm
from django import forms


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "years_of_experience",)


class DishForm(ModelForm):
    cooks = forms.ModelMultipleChoiceField(queryset=get_user_model().objects.all(),
                                           widget=forms.CheckboxSelectMultiple(),
                                           required=False
                                           )
    ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all(),
                                                 widget=forms.CheckboxSelectMultiple(),
                                                 required=True
                                                 )

    class Meta:
        model = Dish
        fields = "__all__"


class CookSearchForm(forms.Form):
    search = forms.CharField(max_length=255,
                                             required=False,
                                             label="",
                                             widget=forms.TextInput(attrs={"placeholder": "Search by name or surname"}),
                                             )


class DishSearchForm(forms.Form):
    name = forms.CharField(max_length=255,
                           required=False,
                           label="",
                           widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
                           )

class IngredientSearchForm(forms.Form):
    name = forms.CharField(max_length=255,
                           required=False,
                           label="",
                           widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
                           )

class DishTypeSearchForm(forms.Form):
    name = forms.CharField(max_length=255,
                           required=False,
                           label="",
                           widget=forms.TextInput(attrs={"placeholder": "Search by type"}),
                           )

