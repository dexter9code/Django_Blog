from django.shortcuts import render, HttpResponse, get_object_or_404
from datetime import date
from .models import Post


def index(request):
    posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {
        "posts": posts
    })


def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all_posts.html', {
        'all_posts': all_posts
    })


def post(request, slug):
    needed_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {
        'post': needed_post,
        'post_tags': needed_post.tags.all()
    })
