from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Posts, Comment, AllComment
from .forms import CommentForm
from django.views.generic import (
	CreateView, 
	UpdateView,
	DeleteView
)
from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	UserPassesTestMixin
)
from django.views.generic.base import RedirectView

def index(request):

	# First 10 post objects
	posts = Posts.objects.all()[:10]
	context = {
		'title': "Post Feed",
		'posts': posts,
	}

	return render(request, 'posts/index.html', context)

def details(request, id):

	postid = id;

	post = Posts.objects.get(id=postid)
	is_liked = False
	if post.likes.filter(id=request.user.id).exists():
		is_liked = True
	comments = Comment.objects.filter(parentPost=postid).order_by('-id')

	if request.method == 'POST':
		comment_form = CommentForm(request.POST or None)
		if comment_form.is_valid():
			comment = request.POST.get('comment')
			comments = comments.create(parentPost = post, user = request.user, comment = comment)
			comments.save()
			return HttpResponseRedirect(post.get_absolute_url())

	else:
		comment_form = CommentForm()

	context = {
		'post': post,
		'css': "posts/details.css",
		'comments': comments,
		'comment_form': comment_form,
		'is_liked': is_liked

	}

	return render(request, 'posts/details.html', context)

def allcomments(request):

	comments = AllComment.objects.all()
	
	context = {
		'comments': comments
	}

	return render(request, 'posts/allcomments.html', context)

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

def add_comment(request, slug):
	post = get_object_or_404(Posts, slug = slug)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit = False)
			comment.post = post
			comment.save()
			return Comment
	else:
		form = CommentForm()
	return render(request, template, context)

class PostLikeToggle(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        print(slug) #Prints the slug
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
