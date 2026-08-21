from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from kitchen.models import Cook, Dish, DishType, Ingredient


# Register your models here.
@admin.register(Cook)
class CookAdmin(UserAdmin):
    pass

@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass


