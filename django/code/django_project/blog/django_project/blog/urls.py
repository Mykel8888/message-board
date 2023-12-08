from django.urls import path
from .views import BlogViewList, BlogDetailView


urlpatterns = [
    path('post/<int:pk>/',  BlogDetailView.as_view(),
          name = "post_detail"),

    path('', BlogViewList.as_view(),
         name='home'),
   ]