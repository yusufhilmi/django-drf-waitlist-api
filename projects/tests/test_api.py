from django.test import TestCase
from django.urls import resolve, reverse


class APITests(TestCase):
    def test_url(self):
        assert (
            reverse("waiter-create")
            == "/"
        )
        assert resolve("/").view_name == "waiter-create"
