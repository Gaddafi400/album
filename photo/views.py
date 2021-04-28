from django.shortcuts import render
from .models import Student
# Create your views here.


def home(request):
    student = Student.objects.all()
    context = {
        'student': student
    }
    return render(request, 'photo/home.html', context=context)

