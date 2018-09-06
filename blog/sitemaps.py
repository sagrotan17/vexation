from django.contrib.sitemaps import Sitemap
from django.utils import timezone
from .models import Post


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.published_objects.all()

    def lastmod(self, item):
        return item.published_at