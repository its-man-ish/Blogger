from django.urls import path
from .views import*
urlpatterns = [
  path('',Index,name='index'),
  path('home/',HomeView.as_view(), name='home'),
  path('articles/<int:pk>',ArticleDetailView.as_view(),name='details'),
  path('articles/<int:pk>/comment/',AddCommentView.as_view(),name='add_comments'),
  path('create/',CreateNewPost.as_view(),name='create'),
  path('update/<int:pk>',UpdatePost.as_view(),name='update'),
  path('delete/<int:pk>',DeletePost.as_view(),name='delete'),
  path('user_posts/',post_of_user, name='user_posts'),

]
