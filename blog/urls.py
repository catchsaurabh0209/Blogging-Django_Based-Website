from django.urls import path
from . import views
urlpatterns = [
    path('', views.base, name='base'),
    path('blog/', views.blog_list, name='blog_list'),
]
