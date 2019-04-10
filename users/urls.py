from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('<str:username>/', views.get_user_profile, name = 'user_profile'),
]