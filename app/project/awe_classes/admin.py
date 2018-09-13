from django.contrib import admin

from project.awe_classes.models import AWEClass, Book, Session, Classroom, FirstAid

# admin.site.register(AWEClass)
admin.site.register(Book)
admin.site.register(FirstAid)
# admin.site.register(Session)
# admin.site.register(Classroom)


@admin.register(AWEClass)
class AWECLassAdmin(admin.ModelAdmin):
    list_display = ['name', 'day', 'start_time', 'end_time', 'class_room']


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'spots']


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'number_of_classes']
