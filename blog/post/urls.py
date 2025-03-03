from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='list-create-post'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy-post'),

    path('posts/comments/', CommentListCreateAPIView.as_view(), name='list-create-comment'),
    path('posts/<int:post_id>/comments/', CommentListCreateAPIView.as_view(), name='list-create-comment'),
    path('posts/<int:post_id>/comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy-comment'),
]
