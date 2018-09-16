from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from project.api.students.serializers import StudentsSerializer, StudentDetailSerializer
from project.people.models import Student


class ListAllStudentsView(ListAPIView):
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()

    def get_queryset(self):
        query = self.request.query_params
        if query.get('first_name'):
            first_name = query.get('first_name')
            return Student.objects.filter(first_name__icontains=first_name)
        elif query.get('last_name'):
            last_name = query.get('last_name')
            return Student.objects.filter(last_name__icontains=last_name)
        elif query.get('teacher'):
            first_name = query.get('teacher')
            return Student.objects.filter(awe_class__teacher__first_name__icontains=first_name)
        elif query.get('current'):
            return Student.objects.filter(end_date__isnull=True)
        elif query.get('past'):
            return Student.objects.filter(end_date__isnull=False)
        return Student.objects.all()


class StudentDetailView(RetrieveAPIView):
    serializer_class = StudentDetailSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated]


class CreateStudentView(ListCreateAPIView):
    serializer_class = StudentDetailSerializer
    permission_classes = [IsAdminUser]
    queryset = Student.objects.all()


class UpdateStudentView(UpdateAPIView):
    serializer_class = StudentDetailSerializer
    permission_classes = [IsAdminUser]
    queryset = Student.objects.all()