from multiprocessing import context
from django import forms
from django.shortcuts import redirect, render
from mvcapp.forms import StudentForm
from mvcapp.models import Student


# Create your views here.
def student_list(request):
    student_list = Student.objects.all()
    return render(request, 'list.html' , context={ 'student_list': student_list})

def add_student(request, id=0):
    if request.method == 'GET':
        if id ==0:
            form = StudentForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request, 'add.html',{ 'form': form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect('list')



def student_delete(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('list')
