from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('reg_success/', views.reg_success, name = 'reg_success'),
	path('log_success/', views.log_success, name = 'log_success'),
	path('search_success/', views.search_success, name = 'search_success')
]
