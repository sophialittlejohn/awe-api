from django.urls import path

from project.api.awe_classes.views import ListAllClassesView, ClassDetailView, CreateClassView, UpdateClassView

app_name = 'class'

urlpatterns = [
    path('', ListAllClassesView.as_view(), name='list_all_classes'),
    path('<int:pk>/', ClassDetailView.as_view(), name='class_detail'),
    path('new/', CreateClassView.as_view(), name='new_class'),
    path('update/<int:pk>/', UpdateClassView.as_view(), name='update_class'),
]