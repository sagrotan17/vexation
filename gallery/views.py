from django.shortcuts import render,get_object_or_404, get_list_or_404, reverse, redirect

from vexation import helpers
from .models import Photo, Gallery, Category, Tag


def gallery_home(request):
    categories = get_list_or_404(Category)
    return render(request, 'gallery/gallery_home.html', {'categories': categories})

def gallery_list(request):
    galleries = Gallery.is_public_objects.order_by("-id").all() # Custom manager for public objects
    # Paginator is in helpers.py. So it could be used projectwide. It is imported as 'helpers':
    galleries = helpers.pg_records(request, galleries, 4)
    return render(request, 'gallery/gallery_list.html', {"galleries": galleries})

def gallery_detail(request, pk, gallery_slug):
    gallery = get_object_or_404(Gallery, is_public='True', pk=pk, slug=gallery_slug)
    queryset = Photo.objects.filter(gallery=gallery)
    context = {"photos": queryset, "gallery": gallery}

    return render(request, 'gallery/gallery_detail.html', context)



# view function to display gallery by category
def gallery_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    galleries = get_list_or_404(Gallery.is_public_objects.order_by("-id"), category=category)
    # Paginator is in helpers.py. So it could be used projectwide. It is imported as 'helpers':
    galleries = helpers.pg_records(request, galleries, 4)
    context = {
        'category': category,
        'galleries': galleries
    }
    return render(request, 'gallery/gallery_by_category.html', context)
