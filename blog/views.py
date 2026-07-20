from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.urls import reverse


def home(request):
    return HttpResponse("hello world")


def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by("-created_at")
    context = {"posts": posts, "title": "لیست پست ها"}
    return render(request, "blog/post_list.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, "blog/blog_detail.html", {"post": post, "path": reverse("blog:post_detail", args=[post.pk])})
