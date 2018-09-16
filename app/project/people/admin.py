from django.contrib import admin

from project.people.models import Address, Student, Staff

# admin.site.register(Address)
# admin.site.register(Student)
# admin.site.register(Staff)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    filter_horizontal = ['awe_class']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'number', 'city', 'zip', 'country']
