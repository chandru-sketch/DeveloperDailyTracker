from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('progress/', views.progress, name='progress'),
    path('goals/', views.goals, name='goals'),
    path('settings/', views.settings_page, name='settings'),
    path('profile/', views.profile, name='profile'),
    path('save-theme/', views.save_theme, name='save_theme'),
]