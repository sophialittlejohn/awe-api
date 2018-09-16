from django.urls import path

from project.api.staff.views import ListAllStaffView, StaffDetailView, CreateStaffView, UpdateStaffView

app_name = 'staff'

urlpatterns = [
    path('', ListAllStaffView.as_view(), name='list_all_staff'),
    path('<int:pk>/', StaffDetailView.as_view(), name='staff_detail'),
    path('new/', CreateStaffView.as_view(), name='staff_new'),
    path('update/<int:pk>/', UpdateStaffView.as_view(), name='update_staff'),
]