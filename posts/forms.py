from django import forms
from .models import Posts, Comment
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('comment',)
		widgets = {
			'comment': forms.Textarea(attrs={'rows': 2, 'col':15})
		}