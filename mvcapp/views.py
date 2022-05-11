import io
from django import forms
from django.shortcuts import redirect, render
from mvcapp.forms import StudentForm, StudentBulkForm
from mvcapp.models import Student
from django.contrib import messages #import messages    


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
            # messages.success(request, 'Added successfully')
        return render(request, 'add.html',{ 'form': form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully')


        return redirect('list')

def bulk_upload(request):
    prompt = {
        'order': 'Order of the CSV  ClassName, Full Name, Phone Number, Student Number'
    }
    if request.method == 'GET':
        return render(request,'list.html', prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set =  csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv_file.read(io_string, delimeter=',', quotechar='|'):
        _, created = Student.objects.update_or_create(
            classname = column[0],
            fullnane = column[1],
            phonenumber = column[2],
            student_number = column[3]
        )
    context={}
    return render(request, 'list.html', context)

# >Class</div>
#         <div class="col col-2">Full Name</div>
#         <div class="col col-3">Mobile</div>
#         <div class="col col-4">Student No.</div>
def student_delete(request, id):
    student = Student.objects.get(pk=id)

    student.delete()
    return redirect('list')
