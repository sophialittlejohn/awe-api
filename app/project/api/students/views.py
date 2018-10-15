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
            return Student.objects.filter(first_name__icontains=first_name).order_by('first_name', 'last_name')
        elif query.get('last_name'):
            last_name = query.get('last_name')
            return Student.objects.filter(last_name__icontains=last_name).order_by('last_name', 'first_name')
        elif query.get('teacher'):
            first_name = query.get('teacher')
            return Student.objects.filter(awe_class__teacher__first_name__icontains=first_name).order_by('first_name', 'last_name')
        elif query.get('current'):
            q1 = query.get('current')
            if query.get('current') == 'asc':
                # get only current students ordered by start_date asc
                return Student.objects.filter(end_date__isnull=True).order_by('start_date', 'first_name')
            elif query.get('current') == 'desc':
                # get only current students ordered by start_date desc
                return Student.objects.filter(end_date__isnull=True).order_by('-start_date', 'first_name')
            elif query.get('current') == 'all_asc':
                # get all students ordered by start_date asc
                return Student.objects.all().order_by('start_date', 'first_name')
            elif query.get('current') == 'all_desc':
                # get all students ordered by start_date desc
                return Student.objects.all().order_by('-start_date')
        elif query.get('past'):
            return Student.objects.filter(end_date__isnull=False).order_by('-start_date', 'first_name')
        # elif query.get('past'):
        #     return Student.objects.filter(end_date__isnull=False)
        return Student.objects.all().order_by('last_name', 'first_name')


class FilterAllStudents(ListAPIView):
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()

    def get_queryset(self):
        query = self.request.query_params
        if query.get('asc'):
            return Student.objects.all().order_by('start_date', 'first_name')
        elif query.get('desc'):
            return Student.objects.all().order_by('-start_date', 'first_name')
        else:
            return Student.objects.all()


class ListAllCurrentStudentsView(ListAPIView):
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()

    def get_queryset(self):
        query = self.request.query_params
        if query.get('asc'):
            return Student.objects.filter(end_date__isnull=True).order_by('start_date', 'first_name')
        elif query.get('desc'):
            return Student.objects.filter(end_date__isnull=True).order_by('-start_date', 'first_name')


class ListAllPastStudentsView(ListAPIView):
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()

    def get_queryset(self):
        return Student.objects.filter(end_date__isnull=False).order_by('end_date', 'start_date')


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
