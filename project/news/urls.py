from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='homepage'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('author/<int:pk>', AuthorView.as_view(), name='author'),
    path('edit/<int:pk>/', EditPostView.as_view(), name='edit'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='delete')
]