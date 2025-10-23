from rest_framework.test import APIClient
from django.contrib.auth.models import User
import pytest


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def auth_user(api_client):
    def take_user(is_staff=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff))

    return take_user
