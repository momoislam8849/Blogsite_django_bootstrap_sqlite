from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','author','body')

		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Give your title'}),
			'author': forms.Select(attrs={'class':'form-control','placeholder':'Author name'}),
			'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Write your blog'}),

		}


class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Give your title'}),
			#'author': forms.Select(attrs={'class':'form-control','placeholder':'Author name'}),
			'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Write your blog'}),

		}
		