from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from project.api.awe_classes.serializers import AWEClassSerializer, AWEClassDetailSerializer
from project.awe_classes.models import AWEClass


class ListAllClassesView(ListAPIView):
    serializer_class = AWEClassSerializer
    queryset = AWEClass.objects.all()
    permission_classes = [IsAuthenticated]


class ClassDetailView(RetrieveAPIView):
    serializer_class = AWEClassDetailSerializer
    queryset = AWEClass.objects.all()
    permission_classes = [IsAuthenticated]


class CreateClassView(ListCreateAPIView):
    serializer_class = AWEClassDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = AWEClass.objects.all()


class UpdateClassView(UpdateAPIView):
    serializer_class = AWEClassDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = AWEClass.objects.all()
