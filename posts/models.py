from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here.
class Posts(models.Model):
	caption = models.CharField(max_length=255)
	image = models.CharField(max_length=255)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return self.caption[0:10] + "..."

	class Meta:
		verbose_name_plural = "Posts"

