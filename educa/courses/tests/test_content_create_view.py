from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import Permission
from io import BytesIO

from ..models import Subject, Course, Module, Image


class ContentCreateTest(TestCase):
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
        self.module = Module.objects.create(
            course=course, title="introduction", description="Introduction to testing"
        )
        self.url = reverse("module_content_create", args=[1, "image"])

    def test_content_create_view_should_create_content(self):
        self.client.force_login(self.owner)
        img = BytesIO(b"my_binary_data")
        img.name = "myimage.jpg"
        response = self.client.post(self.url, {"title": "image_1", "file": img})
        self.assertEqual(response.status_code, 200)
