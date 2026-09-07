from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from django.urls import reverse
from .forms import ContactForm, PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import Q, F, Count


def home(request):
    return HttpResponse("hello world")


def post_list(request):
    posts = (
        Post.objects.select_related("author", "category")
        .prefetch_related("tags")
        .filter(Q(is_published=True) & (Q(title__icontains="پست") | Q(content__icontains="پست")))
        .annotate(comment_count=Count("comments"))
        .order_by("-created_at")
    )
    post_counts = Post.objects.aggregate(post_counts=Count("id"))
    print(post_counts)
    # posts = Post.objects.filter(is_published=True).order_by("-created_at")
    for post in posts:
        print(post.comment_count)

    context = {"posts": posts, "title": "لیست پست ها", "post_counts": post_counts["post_counts"]}
    return render(request, "blog/post_list.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    Post.objects.filter(pk=post.pk).update(views=F("views") + 1)
    comments = post.comments.filter(is_approved=True)
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        

    post.refresh_from_db()
    context = {
        "post": post,
        "comments": comments,
        "comment_form": comment_form,
        "path": reverse("blog:post_detail", args=[post.pk]),
    }

    return render(request, "blog/blog_detail.html", context=context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            return redirect("blog:post_list")
    else:
        form = ContactForm()
    return render(request, "blog/contact.html", {"form": form})


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog:post_list")
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form, "action": "ساخت"})


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == "POST":

        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, "blog/post_form.html", {"form": form, "action": "ویرایش"})
