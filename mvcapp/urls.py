from django.urls import path, include
from . import views


urlpatterns = [
    path('add-student/', views.add_student, name='add-student'),
    path('<int:id>/', views.add_student, name='student-update'),
    path('', views.student_list, name='list'),
    path('delete/<int:id>', views.student_delete, name='delete-student')
]
