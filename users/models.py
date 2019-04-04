# user profile
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	# add features of user profile
	image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics') # profile pic

	def __str__(self):
		return f'{self.user.username} Profile'


