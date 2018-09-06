from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.urls import reverse             # bis Django 1.11: from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
# vexFINAL1.1/vexation/blog/models.py

# Custom Manager:
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

def video_dir_path(instance, filename):
    return 'video_{0}/{1}'.format(instance.category_id, filename)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True,
                            help_text="Slug will be generated automatically from the name of the Category")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    width = models.PositiveIntegerField(default=0)
    height = models.PositiveIntegerField(default=0)
    starter_image_cat = models.ImageField(upload_to='starterImages', null=False, blank=False, width_field="width",
                                      height_field="height")
    link_starter_image = models.CharField(max_length=200, blank=True)
    description = RichTextUploadingField(default="nothing", blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_by_category', args=[self.slug])
    # ggf. unter 2.0 probieren:
        #return reverse('post_by_category', args=[str(self.slug)])



class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True,
                            help_text="Slug will be generated automatically from the name of the Tag")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_by_tag', args=[self.slug])

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,
                            help_text="Slug will be generated automatically from the title of the post")
    content = RichTextUploadingField()
    width = models.PositiveIntegerField(default=0)
    height = models.PositiveIntegerField(default=0)
    starter_image_post = models.ImageField(upload_to='starterImages', null=False, blank=False, width_field="width",
                                      height_field="height")
    link_starter_image = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to=video_dir_path, default="Sorry, es gibt kein Video zum Post", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    link = models.CharField(max_length=200, blank=True)

    # The default Manager:
    objects = models.Manager()

    # Custom made Manager:
    published_objects = PublishedManager()

    class Meta:
        ordering = ('-published_at',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id, self.slug])

# Comment class for comments in posts:
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    # returns the user to the main 'posts/' page (this is the named url) :
    def get_absolute_url(self):
        return reverse('blog:home')

    def __str__(self):
        return self.text