from django.urls import path, re_path
from django.contrib.sitemaps.views import sitemap

from .sitemaps import PostSitemap
from .feeds import LatestPostsFeed
from . import views

sitemaps = {
    'posts': PostSitemap,
}
urlpatterns = [


    re_path(r'^category/(?P<category_slug>[-\w]+)/$', views.post_by_category, name='post_by_category'),
    re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_by_tag, name='post_by_tag'),
    re_path(r'^(?P<pk>\d+)/(?P<post_slug>[-\w]+)$', views.post_detail, name='post_detail'),
    re_path(r'^blog/comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    re_path(r'^blog/comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    re_path(r'^(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^sitemap\.xml/$', sitemap, {'sitemaps' : sitemaps } , name='sitemap'),
    re_path(r'^feed/$', LatestPostsFeed(), name='post_feed'),
    path('', views.blog_home, name='blog_home'),
]
