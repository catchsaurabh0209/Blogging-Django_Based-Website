from django.shortcuts import render
from django.utils import timezone
from .models import Post

def base(request):
    
    
    return render(request, 'blog/front.html', {})


def blog_list(request):
    	
    posts = Post.objects.get(title="self_Improvement")
    return render(request, 'blog/blog_list.html', {'posts': posts})
    
	
