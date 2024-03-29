from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

class PostList(generics.ListCreateAPIView):
 #  queryset = Post.objects.all()
  serializer_class = PostSerializer
  
  def get_queryset(self):
    queryset = Post.objects.filter(author=self.request.user)
    return queryset
    
  def perform_create(self,serializer):
    serializer.save(author=self.request.user)