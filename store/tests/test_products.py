from rest_framework import status
from store.models import Product, Collection
from model_bakery import baker
import pytest


@pytest.mark.django_db
class TestProductsList:
    def test_products_list_with_proper_pagination(self, api_client):
        baker.make(Product, _quantity=20)

        response = api_client.get("/store/products/")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 20
        assert response.data["previous"] is None
        assert response.data["next"] == "http://testserver/store/products/?page=2"
        assert len(response.data["results"]) == 10

    def test_products_lists_per_collections_return_200(self, api_client):
        collection = baker.make(Collection)
        baker.make(Product, _quantity=20, collection=collection)

        response = api_client.get(f"/store/products/?collection_id={collection.id}")

        assert response.status_code == status.HTTP_200_OK
