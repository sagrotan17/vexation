
from django.db import models
# from django.core.urlresolvers import reverse # bis Django 1.11
from django.urls import reverse # ab Django 2.0
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# Custom Manager:
class IsPublicManager(models.Manager):
    def get_queryset(self):
        return super(IsPublicManager, self).get_queryset().filter(is_public='True')



def gal_dir_path(instance1, filename):
    return 'gallery_{0}/{1}'.format(instance1.gallery_id, filename)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True,
                                help_text="Slug will be generated automatically from the name of the Category")
    description = RichTextUploadingField(blank=True)
    width = models.PositiveIntegerField(default=0)
    height = models.PositiveIntegerField(default=0)
    starter_image_cat = models.ImageField(upload_to='starterImages', null=False, blank=False, width_field="width",
                                      height_field="height", default="starterImages/22.jpg")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('gallery_by_category', args=[self.slug])


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True,
                                help_text="Slug will be generated automatically from the name of the Tag")
    description = RichTextUploadingField(blank=True)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
       return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True,
                            help_text="Slug will be generated automatically from the name of the Gallery")

    year_pt = models.PositiveIntegerField(blank=True)
    month_pt = models.PositiveIntegerField(blank=True)
    info_link = models.URLField(default="No Link", blank=True)
    description = RichTextUploadingField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    width = models.PositiveIntegerField(default=0)
    height = models.PositiveIntegerField(default=0)
    starter_image = models.ImageField(upload_to='starterImages', null=False, blank=False, width_field="width",
                                      height_field="height",  default="starterImages/22.jpg")
    is_public = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    # The default Manager:
   # objects = models.Manager()

    # Custom made Manager from above:
    is_public_objects = IsPublicManager()

    class Meta:
        ordering = ['created_date',]
        verbose_name_plural = ('galleries')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Gallery, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('gallery_by_category', args=[self.slug])



class Photo(models.Model):
    title = models.CharField(max_length=200, blank=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

    image = models.ImageField(upload_to=gal_dir_path, null=False, blank=False, width_field="width", height_field="height")
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    is_public = models.BooleanField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    landscape_format = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["timestamp",]