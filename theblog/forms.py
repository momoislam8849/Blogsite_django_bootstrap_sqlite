from django import forms
from .models import Post,Category

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','author', 'category','body')

		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Give your title'}),
			'author': forms.Select(attrs={'class':'form-control','placeholder':'Author name'}),
			'category': forms.Select(choices= choice_list, attrs={'class':'form-control','placeholder':'category name'}),
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
		