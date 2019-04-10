from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from django.views.generic import (
	CreateView, 
	UpdateView,
	DeleteView
)
from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	UserPassesTestMixin
)

from django.views.generic.base import (
	RedirectView
)

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

class PostCreateView(LoginRequiredMixin, 
	 CreateView):
	model = Posts
	fields = ['caption', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user

		#overriding default form valid before returning
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, 
	UserPassesTestMixin, UpdateView):
	model = Posts
	fields = ['caption', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user

		#overriding default form valid before returning
		return super().form_valid(form)

	# enforces that only authors can edit their own posts
	def test_func(self):
		post = self.get_object()
		return (self.request.user == post.author)

class PostDeleteView(LoginRequiredMixin, 
	UserPassesTestMixin, DeleteView):
	model = Posts
	success_url = "/posts"

	# enforces that only authors can delete their own posts
	def test_func(self):
		post = self.get_object()
		return (self.request.user == post.author)
		
class PostLikeToggle(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(Posts, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        print(url_)
        return url_