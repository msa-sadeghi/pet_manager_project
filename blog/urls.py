from django.urls import path
from .views import contact, PostListView, PostDetailView, PostCreateView, PostUpdateView

app_name = "blog"
urlpatterns = [
    # path("", post_list, name="post_list"),
    path("", PostListView.as_view(), name="post_list"),
    path("post_create", PostCreateView.as_view(), name="post_create"),
    # path("post_create", post_create, name="post_create"),
    # path("post/<int:pk>/", post_detail, name="post_detail"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post_update"),
    path("contact/", contact, name="contact"),
]
