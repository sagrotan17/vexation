from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from .models import Post

class LatestPostsFeed(Feed):
    title = 'Vexation Blog Feeds'
    link = '/blog/'
    description = 'New Posts of the blogs'

    def items(self):
        return Post.published_objects.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)