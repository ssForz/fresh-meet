from django.db import models



class Person(models.Model):
	
	username = models.CharField('Имя пользователя', max_length = 20, null=True)

	sex = models.CharField('Пол', max_length = 10, null=True)

	age = models.CharField('Возраст', max_length = 2, null=True)

	town = models.CharField('Город', max_length = 30, null=True)

	interest = models.CharField('Увлечение', max_length = 35, null=True)

	rating = models.FloatField('Рейтинг')

	email = models.CharField('E-mail', max_length = 30, null=True)

	password = models.CharField('Password', max_length = 15, null=True)

	def __str__(self):
		return self.username

class Log_Person(models.Model):

	user_id = models.CharField('User_id', max_length = 30, null=True)