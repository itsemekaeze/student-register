from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.


def homePage(request):
    students = Student.objects.all()
    context = {
        "students": students
    }
    return render(request, 'home.html', context)


def addPage(request):
    name = request.POST.get('content')
    age = request.POST.get('age')
    x_class = request.POST.get('x_class')
    gender = request.POST.get('sex')
    dob = request.POST.get('dob')
    current_date = timezone.now()
    try:

        if request.method == 'POST':
            Student.objects.create(name=name, age=age, x_class=x_class, gender=gender, dob=dob, created_at=current_date)
            return redirect('home')
    except ValueError:
        return redirect('add-student')

    return render(request, 'add.html')


def deletePage(request, id):

    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    context = {
        "obj": student
    }
    return render(request, 'delete.html', context)


def viewPage(request, id):
    students = Student.objects.get(id=id)
    context = {
        "students": students
    }
    return render(request, 'view.html', context)