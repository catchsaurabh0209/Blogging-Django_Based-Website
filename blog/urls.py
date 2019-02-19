from django.urls import path
from . import views
urlpatterns = [
    path('', views.base, name='base'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog1/', views.blog_list1, name='blog_list1'),
    path('about/', views.about, name='about'),
]
