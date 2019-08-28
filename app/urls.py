from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import RedirectView
"""Для использования редиректа"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
    # используем редирект на catalog/
    path('catalog/', include('catalog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

