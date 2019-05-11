from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.
class Posts(models.Model):
	caption = models.CharField(max_length=255)
	image = models.ImageField(default=None, upload_to='memes')
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, related_name = 'likes', blank = True)
	
	def __str__(self):
		return self.caption[0:10] + "..."

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'id': self.pk})

	class Meta:
		verbose_name_plural = "Posts"

#Comments
class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.TextField(max_length=255)
	parentPost = models.ForeignKey(Posts, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(default=datetime.now, blank=True)

	# replies
	#parent = models.ForeignKey("self", null = True, blank = True, on_delete = models.CASCADE)
	#content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return '{}-{}'.format(self.post.title, str(self.user.username))

	def delete_comment(self):
		self.delete()

	def save_comment(self):
		self.save()

	# new replies
	def children(self):
		return Comment.objects.filter(parent = self)

	@property
	def is_parent(self):
		if self.parentPost is not None:
			return False
		return True

# Database view that shows all comments paired with
# more detailed information about their authors
class AllComment(models.Model):
	comment = models.OneToOneField(Comment, on_delete=models.DO_NOTHING, primary_key=True)
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	
	class Meta:
		managed = False
		db_table = "view_allcomments"
		unique_together = (("comment","author"),)