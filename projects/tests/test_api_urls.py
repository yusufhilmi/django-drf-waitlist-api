import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_post_waiter():
    assert (
        reverse("waiter-create")
        == "/"
    )
    assert resolve("/").view_name == "waiter-create"
