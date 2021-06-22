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

   

class UserProfile(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500,blank=True, null=True)
    profile_pic = models.ImageField(blank=True, null=True, upload_to="images/profile/")
    website = models.URLField(blank=True, null=True)
    github = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    youtube = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)

    following = models.ManyToManyField(User, blank=True,related_name='following')
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def profile_posts(self):
        return self.post_set.all()

    def __str__(self):
        return str(self.user)


    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        ordering = ('-created',)


class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=220)
    post_date = models.DateField(auto_now_add=True)
    body = RichTextField(blank=True, null=True)
    add_time = models.TimeField(auto_now_add=True)
    header_image = models.ImageField(blank=True, null=True)

# this function will redirect user to home after creating a new post
    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return str(self.title)



class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE )
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name