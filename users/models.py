from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
# Create your models here.

class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	bio= models.TextField()
	dp= models.ImageField(default='default.jpg',upload_to="dp/")
	website=models.CharField(max_length=255,null=True,blank=True)

	instagram=models.CharField(max_length=255,null=True,blank=True)

	facebook=models.CharField(max_length=255,null=True,blank=True)

	twitter=models.CharField(max_length=255,null=True,blank=True)
	def __str__(self):
		return f'{self.user.username} Profile'



class UserProfile(models.Model):
	user=models.ForeignKey(Post, on_delete=models.CASCADE)
	bio= models.TextField()
	dp= models.ImageField(default='default.jpg',upload_to="dp/")
	website=models.CharField(max_length=255,null=True,blank=True)

	instagram=models.CharField(max_length=255,null=True,blank=True)

	facebook=models.CharField(max_length=255,null=True,blank=True)

	twitter=models.CharField(max_length=255,null=True,blank=True)