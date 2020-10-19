from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date 
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name  #shows title in admin panel


	def get_absolute_url(self):
		#return reverse('article_detail', args=(str(self.id)))
		return reverse('home')


class Post(models.Model):
	title = models.CharField(max_length= 255)
	header_image = models.ImageField(null=True,blank=True, upload_to='images/')
	author = models.ForeignKey(User, on_delete = models.CASCADE)  #cascade = when the user is dilited all his post will delete
	#body = models.TextField()
	body = RichTextField(blank= True, null = True)
	category = models.CharField(max_length=255, default = 'coding')
	snippet = models.CharField(max_length=100)
	post_date = models.DateField(auto_now_add = True)
	likes = models.ManyToManyField(User, related_name = 'blog_posts')

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title + ' | ' + str(self.author)  #shows title and author in admin panel


	def get_absolute_url(self):
		#return reverse('article_detail', args=(str(self.id)))
		return reverse('home')