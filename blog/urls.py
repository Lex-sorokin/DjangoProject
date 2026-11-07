from django.urls import path

from .views import (
    BlogPostCreateView,
    BlogPostDeleteView,
    BlogPostDetailView,
    BlogPostListView,
    BlogPostUpdateView,
    AllBlogPostListView,
)

app_name = 'blog'

urlpatterns = [
    path('', BlogPostListView.as_view(), name='list'),
    path('all/', AllBlogPostListView.as_view(), name='all'),
    path('create/', BlogPostCreateView.as_view(), name='create'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', BlogPostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', BlogPostDeleteView.as_view(), name='delete'),
]
