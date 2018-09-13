from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from project.api.students.serializers import StudentsSerializer, StudentDetailSerializer
from project.people.models import Student


class ListAllStudentsView(ListAPIView):
    """
        List all students
    """
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()


class StudentDetailView(ListAPIView):
    """
        Get student by student ID
    """
    serializer_class = StudentDetailSerializer
    queryset = Student.objects.filter()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Student.objects.filter(id=self.kwargs.get('pk'))


# class StudentByClassView(ListAPIView):
#     """
#         Get student by class ID
#     """
#     serializer_class = StudentsSerializer
#     queryset = Student.objects.filter()
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         return Student.objects.filter(awe_class=self.kwargs.get('pk'))
