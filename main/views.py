from .models import Attendance
from django.shortcuts import render,redirect
from main import models
from django.contrib.auth.decorators import login_required
from django.utils import timezone  

def base_s(request):
    salom=models.User_names.objects.last()
    return render(request,'dashboard/base.html', {'salom': salom})

@login_required(login_url='login')
def attendance(request):
    attendance=models.Attendance.objects.all()
    xodimlar=models.Xodimlar_name.objects.all()
    redirect ('register_user')
    return render(request, 'dashboard/attendance.html', {'attendance': attendance, 'xodimlar': xodimlar})
    



def mark_attendance(request, id):
    attendance = models.Attendance.objects.get(id=id)
    

    attendance.isinstance = not attendance.isinstance
    attendance.save()
    
    return redirect('attendance') 

def User_create(request):
    context={}
    context['categorys'] = models.User_name.objects.all()
    if request.method == 'POST':
         models.User_name.objects.create(name=request.POST['name'], 
                                               ega=request.POST['ega'],
                                               email=request.POST['email'],
                                               phone_number=request.POST['phone_number'],
                                               image=request.POST['image'])
         return redirect('register_user')
        
    return render(request,'main/register_user.html')


