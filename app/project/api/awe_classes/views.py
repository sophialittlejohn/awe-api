from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from project.api.awe_classes.serializers import AWEClassSerializer, AWEClassDetailSerializer
from project.awe_classes.models import AWEClass


class ListAllClassesView(ListAPIView):
    serializer_class = AWEClassSerializer
    queryset = AWEClass.objects.all()
    permission_classes = [IsAuthenticated]


class ClassDetailView(ListAPIView):
    """
        Get student by student ID
    """
    serializer_class = AWEClassDetailSerializer
    queryset = AWEClass.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return AWEClass.objects.filter(id=self.kwargs.get('pk'))
