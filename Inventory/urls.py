
from django.contrib import admin
from django.urls import path
from Inventory_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inventory', views.inventory, name='inventory'),
]
