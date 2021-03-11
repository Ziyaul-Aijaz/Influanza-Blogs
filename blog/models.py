from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=255,default='Uncategorized')
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog-home')

class Post(models.Model):
	title=models.CharField(max_length=100)
	content= RichTextField(blank=True, null=True)
	#content=models.TextField()
	date_posted= models.DateTimeField(default=timezone.now)
	author= models.ForeignKey(User, on_delete=models.CASCADE)
	category=models.CharField(max_length=255, default='Uncategorized')
	likes= models.ManyToManyField(User, related_name='blog_posts')
	header_image= models.ImageField(null=True, blank=True, upload_to="images/")
	def _str__(self):
		return self.title + ' | ' + str(self.author)
	def get_absolute_url(self):
		return reverse('blog-home')

