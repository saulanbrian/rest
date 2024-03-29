from main import apiviews
from django.urls import path

urlpatterns = [
  path('posts',apiviews.PostList.as_view(),name='post-list')
  ]