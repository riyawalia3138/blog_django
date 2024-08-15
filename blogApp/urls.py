from django.urls import path

from . import views
from .views import *

urlpatterns = [
path('', blog.as_view(), name="blog"),
path('search', search, name="search"),
path('<slug:slug>/send-comment', views.send_comment, name="send_comment"),
path('<slug:slug>/', blogdetail.as_view(), name="blog-detail"),
# path('post/<int:post_id>/share/', views.share_post, name='share_post'),
path('post/<slug:slug>/', blogdetail.as_view(), name='post_detail'),
path('post/<int:post_id>/share/', share_post, name='share_post'),
path('post/<slug:slug>/comment/', send_comment, name='send_comment'),

]
