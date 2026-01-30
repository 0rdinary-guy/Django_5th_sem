from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import MenuForm
from .models import Menu
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from django.views.generic import ListView, DetailView  # Make sure ListView is imported
from .models import Menu  # Make sure Menu is imported


class MenuCreateView(LoginRequiredMixin, CreateView):

    model= Menu
    form_class = MenuForm
    template_name = 'menu_form.html'
    success_url = reverse_lazy('menu_list')
    login_url = 'login'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Menu item added successfeully!")

        return response

    def form_invalid(self, form):
        messages.error(self.request, "There was an error adding the menu item. Please try again.")
        return super().form_invalid(form)


#update
class MenuUpdateView(LoginRequiredMixin, UpdateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menu_form.html'
    success_url = reverse_lazy('menu_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Menu item updated successfully!")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "There was an error updating the menu item. Please check the form.")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Update Menu: {self.object.name}'
        context['submit_button'] = 'Update'
        context['form_action'] = 'Update'
        return context


#delete
class MenuDeleteView(LoginRequiredMixin, DeleteView):
    model = Menu
    template_name = 'menu_confirm_delete.html'
    success_url = reverse_lazy('menu_list')
    login_url = 'login'
    context_object_name = 'menu'

    def delete(self, request, *args, **kwargs):
        menu_name = self.get_object().name
        messages.success(self.request, f"'{menu_name}' has been deleted successfully!")
        return super().delete(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Delete Menu Item'
        context['confirm_message'] = f'Are you sure you want to delete "{self.object.name}"?'
        return context
    
# Add this class
class MenuListView(ListView):
    model = Menu
    template_name = 'menu_list.html'
    context_object_name = 'menus'
    ordering = ['-created_at']

# Add this class
class MenuDetailView(LoginRequiredMixin, DetailView):
    model = Menu
    template_name = 'menu_detail.html'
    context_object_name = 'menu'
    login_url = 'login'
    
class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')
    
def home(request):
    return render(request, 'home.html')

# def add_menu(request):
#     if request.method == "POST":
#         form = MenuForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('menu_list')
#     else:
#         form = MenuForm()

#     return render(request, 'add_menu.html', {'form': form})


# def menu_list(request):
#     menus = Menu.objects.all()
#     return render(request, 'menu_list.html', {'menus': menus})