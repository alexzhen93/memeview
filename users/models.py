# user profile
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	# add features of user profile
	image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics') # profile pic
	firstname = models.CharField(max_length = 15, blank = True)
	lastname = models.CharField(max_length = 15, blank = True)
	bio = models.TextField(max_length = 500, blank = True)
	location = models.CharField(max_length = 250, blank = True)
	birth_date = models.DateField(null = True, blank = True)
	#friends = models.ManyToManyField("Profile", blank = True) #new

	def __str__(self):
		return f'{self.user.username} Profile'

	def get_absolute_url(self):
		return "/user/{}".format(self.slug)


# # new ; friends
# class FriendRequest(models.Model):
# 	to_user = models.ForeignKey(User, related_name = 'to_user')
# 	from_user = models.ForeignKey(User, related_name = 'from_user')
# 	timestamp = models.DateTimeField(auto_now_add = True)

# 	def __str__(self):
# 		return "From {}, to {}".format(self.from_user.username, self.to_user.username)