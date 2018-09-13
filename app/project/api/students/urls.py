from django.urls import path

from project.api.students.views import ListAllStudentsView, StudentDetailView

app_name = 'students'

urlpatterns = [
    path('', ListAllStudentsView.as_view(), name='list_all_students'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    # path('class/<int:pk>/', StudentByClassView.as_view(), name='students_by_class'), todo
]