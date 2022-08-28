from django.shortcuts import render
from django.utils import timezone
from .models import House

def initial_page(request):
    houses = House.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    houseslist = []
    minilist = []

    for i in range(len(houses)):
        houses[i].descricao = houses[i].descricao[0:200]
        minilist.append(houses[i])
        if(i%3 == 2):
            houseslist.append(minilist)
            minilist = []

    if len(minilist) != 0:
        #for i in range(3-len(minilist)):
            #minilist.append(houses[i])
        houseslist.append(minilist)
            

    return render(request, 'house/initial_page.html', {'HouseList':houseslist})

### ta faltando: ###
# Filtrar por cidade e bairro
# Google Map
# Login de usuário