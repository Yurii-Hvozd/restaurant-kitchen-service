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
