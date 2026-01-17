from django.urls import path
from recipes.views import home, help

urlpatterns = [
    path('', home),
    path('help/', help)
]