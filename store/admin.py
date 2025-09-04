from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


class InventoryFilter(admin.SimpleListFilter):
    title = "inventory"
    parameter_name = "inventory"

    low_filter = "<10"
    high_filter = ">=10"

    def lookups(self, request, model_admin):
        return [(self.low_filter, "Low Stock"), (self.high_filter, "In Stock")]

    def queryset(self, request, queryset):
        if self.value() == self.low_filter:
            return queryset.filter(inventory__lt=10)
        if self.value() == self.high_filter:
            return queryset.filter(inventory__gte=10)
        return queryset


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ["collection"]
    prepopulated_fields = {"slug": ["title"]}
    search_fields = ["title"]
    actions = ["clear_inventory"]
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price"]
    list_filter = ["collection", "last_updated", InventoryFilter]
    list_per_page = 10
    list_select_related = ["collection"]

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory < 10:
            return "Low Stock"
        return "In Stock"

    def collection_title(self, product):
        return product.collection.title

    @admin.action(description="Clear Inventory")
    def clear_inventory(self, request, queryset):
        updated_inventory = queryset.update(inventory=0)
        self.message_user(
            request, f"{updated_inventory} products were successfully updated."
        )


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "product_count"]
    search_fields = ["title"]

    @admin.display(ordering="product_count")
    def product_count(self, collection):
        url = (
            reverse("admin:store_product_changelist")
            + "?"
            + urlencode({"collection__id": str(collection.id)})
        )
        return format_html("<a href = '{}'>{}</a>", url, collection.product_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(product_count=Count("products"))


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership", "order_number"]
    list_editable = ["membership"]
    list_per_page = 10
    search_fields = ["first_name__istartswith", "last_name__istartswith"]
    ordering = ["first_name", "last_name"]

    @admin.display(ordering="order_number")
    def order_number(self, customer):
        url = (
            reverse("admin:store_order_changelist")
            + "?"
            + urlencode({"customer__id": str(customer.id)})
        )
        return format_html("<a href = '{}'>{} Orders</a>", url, customer.order_number)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(order_number=Count("order"))


class OrderItemInline(admin.StackedInline):
    autocomplete_fields = ["product"]
    model = models.OrderItem
    min_num = 1
    max_num = 10
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ["customer"]
    inlines = [OrderItemInline]
    list_display = ["id", "payment_status", "placed_at", "customer_name"]
    # ordering = ["-placed_at"]
    list_per_page = 10
    list_select_related = ["customer"]

    def customer_name(self, order):
        return f"{order.customer.first_name} {order.customer.last_name}"
