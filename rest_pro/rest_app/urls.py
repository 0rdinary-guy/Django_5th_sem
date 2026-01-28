from rest_pro import urls
from django.urls import path
from . import views
from .views import home,menu_list

urlpatterns = [
    path("", home, name='home'),
    path('list/', views.menu_list, name='menu_list'),
]
