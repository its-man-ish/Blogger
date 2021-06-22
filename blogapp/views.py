from django.shortcuts import render 
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from itertools import chain
# Create your views here.


def Index(request):
    return render(request,'blogapp/index.html')

class HomeView(LoginRequiredMixin,ListView):
    model = Post
    ordering=['-id']
    login_url = 'login'
    template_name ='blogapp/home.html'


class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Post
    login_url = 'login'
    template_name ='blogapp/detail.html'


class CreateNewPost(LoginRequiredMixin,CreateView):
    form_class = PostForm
    login_url = 'login'
    template_name ='blogapp/create_post.html'


class UpdatePost(UpdateView):
    model=Post
    fields = ('title','title_tag','body','header_image')
    template_name ='blogapp/update_post.html'


    def get_absolute_url(self):
        return reverse('home')

class DeletePost(DeleteView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('home')
    template_name = 'blogapp/delete_post.html'
    

class AddCommentView(LoginRequiredMixin,CreateView):
    model = Comments
    form_class = AddCommentForm
    template_name ='blogapp/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)



    success_url = reverse_lazy('home')


 
def post_of_user(request):
    #get logged in user
    profile = UserProfile.objects.get(user=request.user)
    # check who we are following
    users = [user for user in profile.following.all() ]


    posts = []
    qs = None

    #get the posts of folloing user
    for u in users:
        p = UserProfile.objects.get(user=u)
        p_post = p.post_set.all()
        posts.append(p_post)
    #includieng own posts
    my_posts = profile.profile_posts()
    posts.append(my_posts)

    if len(posts)>0:
        qs=sorted(chain(*posts),reverse=True, key=lambda obj:obj.post_date)
    context = {
        'posts': qs,
        'profile': profile,
        }
    return render(request,'blogapp/user_posts.html', context)


