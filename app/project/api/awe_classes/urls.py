from django.urls import path

from project.api.awe_classes.views import ListAllClassesView, ClassDetailView

app_name = 'class'

urlpatterns = [
    path('', ListAllClassesView.as_view(), name='list_all_classes'),
    path('<int:pk>/', ClassDetailView.as_view(), name='staff_detail'),
]