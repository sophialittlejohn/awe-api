from rest_framework import serializers

from ...people.models import Staff
# from project.api.awe_classes.serializers import AddressSerializer


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = [
            'role',
            'first_name',
            'last_name',
            'email',
            'phone',
            'mobile',
            'key_riehen',
            'key_therwil',
        ]


class StaffNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name']


class StaffDetailSerializer(serializers.ModelSerializer):
    #address = AddressSerializer()

    class Meta:
        model = Staff
        fields = [
            'role',
            'first_name',
            'last_name',
            'birthdate',
            'email',
            'address',
            'phone',
            'mobile',
            'contract',
            'old_ahv',
            'ahv',
            'profession',
            'date_hired',
            'date_left',
            'start_salary',
            'first_aid',
            'salary_raise_date',
            'raise_step',
            'new_salary',
            'key_riehen',
            'key_therwil',
            'swiss_permit',
        ]