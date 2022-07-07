from django.db import models

class User(models.Model):
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
	def username(self):
		return self.username
	def sex(self):
		return self.sex
	def age(self):
		return self.age
	def town(self):
		return self.town
	def interest(self):
		return self.interest
	def rating(self):
		return self.rating