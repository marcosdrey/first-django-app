from django.urls import path
from . import views
from .views import BlogCreateView, BlogDetailedView, BlogUpdateView, BlogDeleteView, BlogView, UserBlogListView

urlpatterns = [
    path('', views.home, name='site-home'),
    path('about/', views.about, name='site-about'),
    path('blog/', BlogView.as_view(), name='site-blog'),
    path('blog/new/', BlogCreateView.as_view(), name='blog-new'),
    path('blog/detailed/<int:pk>/', BlogDetailedView.as_view(), name='blog-detailed'),
    path('blog/detailed/<int:pk>/update', BlogUpdateView.as_view(), name='blog-update'),
    path('blog/detailed/<int:pk>/delete', BlogDeleteView.as_view(), name='blog-delete'),
    path('blog/user/<str:username>', UserBlogListView.as_view(), name='user-blog')
]