from django.shortcuts import render, redirect
from .forms import MenuForm
from .models import Menu

def home(request):
    return render(request, 'home.html')

def add_menu(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm()

    return render(request, 'add_menu.html', {'form': form})


def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'menu_list.html', {'menus': menus})