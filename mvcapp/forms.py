from ast import arg
from pydoc import classname
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class  Meta:
        model = Student
        fields = "__all__"
        labels = {
            'fullname': 'Full Name',
            'student_number': 'Student Number',
            'phonenumber': 'Phone Number',
            'classname': 'Class Name',
        }

    
    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['classname'].empty_label = "Select Class"
