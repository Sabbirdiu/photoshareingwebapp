from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse


class ImageAlbum(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cover_image = models.ImageField()    
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image2 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image3 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image4 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image5 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image6 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image7 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image8 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image9 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image10 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_public = models.BooleanField(default=True)  
    date_posted = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})


