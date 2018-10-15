from django.urls import path

from project.api.students.views import ListAllStudentsView, StudentDetailView, CreateStudentView, UpdateStudentView, \
    ListAllPastStudentsView, ListAllCurrentStudentsView, FilterAllStudents

app_name = 'students'

urlpatterns = [
    path('', ListAllStudentsView.as_view(), name='list_all_students'),
    path('past/', ListAllPastStudentsView.as_view(), name='list_all_past_students'),
    path('current/', ListAllCurrentStudentsView.as_view(), name='list_all_current_students'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('new/', CreateStudentView.as_view(), name='new_student'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='new_student'),
    path('asc/', FilterAllStudents.as_view(), name='students_asc'),
]
