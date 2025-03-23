from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("carapp.urls")),
    # path("carapp/", include("carapp.urls")),
    # path("", include("tailwindapp.urls")),
    # path("__reload__/", include("django_browser_reload.urls")),
]
