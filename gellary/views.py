
# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm
from .models import ImageAlbum
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User

class AlbumCreateView(LoginRequiredMixin,CreateView):
    model = ImageAlbum
    fields=['title','cover_image','image','image2','image3','image4','image5','image6','image7','image8','image9','image10','is_public']    
    template_name='gellary/new_album.html'

    def form_valid(self,form):#without a author other user cannot create a post
        form.instance.author = self.request.user
        return super().form_valid(form)

def home(request):
    context = {
        'posts':ImageAlbum.objects.filter(is_public=True).order_by('-date_posted')
    }
    return render(request,'gellary/home.html',context)
class AlbumDetailView(DetailView):
    model = ImageAlbum  
    template_name = 'gellary/detail_album.html'
class UserAlbumListView(ListView):
    model = ImageAlbum
    template_name = 'gellary/user_album.html'  
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return ImageAlbum.objects.filter(author=user,is_public=True).order_by('-date_posted')

class  AlbumUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = ImageAlbum
    fields=['title','cover_image','image','image2','image3','image4','image5','image6','image7','image8','image9','image10','is_public']    
    template_name='gellary/update_album.html'
   
   
    def form_valid(self,form):#without author,other user can not update the post
        form.instance.author = self.request.user
        return super().form_valid(form)        

    def test_func(self):
        post = self.get_object()
        if self.request.user== post.author:
            return True
        return False 
class AlbumDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = ImageAlbum
    template_name = 'gellary/delete_album.html'
    success_url='/'       

    def test_func(self):
        post = self.get_object()
        if self.request.user== post.author:
            return True
        return False
def gellary(request):
    current_user = request.user

    gellary = ImageAlbum.objects.filter(author=current_user).order_by('-date_posted')
    context = {
        'gellary':gellary
    }
    return render(request,'gellary/my_gellary.html',context)