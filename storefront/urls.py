import debug_toolbar
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    path("", include("core.urls")),
    path("admin/", admin.site.urls),
    path("playground/", include("playground.urls")),
    path("store/", include("store.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include("djoser.social.urls")),
    path("__debug__/", include(debug_toolbar.urls)),
]

urlpatterns += [re_path(r"^.*", TemplateView.as_view(template_name="index.html"))]
