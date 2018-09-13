from django.urls import path

from project.api.staff.views import ListAllStaffView, StaffDetailView

app_name = 'staff'

urlpatterns = [
    path('', ListAllStaffView.as_view(), name='list_all_staff'),
    path('<int:pk>/', StaffDetailView.as_view(), name='staff_detail'),
]