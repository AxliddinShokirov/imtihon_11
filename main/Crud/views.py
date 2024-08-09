from main.models import Attendance, Xodimlar_name
from main import models
from django.shortcuts import render,redirect

def Xodim_list(request):
    xodimlar=models.Xodimlar_name.objects.all()
    return render(request, 'dashboard/crude/xodim_list.html', {'xodimlar': xodimlar})

def Xodimlar_craet(request):
    context = {}
    context['categorys'] = models.Xodimlar_name.objects.all()
    if request.method == 'POST':
          models.Xodimlar_name.objects.create(
              name = request.POST['name'],
              surname = request.POST['surname'],
              age = request.POST['age'],
              email = request.POST['email'],
              phone_number = request.POST['phone'],
              address = request.POST['address'],
           
            
          )
          return redirect('Xodim_list')
  
       
    return render(request, 'dashboard/crude/xodim_craets.html', context)
    




from django.db import IntegrityError

def update_Xodim(request, id):
    xodim =models.Xodimlar_name.objects.get(id=id)    
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        address = request.POST.get('address')

        if not name:  # Ensure that 'name' is not empty
            return render(request, 'dashboard/crude/xodim_updeat.html', {
                'xodim': xodim,
                'error_message': 'Name field is required.'
            })

        try:
            xodim.name = name
            xodim.surname = surname
            xodim.age = age
            xodim.email = email
            xodim.phone_number = phone_number
            xodim.address = address
            xodim.save()
            return redirect('Xodim_list')
        except IntegrityError as e:
            return render(request, 'dashboard/crude/xodim_updeat.html', {
                'xodim': xodim,
                'error_message': f'An error occurred: {e}'
            })
    
    return render(request, 'dashboard/crude/xodim_updeat.html', {'xodim': xodim})





def Xodimlar_delete(request, id):
    xodim = models.Xodimlar_name.objects.get(id=id)
    xodim.delete()
    return redirect('Xodim_list')



def Xodimlar_search(request):
    if request.method == 'POST':
        search_term = request.POST.get('search_term')
        xodim = models.Xodimlar_name.objects.filter(name__icontains=search_term)
        return render(request, 'xodimlar.html', {'xodimlar': xodim})
    
    return render(request, 'xodim_search.html')


def create_attendance(request):
    context = {}
    context['xodimlar'] = Xodimlar_name.objects.all() 

    if request.method == 'POST':
        Attendance.objects.create(
            xodimlar_name = Xodimlar_name.objects.get(id=request.POST['xodim']),
            date = request.POST['date'],
            isinstance = request.POST.get(False , True) 
        )
        return redirect('attendance_create')  

    return render(request, 'dashboard/davomat/create.html', context)

def attendance(request):
    attendance = Attendance.objects.all()
    return render(request, 'dashboard/davomat/attendance.html', {'attendance': attendance})

def update_attendance(request, id):
    attendance = Attendance.objects.get(id=id)
    context = {}
    context['attendance'] = attendance
    context['xodimlar'] = Xodimlar_name.objects.all()
    
    if request.method == 'POST':
        xodimlar_name = Xodimlar_name.objects.get(id=request.POST['xodim'])
        date = request.POST['date']
        isinstance = request.POST.get('isinstance', False)
        attendance.xodimlar_name = xodimlar_name
        attendance.date = date
        attendance.isinstance = isinstance
        attendance.save()
        return redirect('attendance')
    
    return render(request, 'dashboard/davomat/update.html', context)

def delete_attendance(request, id):
    attendance = Attendance.objects.get(id=id)
    attendance.delete()
    return redirect('attendance')

def search_attendance(request):
    if request.method == 'POST':
        search_term = request.POST.get('search_term')
        attendance = Attendance.objects.filter(xodimlar_name__name__icontains=search_term)
        return render(request, 'dashboard/davomat/attendance.html', {'attendance': attendance})
    
    return render(request, 'dashboard/davomat/search.html')










    
        
    


    