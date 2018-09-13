from django.urls import path, include

app_name = 'api'
urlpatterns = [
    path('auth/', include('project.api.auth.urls'), name='auth'),
    path('students/', include('project.api.students.urls'), name='students'),
    path('staff/', include('project.api.staff.urls'), name='staff'),
    path('class/', include('project.api.awe_classes.urls'), name='class'),
]