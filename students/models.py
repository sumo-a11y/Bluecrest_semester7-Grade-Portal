from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=120, unique=True)
    code = models.CharField(max_length=10, unique=True)
    faculty = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return f'{self.code} - {self.name}'

    def get_absolute_url(self):
        return reverse('students:department-detail', args=[self.pk])


class Semester(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)

    class Meta:
        unique_together = [('name', 'year')]
        ordering = ['-year', 'name']

    def __str__(self):
        return f'{self.name} {self.year}'

    def get_absolute_url(self):
        return reverse('students:semester-detail', args=[self.pk])


class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    credits = models.PositiveSmallIntegerField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='courses')
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT, related_name='courses')
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return f'{self.code} - {self.title}'

    def get_absolute_url(self):
        return reverse('students:course-detail', args=[self.pk])


class Student(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('graduated', 'Graduated'),
    ]

    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='students')
    enrollment_year = models.PositiveSmallIntegerField()
    current_semester = models.ForeignKey(Semester, on_delete=models.PROTECT, related_name='students')
    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['student_id']

    def __str__(self):
        return f'{self.student_id} - {self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('students:student-detail', args=[self.pk])


class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='registrations')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='registrations')
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT, related_name='registrations')
    registered_on = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=4, blank=True)

    class Meta:
        unique_together = [('student', 'course', 'semester')]
        ordering = ['-registered_on']

    def __str__(self):
        return f'{self.student} → {self.course} ({self.semester})'

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.course.semester != self.semester:
            raise ValidationError('Course semester must match registration semester.')

    def get_absolute_url(self):
        return reverse('students:registration-detail', args=[self.pk])
