from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

# Create your views here.
def index(request):

	# All post objects
	posts = Posts.objects.all()

	context = {
		'title': "Post Feed",
		'posts': posts,
	}

	return render(request, 'posts/index.html', context)


def details(request, id):
	post = Posts.objects.get(id=id)

	context = {
		'post': post,
		'css': "posts/details.css"
	}

	return render(request, 'posts/details.html', context)
