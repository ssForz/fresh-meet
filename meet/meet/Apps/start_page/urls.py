from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('reg_success/', views.reg_success, name = 'reg_success')
]
