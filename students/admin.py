from django.contrib import admin
from .models import Course, Department, Registration, Semester, Student


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'faculty']
    search_fields = ['code', 'name', 'faculty']


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'start_date', 'end_date', 'is_active']
    list_filter = ['year', 'is_active']
    search_fields = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'title', 'department', 'semester', 'credits']
    list_filter = ['department', 'semester']
    search_fields = ['code', 'title']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'first_name', 'last_name', 'email', 'department', 'status']
    list_filter = ['department', 'status', 'current_semester']
    search_fields = ['student_id', 'first_name', 'last_name', 'email']


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'semester', 'registered_on', 'grade']
    list_filter = ['semester', 'course']
    search_fields = ['student__student_id', 'course__code']
