from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from project.api.staff.serializers import StaffSerializer, StaffDetailSerializer
from project.people.models import Staff


class ListAllStaffView(ListAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    permission_classes = [IsAuthenticated]


class StaffDetailView(ListAPIView):
    """
        Get student by student ID
    """
    serializer_class = StaffDetailSerializer
    queryset = Staff.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Staff.objects.filter(id=self.kwargs.get('pk'))
