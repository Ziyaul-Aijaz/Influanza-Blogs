from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import CreateView,DeleteView
from .models import Post,Category
from .forms import PostForm,EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from users.forms import ProfileUpdateForm
from users.models import Profile
from django.contrib.auth.models import User
# Create your views here.

#posts=[
#{
#'author': 'Ziyaul Aijaz',
#'title': 'Blog Post',
#'content': 'First post content',
#'date_posted': 'October 24, 2020'	
#},
#{
#'author': 'Robin',
#'title': 'Blog Post 2',
#'content': '2 post content',
#'date_posted': 'October 25, 2020'	
#}

#]

def home(request):
	context={
	'posts':Post.objects.all().order_by('-date_posted')
	}
	return render(request,'blog/home.html',context)

#def LikeView(request, id):
#	post= get_object_or_404(Post, id= request.POST.get('post_id'))
	#post=Post.objects.get(id=pk)
#	post.likes.add(request.user)
#	return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

def category_home(request):
	context={
	'posts':Category.objects.all(),
	'category':Post.objects.all()
	}
	return render(request,'blog/categories_home.html',context)

def about(request):
	return render(request,'blog/about.html',{'title':'About'})

def detail_view(request, id):
	context={}
	context["post"]=Post.objects.get(id=id)
	return render(request,'blog/article_detail.html',context)

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-',' ')).order_by('-date_posted')

	return render(request, 'blog/categories.html', {'cats':cats, 'category_posts':category_posts})

#def AuthorDetail(request, author_id):
#	author_detail= Post.objects.filter(author=Post.objects.filter(author_id=author))
#	p_form= ProfileUpdateForm()
    
#	return render(request,'blog/profile_page.html',{'author_detail':author_detail,'p_form':p_form})

def update_view(request, id):
	context={}
	obj=get_object_or_404(Post, id=id)
	form=EditForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/article/"+str(id))
	context["form"]=form
	return render(request,"blog/update_view.html",context)

class AddPostView(CreateView):
	model=Post
	form_class=PostForm
	template_name= 'blog/add_post.html'
	#fields= '__all__'

class DeletePost(DeleteView):
	model=Post
	template_name='blog/delete_post.html'
	success_url = reverse_lazy('blog-home')

#def add_post(request,pk):
#	context={}


    # add the dictionary during initialization
    
#	form = PostForm(request.POST or None) 
#	    
#	if form.is_valid(): 
#		form.save() 
          
#	context['form']= form 
#	return render(request, "blog/add_post.html", context,{'post': get_object_or_404(Post,pk=id)})
