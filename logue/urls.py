"""logue URL Configuration"""
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logue/', include('feed.urls')),
    path('accounts/', include('allauth.urls')),
    path('', RedirectView.as_view(url='/logue', permanent=True)),
]
