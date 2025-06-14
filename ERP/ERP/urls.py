"""
URL configuration for ERP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from CRUD.views import AssetViewSet
from django.contrib import admin
from django.urls import path, include 
from . import views # Import do arquivo que contém as URLs do projeto ERP
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('assets', AssetViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view), 
    path('estoque/', views.estoque_view, name='estoque'), 
    path('CRUD/', include('CRUD.urls', namespace='CRUD'))


    #path('CRUD/', include(router.urls)),  # Incluindo as URLs da API REST
    #path('CRUD/', include('CRUD.urls')),  # Incluindo as URLs do CRUD

]

# Em TRABALHO_2_ERP/ERP/urls.py (ou o urls.py principal do seu projeto)


