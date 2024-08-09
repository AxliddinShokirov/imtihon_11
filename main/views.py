from .models import Attendance
from django.shortcuts import render,redirect
from main import models
from django.contrib.auth.decorators import login_required
from django.utils import timezone  # bugungi sanani olish uchun


@login_required(login_url='login')
def attendance(request):
    attendance=models.Attendance.objects.all()
    xodimlar=models.Xodimlar_name.objects.all()
    redirect ('register_user')
    return render(request, 'dashboard/attendance.html', {'attendance': attendance, 'xodimlar': xodimlar})
    



def mark_attendance(request, id):
    attendance = models.Attendance.objects.get(id=id)
    
    # Toggle the isinstance status
    attendance.isinstance = not attendance.isinstance
    attendance.save()
    
    return redirect('attendance')  # Replace with the name of the view rendering your template

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


