# BLECREST Grade Portal — Summaries

## Brief Summary

- **What:** A Django-based grade portal for BLECREST semester 7 that manages departments, semesters, courses, students, registrations, and grades.
- **How to run:** Activate the virtualenv and run `python manage.py runserver`.

## Normal Summary

- **Overview:** This repository is a Django project (configured in `config/settings.py`) using SQLite (`db.sqlite3`) for development. The main domain logic lives in the `students` app (`students/models.py`) which defines `Department`, `Semester`, `Course`, `Student`, and `Registration`. Other apps (`courses`, `grades`, `lecturers`, `reports`) currently contain placeholders.
- **Primary user flows:** Admins create/manage departments, semesters, courses, and student records; register students into courses; and enter/export grades. Students and lecturers view profiles, registrations, and grades where implemented.
- **Docs:** See the full project doc [PROJECT_DOCUMENTATION.md](PROJECT_DOCUMENTATION.md) and the user-facing guide [USER_GUIDE.md](USER_GUIDE.md).

## Detailed Summary (Key points)

- **Technology:** Django 6.x, Python (virtualenv at `gradeportalenv/`), SQLite for development.

- **Data model highlights:**
  - `Department`: name/code, groups courses and students.
  - `Semester`: name, year, active flag; unique per (name, year).
  - `Course`: code, title, credits, FK -> `Department`, `Semester`.
  - `Student`: `student_id`, contact info, FK -> `Department`, `current_semester`.
  - `Registration`: links `Student` + `Course` + `Semester`, enforces uniqueness and semester consistency.

- **Admin access:** Uses Django auth; account `bluecrest@2025` was added as a superuser for development (see docs).

- **How to inspect/manage:** Use `manage.py shell` for scripted changes, `manage.py migrate` for DB, and admin UI at `/admin/`.

- **Next recommendations:** add model docstrings, fill in other app models, add automated tests, and create PDF exports of the docs (I can generate PDFs if you want).

---

Generated: 2026-06-11
