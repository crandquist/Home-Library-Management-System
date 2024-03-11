# django_project/urls.py
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
    path('library/', include(('library_app.urls', 'library_app'), namespace='library_app')),
    path('reading-log/', include(('reading_log.urls', 'reading_log'), namespace='reading_log')),
    path('search/', include(('search.urls', 'search'))),  # Update this line
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
