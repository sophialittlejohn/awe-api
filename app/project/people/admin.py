from django.contrib import admin

from project.people.models import Address, Student, Staff

# admin.site.register(Address)
# admin.site.register(Student)
# admin.site.register(Staff)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(Staff)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(Address)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['street', 'number', 'city', 'zip', 'country']
