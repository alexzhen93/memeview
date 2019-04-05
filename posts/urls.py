from django.urls import path
from django.conf.urls import url
from . import views
from .views import PostCreateView, PostUpdateView

urlpatterns = [
	path('', views.index, name='posts-index'),
	path('new/', PostCreateView.as_view(), 
		name='post-create'),
	url(r'^details/(?P<id>\d+)/$', 
		views.details, name='post-detail'),
	path('update/<int:pk>/', PostUpdateView.as_view(),
		name='post-update')

]