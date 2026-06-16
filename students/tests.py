from django.test import TestCase
from django.urls import reverse

from .models import Department, Semester, Course


class MultiButtonFormTests(TestCase):
	def test_department_create_addanother_and_continue(self):
		url = reverse('students:department-create')
		data = {
			'name': 'Computer Science',
			'code': 'CS',
			'faculty': 'Engineering',
			'description': 'CS dept',
			'action': 'addanother',
		}
		resp = self.client.post(url, data)
		self.assertEqual(resp.status_code, 302)
		# add another should redirect back to create
		self.assertIn(reverse('students:department-create'), resp['Location'])

		# now test continue (should redirect to update for created pk)
		data2 = data.copy()
		data2['code'] = 'CS2'
		data2['name'] = 'Computer Science II'
		data2['action'] = 'continue'
		resp2 = self.client.post(url, data2)
		self.assertEqual(resp2.status_code, 302)
		dep = Department.objects.get(code='CS2')
		self.assertIn(reverse('students:department-update', kwargs={'pk': dep.pk}), resp2['Location'])

	def test_semester_create_addanother_and_continue(self):
		url = reverse('students:semester-create')
		data = {
			'name': 'Fall',
			'year': 2026,
			'start_date': '2026-09-01',
			'end_date': '2026-12-20',
			'is_active': False,
			'action': 'addanother',
		}
		resp = self.client.post(url, data)
		self.assertEqual(resp.status_code, 302)
		self.assertIn(reverse('students:semester-create'), resp['Location'])

		data2 = data.copy()
		data2['name'] = 'Autumn'
		data2['year'] = 2027
		data2['start_date'] = '2027-09-01'
		data2['end_date'] = '2027-12-20'
		data2['action'] = 'continue'
		resp2 = self.client.post(url, data2)
		self.assertEqual(resp2.status_code, 302)
		sem = Semester.objects.get(name='Autumn', year=2027)
		self.assertIn(reverse('students:semester-update', kwargs={'pk': sem.pk}), resp2['Location'])

	def test_course_create_addanother_and_continue(self):
		# create a department and semester first
		dep = Department.objects.create(name='Math', code='MTH')
		sem = Semester.objects.create(name='Spring', year=2026, start_date='2026-01-10', end_date='2026-05-15')
		url = reverse('students:course-create')
		data = {
			'code': 'MTH101',
			'title': 'Calculus I',
			'credits': 3,
			'department': dep.pk,
			'semester': sem.pk,
			'description': '',
			'action': 'addanother',
		}
		resp = self.client.post(url, data)
		self.assertEqual(resp.status_code, 302)
		self.assertIn(reverse('students:course-create'), resp['Location'])

		course = Course.objects.get(code='MTH101')
		data2 = data.copy()
		data2['code'] = 'MTH102'
		data2['title'] = 'Calculus II'
		data2['action'] = 'continue'
		resp2 = self.client.post(url, data2)
		self.assertEqual(resp2.status_code, 302)
		course2 = Course.objects.get(code='MTH102')
		self.assertIn(reverse('students:course-update', kwargs={'pk': course2.pk}), resp2['Location'])

