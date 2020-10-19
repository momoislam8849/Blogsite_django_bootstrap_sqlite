from django import forms
from .models import Post,Category

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','author', 'category','body','snippet','header_image')

		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Give your title'}),
			'author': forms.TextInput(attrs={'class':'form-control','value':'', 'id': 'uid', 'type':'hidden'}),			
			#'author': forms.Select(attrs={'class':'form-control','placeholder':'Author name'}),
			'category': forms.Select(choices= choice_list, attrs={'class':'form-control','placeholder':'category name'}),
			'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Write your blog'}),
			'snippet': forms.Textarea(attrs={'class':'form-control'}),


		}


class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body','snippet')

		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Give your title'}),
			#'author': forms.Select(attrs={'class':'form-control','placeholder':'Author name'}),
			'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Write your blog'}),
			'snippet': forms.Textarea(attrs={'class':'form-control'}),


		}
		