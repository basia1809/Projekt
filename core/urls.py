from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('oferta/', views.offer, name='offer'),
    path('cennik/', views.prices, name='prices'),
    path('zamow/', views.order, name='order'),
]
