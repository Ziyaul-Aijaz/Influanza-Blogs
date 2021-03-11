from django import forms 
from .models import Post,Category

choices=Category.objects.all().values_list('name','name') 


choice_list=[]

for item in choices:  
	choice_list.append(item)  
# creating a form 
class PostForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Post 
  
        # specify fields to be used 
        fields = [ 
            "title", 
            "content",
            "date_posted",
            #"header_image",
            "category",
            "author", 
        ]
        widgets={
        'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Provide title'}),
        'content':forms.Textarea(attrs={'class':'form-control'}),
        'author':forms.TextInput(attrs={'class':'form-control','id':'user','type':'hidden'}),
        #'date_posted':forms.Select(attrs={'class':'form-control'}),
        #'author':forms.Select(attrs={'class':'form-control'}),
        'category':forms.Select(choices=choice_list,attrs={'class':'form-control'})
        } 


class EditForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Post 
  
        # specify fields to be used 
        fields = [ 
            "title", 
            "content",
         #   "date_posted",
          #  "author", 
        ]
        widgets={
        'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Provide title'}),
        'content':forms.Textarea(attrs={'class':'form-control'}),
        #'date_posted':forms.Select(attrs={'class':'form-control'}),
        #'author':forms.Select(attrs={'class':'form-control'})
        } 