from django.urls import path

from . import views

urlpatterns = [
	path('/office', views.index, name = 'index')
]