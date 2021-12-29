from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import Permission

from ..models import Subject, Course


class CourseUpdateTest(TestCase):
    def setUp(self):
        number_of_courses = 5
        self.owner = User.objects.create(
            username="tester",
            email="abc1@gmail.com",
            first_name="t",
            last_name="u",
            password="Qwer43@1",
        )
        self.owner.user_permissions.add(Permission.objects.get(codename="add_course"))
        subject = Subject.objects.create(title="testing", slug="test")

        for course in range(number_of_courses):
            Course.objects.create(
                owner=self.owner,
                subject=subject,
                title="Django testing",
                slug=f"Django testing {course}",
                overview="testing in django",
            )
        self.url = reverse("course_create")

    def test_only_instructor_can_create_course(self):
        self.client.force_login(self.owner)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
