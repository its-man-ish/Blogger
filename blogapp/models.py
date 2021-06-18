from django.db import models
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Category(models.Model):
    name= models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=220)
    post_date = models.DateField(auto_now_add=True)
    body = RichTextField(blank=True, null=True)
    add_time = models.TimeField(auto_now_add=True)
    header_image = models.ImageField(blank=True, null=True)

# this function will redirect user to home after creating a new post
    def get_absolute_url(self):
        return reverse('home')

   

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500,blank=True, null=True)
    profile_pic = models.ImageField(blank=True, null=True, upload_to="images/profile/")
    website = models.URLField(blank=True, null=True)
    github = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    youtube = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)




    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE )
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name