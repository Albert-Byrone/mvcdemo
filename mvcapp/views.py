from django.shortcuts import render

# Create your views here.
def student_list(request):
    student_list = Student.objects.all()
    return render(request, 'list.html' , context={ 'student_list': student_list})

