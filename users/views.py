from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm # import custom form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from posts.models import Posts


# register user
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		# check if credentials valid 
		if form.is_valid(): # create user with credentials 
			form.save() # save user info
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created. You are now able to log in.')
			return redirect('login') # redirect to posts page
	else:
		form = UserRegisterForm() # no new uer
	return render(request, 'users/register.html', {'form': form})

# profile page
@login_required # decorater to restrict user to have logged in to access page
def profile(request):
	#user = UserProfile.objects.get(user=request.user){'profile_user': user}
	user_posts  = Posts.objects.filter(author=request.user).order_by('created_at')
	return render(request, 'users/profile.html', {'user_posts': user_posts})

@login_required
def edit_profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance = request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/edit_profile.html', context)

def get_user_profile(request, username = None):
	user = User.objects.get(username = username)
	return render(request, 'users/profile.html', {"user": user})