# from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('Esta é a pagina inicial')


def ajuda(request):
    return HttpResponse('Pagina de ajuda')

