from django.urls import path

from project.api.students.views import ListAllStudentsView, StudentDetailView, CreateStudentView, UpdateStudentView

app_name = 'students'

urlpatterns = [
    path('', ListAllStudentsView.as_view(), name='list_all_students'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('new/', CreateStudentView.as_view(), name='new_student'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='new_student'),
]