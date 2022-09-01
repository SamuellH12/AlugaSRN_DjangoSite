from django.urls import path
from . import views

urlpatterns = [
    path('', views.initial_page, name='initial_page'),
    path('house/<int:pk>/', views.house_detail, name='house_detail'),
    path('quem', views.quemSomos, name="quem"),
    path('MyHouses', views.myHouses, name='myHouses'),
    path("register/", views.register_page, name="register"),
    path('pesquisa',  views.pesquisa, name="pesquisa"),
    path('house/<int:pk>/edit', views.editHouse, name='house_edit'),
    path('house/<int:pk>/delete', views.deleteHouse, name='house_delete'),
    path('newHouse', views.newHouse, name="newHouse")
]