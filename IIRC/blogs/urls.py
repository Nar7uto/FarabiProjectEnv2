from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^', views.blogs, name='blogs'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^test/', views.post, name='post'),
]