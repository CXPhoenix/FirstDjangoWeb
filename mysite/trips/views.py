from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Posts

# Create your views here.
def helloWorld(request):
    context = {"currentTime": str(datetime.now())}
    return render(request, 'trips/helloWorld.html', context)

def home(request):
    postList = Posts.objects.all()
    return render(request, 'trips/home.html', {
        'postList': postList,
    })

def postDetail(request, pk):
    post = Posts.objects.get(pk=pk)
    return render(request, 'trips/post.html',{
        'post': post,
    })