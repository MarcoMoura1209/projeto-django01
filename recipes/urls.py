from django.urls import path
from recipes.views import home, ajuda

urlpatterns = [
    path('', home),
    path('ajuda/', ajuda)
]