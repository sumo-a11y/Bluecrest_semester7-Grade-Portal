# BLECREST Grade Portal — User Guide

This guide explains how to use the Grade Portal from the perspective of common users: Administrators (staff/superuser), Lecturers, and Students.

---

## Quick start (for everyone)

1. Ensure the development server is running locally (or use your deployed URL):

```powershell
& .\gradeportalenv\Scripts\Activate.ps1
python manage.py runserver
```

2. Open the site in a browser, e.g. `http://127.0.0.1:8000/`.
3. Admin site: `http://127.0.0.1:8000/admin/`.

---

## Roles & permissions

- Administrator (superuser / staff): full access to the Django admin site and high-level management (create/edit/delete students, courses, semesters, registrations, users, and reports).
- Lecturer (staff): typically can view/manage course assignments and enter grades (depends on app implementation and permissions).
- Student: can view their profile, registered courses, and grades (if the site exposes these pages).

Access to admin requires `is_active=True` and `is_staff=True` (superusers also have `is_superuser=True`).

---

## Logging in

- Admins and staff: use the Django admin login at `/admin/`.
- Students and lecturers: use the site login page if one exists (check the project URLs) or authenticate through the admin for account creation.

If you cannot log in:
- Confirm username and password are entered exactly (case-sensitive).
- Verify the server is using the same `db.sqlite3` where your account exists.
- Use the shell to inspect the user flags (see Troubleshooting below).

---

## Administrator (common tasks)

1. Create a user (via admin): Admin → Users → Add user. Fill username, password, and set `is_staff` or `is_superuser` as needed.

2. Manage departments/semesters/courses:
   - Departments: create `Department` entries (name, code, faculty).
   - Semesters: create `Semester` with `name`, `year`, `start_date`, `end_date`. Mark the active semester with `is_active=True`.
   - Courses: create `Course` entries and link to `Department` and `Semester`.

3. Create and manage students:
   - In admin, add `Student` records with `student_id`, names, email, `department`, `enrollment_year`, and `current_semester`.

4. Registrations (enrolling students in courses):
   - In admin, add `Registration` linking a `Student` to a `Course` and `Semester`. Note the system enforces uniqueness per `(student, course, semester)`.

5. Enter or edit grades:
   - Update the `Registration` record's `grade` field for each student-course entry.

6. Generate reports:
   - Use the `reports` app or admin export features (if implemented) to produce student or grade reports.

---

## Lecturer (common tasks)

- View assigned courses (check `Course` listings or custom lecturer views).
- Enter grades (if a lecturer-facing UI exists) or ask an admin to grant access to the admin site.
- Export course rosters or grade sheets if the app provides reporting tools.

---

## Student (common tasks)

- View profile and current semester details.
- View registered courses and grades (if the site exposes these pages).
- Contact administrators for corrections (e.g., wrong email, missing registration).

---

## URLs & pages to know

- Home: `/`
- Admin: `/admin/`
- Students list/detail/registration pages: typically namespaced under `students` (check `students/urls.py`).
- Login/logout: check `config/urls.py` for authentication routes.

---

## Troubleshooting common issues

1. Cannot log in:
   - Run the following to inspect the user (using the project virtualenv):

```powershell
gradeportalenv\Scripts\python.exe manage.py shell -c "from django.contrib.auth import get_user_model; U=get_user_model(); u=U.objects.filter(username='bluecrest@2025').first(); print(u, getattr(u,'is_active',None), getattr(u,'is_staff',None), getattr(u,'is_superuser',None))"
```

2. Authentication fails despite correct password:
   - Verify the `authenticate()` function works in the shell:

```powershell
gradeportalenv\Scripts\python.exe manage.py shell -c "from django.contrib.auth import authenticate; print(authenticate(username='bluecrest@2025', password='Semester7'))"
```

If that returns `None`, there may be a custom auth backend or the password wasn't set in the active database.

3. Data not present on site:
   - Confirm the same `db.sqlite3` is used by the running server and the shell commands.
   - Check migrations were applied: `python manage.py migrate`.

---

## Administrator: emergency account commands

- Create a superuser from the shell:

```powershell
python manage.py createsuperuser
```

- Create/update a user programmatically (example used in support):

```powershell
python manage.py shell -c "from django.contrib.auth import get_user_model; U=get_user_model(); u,created=U.objects.get_or_create(username='bluecrest@2025', defaults={'email':'gbanyansumo25@gmail.com'}); u.email='gbanyansumo25@gmail.com'; u.is_active=True; u.is_staff=True; u.is_superuser=True; u.set_password('Semester7'); u.save(); print('CREATED' if created else 'UPDATED')"
```

Use that pattern only on development systems. Do not commit secrets to source control.

---

## Support & next steps

- If you want role-specific walkthroughs (screenshots or step-by-step admin clicks), tell me which role to document and I'll expand the guide.
- I can also produce a PDF version of this guide—shall I generate `USER_GUIDE.pdf` now?

---

Generated: 2026-06-11
