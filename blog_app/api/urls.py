from django.urls import path

from .views import BlogView
app_name = 'blog_app'

urlpatterns = [

    path('blogs/', BlogView.as_view(), name='blog-view'),

 ]