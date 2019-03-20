from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
	caption = models.CharField(max_length=255)
	image = models.CharField(max_length=255)
	created_at = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.caption[0:10] + "..."

	class Meta:
		verbose_name_plural = "Posts"

