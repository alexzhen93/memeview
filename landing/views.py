from django.shortcuts import render

# Create your views here.
def index(request):

	context = {
		'css': 'landing/landing.css'
	}
	return render(request, 'landing/index.html', context)