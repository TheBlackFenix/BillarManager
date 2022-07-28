"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views
from django.urls import path

urlpatterns = [
    
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('mesa/', views.MesaView.as_view()),
    path('mesa/<int:pk>/', views.MesaDetail.as_view()),
    path('estado/', views.EstadoView.as_view()),
    path('estado/<int:pk>/', views.EstadoDetail.as_view()),
    path('tipomesa/', views.TipoMesaView.as_view()),
    path('tipomesa/<int:pk>/', views.TipoMesaDetail.as_view()),
    path('tarifa/', views.TarifaView.as_view()),
    path('tarifa/<int:pk>/', views.TarifaDetail.as_view()),
    path('cliente/', views.ClienteView.as_view()),
    path('cliente/<int:pk>/', views.ClienteDetail.as_view()),
    path('tiempo/', views.TiempoView.as_view()),
    path('tiempo/<int:pk>/', views.TiempoDetail.as_view()),
]
