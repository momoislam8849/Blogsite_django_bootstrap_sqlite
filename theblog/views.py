from django.shortcuts import render
from .models import Post,Category
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
# Create your views here.

#def home(request):
#	return render(request, 'home.html', {})

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-post_date', '-id']

def CategoryView(request,cats):
	category_posts = Post.objects.filter(category= cats.replace('-',' '))
	return render(request,'categories.html',{'cats':cats.title().replace('-',' '), 'category_posts': category_posts})

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_detail.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'

class AddCategoryView(CreateView):
	model = Category
	#form_class = PostForm
	template_name = 'add_category.html'
	fields = '__all__'

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'
	#fields = ['title', 'body']
	#success_url = reverse_lazy('home')

class DeletePostView(DeleteView):
	model = Post
	#form_class = EditForm
	template_name = 'delete_post.html'
	#fields = ['title', 'body']
	success_url = reverse_lazy('home')
		