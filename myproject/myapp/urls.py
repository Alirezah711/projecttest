from django.urls import path
from.views import UserView,UserCreate,UserUpdate,UserDelete

urlpatterns=[
    path('', UserView.as_view() ,name="user"), 
    path('creat-user/', UserCreate.as_view(),name="creat-user"),
    path('update-user/<int:pk>/',UserUpdate.as_view(),name="update-user"),
    path('user-delete/<int:pk>/',UserDelete.as_view(),name="User-delete"),
]
