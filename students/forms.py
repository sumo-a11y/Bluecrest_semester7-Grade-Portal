from django import forms
from django.core.exceptions import ValidationError

from .models import Course, Department, Registration, Semester, Student


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'code', 'faculty', 'description']

    def clean_code(self):
        code = self.cleaned_data.get('code', '').strip().upper()
        if Department.objects.filter(code=code).exclude(pk=self.instance.pk).exists():
            raise ValidationError('A department with this code already exists.')
        return code


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['name', 'year', 'start_date', 'end_date', 'is_active']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and end_date <= start_date:
            raise ValidationError('Semester end date must be after its start date.')

        if cleaned_data.get('is_active'):
            existing = Semester.objects.filter(is_active=True).exclude(pk=self.instance.pk)
            if existing.exists():
                raise ValidationError('Only one semester can be active at a time.')

        return cleaned_data


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'title', 'credits', 'department', 'semester', 'description']

    def clean_code(self):
        code = self.cleaned_data.get('code', '').strip().upper()
        if Course.objects.filter(code=code).exclude(pk=self.instance.pk).exists():
            raise ValidationError('A course with this code already exists.')
        return code


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_id',
            'first_name',
            'last_name',
            'email',
            'department',
            'enrollment_year',
            'current_semester',
            'date_of_birth',
            'phone',
            'status',
        ]

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id', '').strip().upper()
        if Student.objects.filter(student_id=student_id).exclude(pk=self.instance.pk).exists():
            raise ValidationError('A student with this ID already exists.')
        return student_id

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError('A student with this email already exists.')
        return email


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['student', 'course', 'semester', 'grade']

    def clean(self):
        cleaned_data = super().clean()
        course = cleaned_data.get('course')
        semester = cleaned_data.get('semester')

        if course and semester and course.semester != semester:
            raise ValidationError('Selected course must be offered in the chosen semester.')

        return cleaned_data
