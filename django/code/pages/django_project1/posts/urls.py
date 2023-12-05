from django.urls import path

from posts import views


urlpatterns=[
    path('', views.HomePageView.as_view(),
         name='home')
]