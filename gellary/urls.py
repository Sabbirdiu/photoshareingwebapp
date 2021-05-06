
from django.urls import path
from .views import AlbumCreateView,home,AlbumDetailView,UserAlbumListView,gellary,AlbumUpdateView,AlbumDeleteView
urlpatterns = [
   path('',home),
   path('<int:pk>/',AlbumDetailView.as_view(),name ='post-detail'),
   path('post_create/',AlbumCreateView.as_view(),name="create"),
   path('user/<str:username>', UserAlbumListView.as_view(), name='user-posts'),
   path('gellary/', gellary, name='gellary'),
   path('album/<int:pk>/update_post/',AlbumUpdateView.as_view(),name ='album-update'),
   path('post/<int:pk>/delete_post/',AlbumDeleteView.as_view(),name ='post-delete'),
]