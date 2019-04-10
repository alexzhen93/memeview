from django import forms
from .models import Posts, Comment
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
	comment = forms.CharField(label ='', widget = forms.Textarea(attrs= {
		'class': 'form-control',
		'placeholder': 'Write a comment...',
		'row':'',
		'col':'',
		'style': 'height : 2.5em;'
		}))
	class Meta:
		model = Comment
		fields = ('comment',)
		# widgets = {
		# 	'comment': forms.Textarea( attrs={'rows': 2, 'col':15})
		# }