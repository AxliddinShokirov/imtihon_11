from django.urls import path, include
from main import views
from main.Crud import urls

urlpatterns = [
   
    path('attendes/', views.attendance, name='attendance'),
    path('crud/', include('main.Crud.urls'), name='crud'),
    path('mark_attendance/<int:id>/', views.mark_attendance, name='mark_attendance'),
    path('', include('main.login.urls'), name='login'),
    path('', views.base_s,name='user'),
    ]