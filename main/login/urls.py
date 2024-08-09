from . import views
from django.urls import path

urlpatterns = [
    # path('register/', views.register_user, name='register_user'),
    path('register/', views.register_user, name='register_user'),  # Registration page
    path('', views.login_user, name='login_user'),  # Login page
    path('logout/', views.log_out, name='log_out'),  # Logout
    path('error/', views.error, name='error'), 
]