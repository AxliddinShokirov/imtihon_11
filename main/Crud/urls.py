from django.urls import path
from main.Crud import views
 
urlpatterns =[
     path('xodimlar_list/', views.Xodim_list, name='Xodim_list'),
     path('xodim_create/', views.Xodimlar_craet, name='Xodimlar_create' ),
     path('xodim_update/<int:id>/', views.update_Xodim, name='Xodimlar_update'),
     path('xodim_delete/<int:id>/', views.Xodimlar_delete, name='Xodimlar_delete' ),
     path('attendance/create/', views.create_attendance, name='attendance_create'),
     path('attendance/list/', views.create_attendance, name='attendance_list'),
     path('attendance/delete/<int:id>/', views.delete_attendance, name='attendance_delete'),
    # boshqa URL yo'llarini qo'shish mumkin


     
 ]