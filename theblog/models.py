from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date 

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length= 255)
	author = models.ForeignKey(User, on_delete = models.CASCADE)  #cascade = when the user is dilited all his post will delete
	body = models.TextField()
	post_date = models.DateField(auto_now_add = True)


	def __str__(self):
		return self.title + ' | ' + str(self.author)  #shows title and author in admin panel


	def get_absolute_url(self):
		#return reverse('article_detail', args=(str(self.id)))
		return reverse('home')