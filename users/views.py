from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm # import custom form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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
def profile(request, username = None):
	#user = UserProfile.objects.get(user=request.user){'profile_user': user}
	return render(request, 'users/profile.html')

@login_required
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()

def get_user_profile(request, username):
	user = User.objects.get(username = username)
	return render(request, 'users/profile.html', {"user": user})