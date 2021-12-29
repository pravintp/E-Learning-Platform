from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import Permission

from ..models import Subject, Course


class CourseListTest(TestCase):
    def setUp(self):
        number_of_courses = 5
        self.owner = User.objects.create(
            username="tester",
            email="abc1@gmail.com",
            first_name="t",
            last_name="u",
            password="Qwer43@1",
        )
        self.owner.user_permissions.add(Permission.objects.get(codename="view_course"))
        subject = Subject.objects.create(title="testing", slug="test")

        for course in range(number_of_courses):
            Course.objects.create(
                owner=self.owner,
                subject=subject,
                title="Django testing",
                slug=f"Django testing {course}",
                overview="testing in django",
            )
        self.url = reverse("manage_course_list")

    def test_whether_course_list_view_returns_200_code(self):
        self.client.force_login(self.owner)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_anonymous_user_should_not_access_course_list(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
