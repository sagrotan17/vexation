from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required


from vexation import helpers
from .models import Tag, Category, Post, Comment
from .forms import CommentForm



# Create your views here.
# view function to display a list of posts
def blog_home(request):
    categories = get_list_or_404(Category)
    return render(request, 'blog/blog_home.html', {'categories': categories})

def post_list(request):
    posts = Post.published_objects.order_by("-id").all()    # Custom Manger for 'published objecs'
    # paginator is in separate file to use it projectwide. It is imported as 'helpers':
    posts = helpers.pg_records(request, posts, 4)
    return render(request, 'blog/post_list.html', {'posts': posts})


# view function to display a single post
def post_detail(request, pk, post_slug):
    post = get_object_or_404(Post, status='published', pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# view function to display post by category
def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = get_list_or_404(Post.published_objects.order_by("-id"), category=category)
    posts = helpers.pg_records(request, posts, 5)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/post_by_category.html', context)


# view function to display post by tag
def post_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    #posts = get_list_or_404(Post, tags=tag)
    posts = get_list_or_404(Post.published_objects.order_by("-id"), tags=tag)
    posts = helpers.pg_records(request, posts, 5)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/post_by_tag.html', context )


def test_redirect(request):
    return redirect('post_list', permanent=True)


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
           # human=True     #for simple captcha
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            #return redirect('techblog_list')
            return render(request, 'blog/successmessage.html')
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog_detail', pk=comment.post.pk)
