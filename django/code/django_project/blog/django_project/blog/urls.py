from django.urls import path
from .views import (BlogViewList, BlogDetailView, BlogCreateView, BlogUpadateView,BlogDeleteView )


urlpatterns = [

        
    path('post/new', BlogCreateView.as_view(), #to make a new post
         name='post_new'),

    path('post/<int:pk>/',  BlogDetailView.as_view(), # to see the details and body of the info using id
            name = "post_detail"),

     path('post/<int:pk>/edit/', BlogUpadateView.as_view(), #to edit or update post
         name ="post_edit"),
         
     path('post/<int:pk>/delete/', BlogDeleteView.as_view(), #to edit or update post
         name ="post_delete"),


    path('', BlogViewList.as_view(),
            name='home'), # home page
   ]