from django.contrib.sitemaps import Sitemap
from django.utils import timezone
from .models import Gallery


class GallerySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Gallery.is_public_objects.all()

    def lastmod(self, item):
        return item.created_date