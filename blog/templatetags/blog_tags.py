from django import template
from django.db.models import Count
import random


register = template.Library()

from ..models import Post



# Tag to create random Fador for Bootstrap Cards
@register.simple_tag
def fader():
    faderValues = ["fadeIn-bottom", "fadeIn-top", "fadeIn-left", "fadeIn-right","fadeIn-top fadeIn-left", "fadeIn-top fadeIn-right", "fadeIn-bottom fadeIn-left", "fadeIn-bottom fadeIn-right"]
    f = random.choice(faderValues)
    return f

@register.simple_tag(name = 'count_total_posts')
def total_posts():
    return Post.published_objects.count()   # use of the customed manager

@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published_objects.order_by('-published_at')[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published_objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

@register.simple_tag
def get_latest_posts(count=5):
    return Post.published_objects.order_by('-published_at')[:count]