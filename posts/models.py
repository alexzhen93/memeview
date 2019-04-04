from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.
class Posts(models.Model):
	caption = models.CharField(max_length=255)
	image = models.CharField(max_length=255)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.caption[0:10] + "..."

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'id': self.pk})

	class Meta:
		verbose_name_plural = "Posts"

