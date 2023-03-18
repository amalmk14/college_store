from django.shortcuts import render, redirect, get_object_or_404
from .models import Task,Course
from django.contrib import messages
from .forms import DeptForm
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def base(request):
    return render(request,'base.html')

def add(request):
    form = DeptForm()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        age = request.POST.get('age', '')
        dob = request.POST.get('dob', '')
        phone = request.POST.get('phone', '')
        gender = request.POST.get('gender', '')
        address = request.POST.get('address', '')
        # purpose = request.POST.get('purpose','')
        # department = request.POST.get('department',)
        # course = request.POST.get('course',)
        materials = request.POST.get('materials','')
        email = request.POST.get('email', '')
        task = Task(name=name, age=age, dob=dob, gender=gender, address=address, materials=materials, email=email,phone=phone)
        task.save()
        messages.info(request,'Request Confirmed')
        return redirect('add')

    return render(request,'add.html',{'form':form})

#
# def task_update_view(request,pk):
#     task = get_object_or_404(Task, pk=pk)
#     form = DeptForm(instance=task)
#     if request.method == 'POST':
#         form = DeptForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect('task_change', pk=pk)
#     return render(request, 'add.html',{'form':form})


# AJAX
def load_course(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'course_dropdown_list.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)