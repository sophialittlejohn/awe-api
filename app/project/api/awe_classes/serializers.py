from rest_framework import serializers

from project.api.staff.serializers import StaffSerializer, StaffNameSerializer
from project.awe_classes.models import AWEClass, Classroom, Session, Book, FirstAid
from project.people.models import Address


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'


class SessionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name']


class FirstAidSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstAid
        fields = '__all__'


class AWEClassDetailSerializer(serializers.ModelSerializer):
    teacher = StaffSerializer(many=True)
    class_room = ClassroomSerializer()
    session = SessionSerializer()
    books = BookSerializer()

    class Meta:
        model = AWEClass
        fields = [
            'name',
            'teacher',
            'day',
            'time',
            'class_room',
            'total_classes',
            'program',
            'session',
            'books'
        ]


class AWEClassSerializer(serializers.ModelSerializer):
    teacher = StaffNameSerializer(many=True)
    class_room = ClassroomSerializer()
    session = SessionNameSerializer()
    books = BookNameSerializer()

    class Meta:
        model = AWEClass
        fields = [
            'name',
            'teacher',
            'day',
            'time',
            'class_room',
            'total_classes',
            'program',
            'session',
            'books'
        ]
