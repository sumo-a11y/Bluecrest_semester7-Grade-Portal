# BLECREST Grade Portal — Project Documentation

## Overview

A Django-based grade portal for BLECREST semester 7. Core apps: `students`, `courses`, `grades`, `lecturers`, `reports`, `resources`, `accounts`. The project uses SQLite for development (`db.sqlite3`).

## Quick facts

- Django version (bundled in venv): 6.0.x
- Python: project virtualenv at `gradeportalenv/`
- Database: SQLite (`db.sqlite3`)

## Repository layout

- `manage.py` — Django management wrapper
- `config/` — project configuration (`settings.py`, `urls.py`, `wsgi.py`, `asgi.py`)
- `accounts/`, `students/`, `courses/`, `grades/`, `lecturers/`, `reports/`, `resources/` — Django apps
- `templates/` — global templates
- `requirements.txt` — declared dependencies
- `gradeportalenv/` — local virtual environment (not for production)

## Setup (local development)

1. Activate virtualenv (PowerShell):

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
& .\gradeportalenv\Scripts\Activate.ps1
```

2. Install dependencies (if you need to):

```powershell
pip install -r requirements.txt
```

3. Apply migrations:

```powershell
python manage.py migrate
```

4. Create a superuser (if needed):

```powershell
python manage.py createsuperuser
```

5. Run the development server:

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ and http://127.0.0.1:8000/admin/.

## The user account (created during support session)

- Username: `bluecrest@2025`
- Email: `gbanyansumo25@gmail.com`
- Password: `Semester7`
- Current status: `is_active=True`, `is_staff=True`, `is_superuser=True`

Notes: these credentials were added/updated directly in the development SQLite database during support. Change the password after first login for security.

## Key configuration files

- `config/settings.py` — check `INSTALLED_APPS`, `DATABASES`, `STATICFILES_DIRS`, and `TEMPLATES`.
- `students/` — contains templates and `templatetags/model_extras.py` used by the frontend.

## Architecture & Models (detailed)

The core domain logic is implemented in the `students` app. Other apps (`courses`, `grades`, `lecturers`, `reports`) currently have no models defined in `models.py` and act as placeholders or contain logic elsewhere.

`students.models` summary:

- `Department` — administrative grouping for courses and students. Fields: `name`, `code`, `faculty`, `description`.
- `Semester` — academic period with `name`, `year`, `start_date`, `end_date`, and `is_active` flag. Unique on `(name, year)`.
- `Course` — course catalog entry with `code`, `title`, `credits`, foreign keys to `Department` and `Semester`, and `description`.
- `Student` — student record with `student_id`, `first_name`, `last_name`, `email`, `department`, `enrollment_year`, `current_semester`, `date_of_birth`, `phone`, `status` (active/inactive/graduated), and `created_at`.
- `Registration` — enrollment linking `Student` to `Course` for a `Semester`, with `registered_on` and optional `grade`. Enforces uniqueness per `(student, course, semester)` and validates the course semester matches the registration semester.

Relationships & constraints:

- `Course` -> `Department` (PROTECT)
- `Course` -> `Semester` (PROTECT)
- `Student` -> `Department` (PROTECT)
- `Student` -> `Semester` (current_semester, PROTECT)
- `Registration` links `Student`, `Course`, and `Semester` and enforces integrity via `unique_together` and `clean()` checks.

If you want, I can extract field lists for other apps or generate ER diagrams from these models.

## Apps & important files

- `accounts/models.py` — currently empty placeholder (project uses Django's default user model).
- `students/models.py`, `courses/models.py`, `grades/models.py`, `lecturers/models.py`, `reports/models.py` — primary domain models (review each app for field-level documentation).
- `templates/students/` — includes base and CRUD templates:
  - `base.html`
  - `object_list.html`, `object_detail.html`, `object_form.html`, `object_confirm_delete.html`

## Admin access

The admin site is available at `/admin/`. The created account `bluecrest@2025` is a superuser and can access the admin.

If you prefer to create/manage admin accounts through the shell instead, use:

```powershell
python manage.py shell
# then:
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('username', 'email@example.com', 'password')
```

## Running checks and tests

Run Django checks and the test suite:

```powershell
python manage.py check
python manage.py test
```

## Troubleshooting login issues

- Ensure server uses the same `db.sqlite3` file where the user was created.
- Confirm `is_active` and `is_staff` / `is_superuser` flags via shell.
- Verify no custom authentication backend overrides the username/email behavior (check `config/settings.py`).

## How to export this documentation to PDF locally

If `pandoc` is installed, run:

```powershell
pandoc PROJECT_DOCUMENTATION.md -o PROJECT_DOCUMENTATION.pdf
```

Or with Python and `markdown` + `weasyprint` (if installed):

```powershell
pip install markdown weasyprint
python - <<'PY'
import markdown, weasyprint
html = markdown.markdown(open('PROJECT_DOCUMENTATION.md', 'r', encoding='utf-8').read())
weasyprint.HTML(string=html).write_pdf('PROJECT_DOCUMENTATION.pdf')
PY
```

If you're unable to convert locally, I can attempt to generate the PDF here; tell me if you want me to try.

## Notes & next steps

- Consider adding inline docstrings to models and views for automatic API docs generation.
- Add a CONTRIBUTING.md and developer guide if collaborators will join.

---

Generated by support session on 2026-06-11.
