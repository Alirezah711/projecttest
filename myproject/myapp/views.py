from multiprocessing import context
from django.forms import fields_for_model
from django.views.generic.list import ListView
from .models import User
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render

class UserView(ListView):
 model =User
 template_name = "User_list.html"
 context_object_name='Userdb'

class UserCreate(CreateView):
 model = User
 template_name= 'Usercreate.html'
 fields=['Name','family','age','cod']
 success_url=reverse_lazy('user')
 
class UserUpdate(UpdateView):
  model = User
  fields=['Name','family','age','cod']
  success_url=reverse_lazy('user')
  template_name= 'Usercreate.html'

class UserDelete(DeleteView):
  model = User
  context_object_name='Userdb'
  success_url=reverse_lazy('user')
  template_name= 'user_confirm_delete.html'
 

 