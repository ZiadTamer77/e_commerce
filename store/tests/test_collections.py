from rest_framework import status
from store.models import Collection, Product
from model_bakery import baker
import pytest


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post("/store/collections/", collection)

    return do_create_collection


@pytest.fixture
def delete_collection(api_client):
    def do_delete_collection(collection):
        return api_client.delete(f"/store/collections/{collection.id}/")

    return do_delete_collection


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self, create_collection):
        response = create_collection({"title": "a"})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, create_collection, auth_user):
        auth_user()

        response = create_collection({"title": "a"})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_return_400(self, create_collection, auth_user):
        auth_user(is_staff=True)

        response = create_collection({"title": ""})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["title"] is not None

    def test_if_data_is_valid_return_201(self, create_collection, auth_user):
        auth_user(is_staff=True)

        response = create_collection({"title": "a"})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] > 0


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_return_200(self, api_client):
        collection = baker.make(Collection)

        response = api_client.get(f"/store/collections/{collection.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "id": collection.id,
            "title": collection.title,
            "products_count": 0,
        }


@pytest.mark.django_db
class TestDeleteCollection:
    def test_delete_collection_with_products_returns_405(
        self, auth_user, delete_collection
    ):
        auth_user(is_staff=True)
        collection = baker.make(Collection)
        baker.make(Product, collection=collection)

        response = delete_collection(collection)

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_user_is_not_admin_returns_403(self, auth_user, delete_collection):
        auth_user()
        collection = baker.make(Collection)

        response = delete_collection(collection)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_anonymous_return_401(self, delete_collection):
        collection = baker.make(Collection)

        response = delete_collection(collection)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_delete_works_returns_204(self, delete_collection, auth_user):
        auth_user(is_staff=True)
        collection = baker.make(Collection)

        response = delete_collection(collection)

        assert response.status_code == status.HTTP_204_NO_CONTENT
