from django.shortcuts import render
from .models import Student
from django.views.generic import ListView, DetailView
# Create your views here.


# def home(request):
#     student = Student.objects.all()
#     context = {
#         'student': student
#     }
#     return render(request, 'photo/home.html', context=context)


class HomeView(ListView):
    model = Student
    template_name = 'photo/home.html'
    context_object_name = 'student'
    ordering = ['name']
    # paginate_by = 6


class StudentDetailView(DetailView):
    model = Student
    # template_name = 'photo/home.html'
    # context_object_name = 'student'
    # ordering = ['name']
