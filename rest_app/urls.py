from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
import sys
print(f"=== Loading rest_app.urls ===", file=sys.stderr)
print(f"Trying to import views...", file=sys.stderr)

try:
    from . import views
    print(f"Successfully imported views!", file=sys.stderr)
except Exception as e:
    print(f"ERROR importing views: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc()
urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    
    
    # Auth URLs
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Add this
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Optional
    
    
    # Menu List - THIS IS MISSING!
    path('menu/', views.MenuListView.as_view(), name='menu_list'),
    
    # Add menu item
    path('menu/add/', views.MenuCreateView.as_view(), name='menu_add'),
    
    # Update menu item
    path('menu/<int:pk>/update/', views.MenuUpdateView.as_view(), name='menu_update'),
    
    # Delete menu item
    path('menu/<int:pk>/delete/', views.MenuDeleteView.as_view(), name='menu_delete'),
    
    # View single menu item detail
    path('menu/<int:pk>/', views.MenuDetailView.as_view(), name='menu_detail'),
]