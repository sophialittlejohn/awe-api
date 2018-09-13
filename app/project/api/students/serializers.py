from rest_framework import serializers

from project.api.awe_classes.serializers import AWEClassSerializer, AddressSerializer
from project.people.models import Student


class StudentDetailSerializer(serializers.ModelSerializer):
    awe_class = AWEClassSerializer(many=True)
    address = AddressSerializer()

    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'awe_class',
            'birthdate',
            'email',
            'address',
            'phones',
            'mother_name',
            'mother_workplace',
            'father_name',
            'father_workplace',
            'cambridge_exam',
            'registered',
            'start_date',
            'end_date',
            'cost_per_class',
            'discount',
            'notes',
        ]


class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'awe_class',
            'birthdate',
            'email',
            'mother_name',
            'father_name',
            'registered',
            'start_date',
            'notes',
        ]
