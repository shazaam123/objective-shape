from django.test import TestCase, Client
from django.contrib.auth.models import *
from django.urls import reverse
from .models import Student


class StudentTest(TestCase):
    def setup(self):
        self.client = Client()
        self.admin_user = objects.create_superuser(
            username='jobet9530',
            first_name='Jobet',
            last_name='Casquejo',
            email='jobetcasquejo221@gmail.com'
        )

    def add_student_test(self):
        response = self.client.post(reverse('student_add_view'), {
            'first_name': 'Test',
            'middle_initial': 'P',
            'last_name': 'Sample',
            'month': 'November'
        })
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Test')
