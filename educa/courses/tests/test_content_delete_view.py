from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import Permission
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import get_object_or_404

from ..models import Subject, Course, Module, Image


class CourseUpdateTest(TestCase):
    def setUp(self):
        self.owner = User.objects.create(
            username="tester",
            email="abc1@gmail.com",
            first_name="t",
            last_name="u",
            password="Qwer43@1",
        )
        self.owner.user_permissions.add(Permission.objects.get(codename="view_course"))
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
        img = SimpleUploadedFile("file.jpg", b"file_content")
        self.image = Image.objects.create(file=img, owner=self.owner, title="Image_1")
        self.url = reverse("module_content_delete", args=[1])

    def test_module_delete_content_should_delete_content(self):
        self.client.force_login(self.owner)
        response = self.client.get(self.url)
        self.assertContains(response, "Are you sure you want to remove")
