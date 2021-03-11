from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import UserRegisterForm,UserChangeForm,ProfileUpdateForm
from django.contrib.auth.views import PasswordChangeView


class UserRegisterView(generic.CreateView):
    form_class= UserRegisterForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class= UserChangeForm
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('blog-home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class= PasswordChangeForm
    success_url=reverse_lazy('blog-home')



def profile(request):
    p_form= ProfileUpdateForm()
    context={'p_form':p_form}
    return render(request,'registration/profile.html',context)

