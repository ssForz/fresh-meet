from django.db import models

class Office(models.Model):
	CHOICE_SEX = (
		('M', 'Male'),
		('F', 'Female'),
	)
	username = models.CharField('Имя пользователя', max_length = 20)
	sex = models.CharField('Пол', max_length = 1, choices = CHOICE_SEX)
	age = models.IntegerField('Возраст')
	town = models.CharField('Город', max_length = 30)
	interest = models.CharField('Увлечение', max_length = 35)
	rating = models.FloatField('Рейтинг')
	email = models.CharField('E-mail', max_length = 30)
	password = models.CharField('Password', max_length = 15)
