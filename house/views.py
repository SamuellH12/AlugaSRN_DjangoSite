from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q
from .models import House
from .forms import NewUserForm, NewHouseForm


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

def house_detail(request, pk):
    house = get_object_or_404(House, pk=pk)
    return render(request, 'house/house_detail.html', {'house' : house})

def quemSomos(request):
    return render(request, 'house/quemSomos.html', {})

@login_required
def myHouses(request):
    houses = House.objects.filter(dono=request.user)
    return render(request, 'house/myHouses.html', {'houses' : houses})

@login_required
def newHouse(request):
    if request.method == "POST":
        form = NewHouseForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            house.dono = request.user
            house.published_date = timezone.now()
            house.save()
            return redirect('house', pk=house.pk)
    else:
        form = NewHouseForm()

    return render(request, 'house/add.html', {'form' : form})

def pesquisa(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
        if query == 'None':
            query = 'a'
        donos = User.objects.filter( Q( first_name__icontains = query ) | Q( last_name__icontains = query ) )
        results = House.objects.filter( Q(titulo__icontains = query) | Q( dono__in = donos ) )

    return render(request, 'house/pesquisa.html', {'query': query, 'results': results})


def register_page(request):

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("/")

        messages.error(request, "Unsuccessful registration. Invalid information.")


    form = NewUserForm()
    return render(request, 'house/register.html', {'register_form' : form})


### ta faltando: ###
# Filtrar por cidade e bairro
# Google Map
# pagina de detalhes e solicitação de compra