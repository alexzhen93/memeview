from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm # import custom form

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
