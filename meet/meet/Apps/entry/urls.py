from django.urls import path

from . import views

urlpatterns = [
	path('/entry', views.index, name = 'index')
]