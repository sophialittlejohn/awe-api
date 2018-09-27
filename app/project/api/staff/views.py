from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from project.api.staff.serializers import StaffSerializer, StaffDetailSerializer
from project.people.models import Staff


class ListAllStaffView(ListAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    permission_classes = [IsAuthenticated]


class StaffDetailView(RetrieveAPIView):
    serializer_class = StaffDetailSerializer
    queryset = Staff.objects.all()
    permission_classes = [IsAuthenticated]


class CreateStaffView(ListCreateAPIView):
    serializer_class = StaffDetailSerializer
    permission_classes = [IsAdminUser]
    queryset = Staff.objects.all()


class UpdateStaffView(UpdateAPIView):
    serializer_class = StaffDetailSerializer
    permission_classes = [IsAdminUser]
    queryset = Staff.objects.all()
