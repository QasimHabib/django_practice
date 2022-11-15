#from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from .models import Students
from .forms import StudentsForm
# Create your views here.

def index(request):
    student = Students.objects.all()
    #template = loader.get_template('app1/index.html')
    context ={
        'student' : student
    }
    return render(request, 'app1/index.html', context)
    #return HttpResponse(template.render(context, request))

def detail(request, student_id):
    student = get_object_or_404(Students, pk= student_id)
    return render(request, 'app1/detail.html',{'student': student})

def add(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = StudentsForm()
        context = {
            'form': form,
        }
    return render(request, 'app1/add.html', context)