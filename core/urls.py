from django.views.generic import TemplateView
from django.urls import path
from django.http import JsonResponse


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("", TemplateView.as_view(template_name="core/index.html")),
    path("health/", health),
]
