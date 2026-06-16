from django.urls import path

from . import views

app_name = 'students'

urlpatterns = [
    path('', views.StudentListView.as_view(), name='student-list'),
    path('student/create/', views.StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('student/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student-update'),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),

    path('departments/', views.DepartmentListView.as_view(), name='department-list'),
    path('departments/create/', views.DepartmentCreateView.as_view(), name='department-create'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department-detail'),
    path('departments/<int:pk>/edit/', views.DepartmentUpdateView.as_view(), name='department-update'),
    path('departments/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department-delete'),

    path('semesters/', views.SemesterListView.as_view(), name='semester-list'),
    path('semesters/create/', views.SemesterCreateView.as_view(), name='semester-create'),
    path('semesters/<int:pk>/', views.SemesterDetailView.as_view(), name='semester-detail'),
    path('semesters/<int:pk>/edit/', views.SemesterUpdateView.as_view(), name='semester-update'),
    path('semesters/<int:pk>/delete/', views.SemesterDeleteView.as_view(), name='semester-delete'),

    path('courses/', views.CourseListView.as_view(), name='course-list'),
    path('courses/create/', views.CourseCreateView.as_view(), name='course-create'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:pk>/edit/', views.CourseUpdateView.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course-delete'),

    path('registrations/', views.RegistrationListView.as_view(), name='registration-list'),
    path('registrations/create/', views.RegistrationCreateView.as_view(), name='registration-create'),
    path('registrations/<int:pk>/', views.RegistrationDetailView.as_view(), name='registration-detail'),
    path('registrations/<int:pk>/edit/', views.RegistrationUpdateView.as_view(), name='registration-update'),
    path('registrations/<int:pk>/delete/', views.RegistrationDeleteView.as_view(), name='registration-delete'),
]
