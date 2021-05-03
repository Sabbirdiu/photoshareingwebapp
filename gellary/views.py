
# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm
from .models import ImageAlbum
from django.views.generic import CreateView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

class PostCreateView(LoginRequiredMixin,CreateView):
    model = ImageAlbum
    fields=['title','cover_image','image','image2','image3','image4','image5','image6','image7','image8','image9','image10','is_public']    
    template_name='gellary/new_album.html'

    def form_valid(self,form):#without a author other user cannot create a post
        form.instance.author = self.request.user
        return super().form_valid(form)
# class PostListView(ListView):
#     model = ImageAlbum
#     template_name = 'gellary/home.html'
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     paginate_by = 2
def home(request):
    context = {
        'posts':ImageAlbum.objects.filter(is_public=True).order_by('-date_posted')
    }
    return render(request,'gellary/home.html',context)
class PostDetailView(DetailView):
    model = ImageAlbum  
    template_name = 'gellary/detail_view.html'
class UserAlbumListView(ListView):
    model = ImageAlbum
    template_name = 'gellary/user_album.html'  
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return ImageAlbum.objects.filter(author=user,is_public=True).order_by('-date_posted')
# class Gellary(ListView):
#     model = ImageAlbum
#     template_name = 'gellary/gellary.html'  
#     context_object_name = 'posts'
#     paginate_by = 5

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return ImageAlbum.objects.filter(author=user).order_by('-date_posted')
def gellary(request):

    gellary = ImageAlbum.objects.filter().order_by('-date_posted')
    context = {
        'gellary':gellary
    }
    return render(request,'gellary/gellary.html',context)