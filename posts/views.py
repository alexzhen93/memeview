from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from django.views.generic import CreateView

def index(request):

	# First 10 post objects
	posts = Posts.objects.all()[:10]
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

class PostCreateView(CreateView):
	model = Posts
	fields = ['caption', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user

		#overriding default form valid before returning
		return super().form_valid(form)