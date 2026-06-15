from django.urls import reverse_lazy
from django.views import generic

from .forms import CourseForm, DepartmentForm, RegistrationForm, SemesterForm, StudentForm
from .models import Course, Department, Registration, Semester, Student


class MultiButtonFormMixin:
    def get_success_url(self):
        if '_addanother' in self.request.POST:
            return reverse_lazy(f'students:{self.model._meta.model_name}-create')
        if '_continue' in self.request.POST:
            return reverse_lazy(
                f'students:{self.model._meta.model_name}-update',
                kwargs={'pk': self.object.pk}
            )
        return reverse_lazy(f'students:{self.model._meta.model_name}-list')


class DepartmentListView(generic.ListView):
    model = Department
    template_name = 'students/object_list.html'


class DepartmentDetailView(generic.DetailView):
    model = Department
    template_name = 'students/object_detail.html'


class DepartmentCreateView(MultiButtonFormMixin, generic.CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'students/object_form.html'


class DepartmentUpdateView(MultiButtonFormMixin, generic.UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'students/object_form.html'


class DepartmentDeleteView(generic.DeleteView):
    model = Department
    success_url = reverse_lazy('students:department-list')
    template_name = 'students/object_confirm_delete.html'


class SemesterListView(generic.ListView):
    model = Semester
    template_name = 'students/object_list.html'


class SemesterDetailView(generic.DetailView):
    model = Semester
    template_name = 'students/object_detail.html'


class SemesterCreateView(MultiButtonFormMixin, generic.CreateView):
    model = Semester
    form_class = SemesterForm
    template_name = 'students/object_form.html'


class SemesterUpdateView(MultiButtonFormMixin, generic.UpdateView):
    model = Semester
    form_class = SemesterForm
    template_name = 'students/object_form.html'


class SemesterDeleteView(generic.DeleteView):
    model = Semester
    success_url = reverse_lazy('students:semester-list')
    template_name = 'students/object_confirm_delete.html'


class CourseListView(generic.ListView):
    model = Course
    template_name = 'students/object_list.html'


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'students/object_detail.html'


class CourseCreateView(MultiButtonFormMixin, generic.CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'students/object_form.html'


class CourseUpdateView(MultiButtonFormMixin, generic.UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'students/object_form.html'


class CourseDeleteView(generic.DeleteView):
    model = Course
    success_url = reverse_lazy('students:course-list')
    template_name = 'students/object_confirm_delete.html'


class StudentListView(generic.ListView):
    model = Student
    template_name = 'students/object_list.html'


class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'students/object_detail.html'


class StudentCreateView(MultiButtonFormMixin, generic.CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/object_form.html'


class StudentUpdateView(MultiButtonFormMixin, generic.UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/object_form.html'


class StudentDeleteView(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('students:student-list')
    template_name = 'students/object_confirm_delete.html'


class RegistrationListView(generic.ListView):
    model = Registration
    template_name = 'students/object_list.html'


class RegistrationDetailView(generic.DetailView):
    model = Registration
    template_name = 'students/object_detail.html'


class RegistrationCreateView(MultiButtonFormMixin, generic.CreateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'students/object_form.html'


class RegistrationUpdateView(MultiButtonFormMixin, generic.UpdateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'students/object_form.html'


class RegistrationDeleteView(generic.DeleteView):
    model = Registration
    success_url = reverse_lazy('students:registration-list')
    template_name = 'students/object_confirm_delete.html'
