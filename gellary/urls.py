
from django.urls import path
from .views import PostCreateView,home,PostDetailView,UserAlbumListView,gellary,AlbumUpdateView,AlbumDeleteView
urlpatterns = [
   path('',home),
   path('<int:pk>/',PostDetailView.as_view(),name ='post-detail'),
   path('post_create/',PostCreateView.as_view(),name="create"),
   path('user/<str:username>', UserAlbumListView.as_view(), name='user-posts'),
   path('gellary/', gellary, name='gellary'),
   path('album/<int:pk>/update_post/',AlbumUpdateView.as_view(),name ='album-update'),
     path('post/<int:pk>/delete_post/',AlbumDeleteView.as_view(),name ='post-delete'),
]