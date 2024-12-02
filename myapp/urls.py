from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('success/', views.success_view, name='success_url'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('passchange/', views.pass_change, name='passchange'),
    path('passchange2/', views.pass_change2, name='passchange2'),
    path('change_user_data/', views.change_user_data, name='change_user_data'),
]
