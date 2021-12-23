"""
URL Configuration for test-new-structure project.
The `urlpatterns` list routes URLs. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import permissions
from rest_framework.schemas import get_schema_view

from healthcheck import views

urlpatterns = [
    path("__health", views.health),
    path("api/v1/", include("h1st_api.urls")),
    path('openapi', get_schema_view(
        title="test-new-structure API",
        description="API layer for test-new-structure",
        public=True,
        permission_classes=[permissions.AllowAny],
    ), name='openapi-schema'),
    # Route TemplateView to serve the ReDoc template.
    #   * Provide `extra_context` with view name of `SchemaView`.
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),
]
