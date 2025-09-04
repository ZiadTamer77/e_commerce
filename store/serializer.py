from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title", "products_count"]

    products_count = serializers.IntegerField()

    # products_count = serializers.SerializerMethodField(method_name="get_products_count")

    # def get_products_count(self, collection: Collection):
    #     return collection.products.count()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "slug",
            "inventory",
            "unit_price",
            "price_with_tax",
            "collection",
        ]

    price_with_tax = serializers.SerializerMethodField(method_name="get_price_with_tax")

    def get_price_with_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
