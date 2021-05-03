
from django.urls import path
from .views import PostCreateView,home,PostDetailView,UserAlbumListView,gellary
urlpatterns = [
   path('',home),
   path('<int:pk>/',PostDetailView.as_view(),name ='post-detail'),
   path('post_create/',PostCreateView.as_view(),name="create"),
   path('user/<str:username>', UserAlbumListView.as_view(), name='user-posts'),
   path('gellary/', gellary, name='gellary'),
]