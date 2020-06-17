"""Posts forms."""
#Django
from django import forms

#Model
from posts.models import Post

class PostForm(forms.ModelForm):
	class Meta:
		"""Form settings"""
		model = Post
		fields = ['user', 'profile', 'title', 'photo']
		pass
