from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import Permission

from ..models import Subject, Course, Module


class CourseUpdateTest(TestCase):
    def setUp(self):
        self.owner = User.objects.create(
            username="tester",
            email="abc1@gmail.com",
            first_name="t",
            last_name="u",
            password="Qwer43@1",
        )
        self.owner.user_permissions.add(
            Permission.objects.get(codename="change_course")
        )
        subject = Subject.objects.create(title="testing", slug="test")

        course = Course.objects.create(
            owner=self.owner,
            subject=subject,
            title="Django testing",
            slug="django-testing",
            overview="testing in django",
        )
        Module.objects.create(
            course=course, title="introduction", description="Introduction to testing"
        )
        self.url = reverse("course_module_update", args=[1])

    def test_module_update_page_should_return_status_code_200(self):
        self.client.force_login(self.owner)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
