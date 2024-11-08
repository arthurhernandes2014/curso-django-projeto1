# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# Toda consulta de rota é chamado de um HTTP REQUEST, toda vez que fazemos uma
# consulta, a rota irá receber um request, como esse exemplo abaixo.
def home(request):
    return render(request, "recipes/pages/home.html", context={
        "name": "Tutu"
    })
