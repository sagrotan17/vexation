from django.urls import path, re_path

from . import views
from .sitemaps import GallerySitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'galleries': GallerySitemap,
}

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/(?P<gallery_slug>[-\w]+)/$', views.gallery_detail, name = 'gallery_detail'),
    re_path(r'^category/(?P<category_slug>[-\w]+)/$', views.gallery_by_category, name='gallery_by_category'),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('', views.gallery_home, name='gallery_home'),
    ]