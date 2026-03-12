from django.shortcuts import render
from utils.recipe.factory import make_recipe
# Create your views here.
# from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-views.html', context={
        'recipe': make_recipe(),
    })
