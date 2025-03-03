from django.urls import path,include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import user_passes_test

store = ''
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),  
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'), 

    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('member/', views.member_dashboard, name='member_dashboard'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('store/', views.store_dashboard, name='store_dashboard'),
    path('store/add_product/', views.add_product, name='add_product'),
    path('store/edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('store/delete_product/<int:product_id>/', views.delete_product, name='delete_product'),


]