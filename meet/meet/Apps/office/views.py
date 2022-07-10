from django.shortcuts import render

from django.template.loader import get_template

from user.models import Person

from django.http import HttpResponse

def index(request):

	check = request.COOKIES.get('csrftoken')

	check_token = 0;

	news = Person.objects.all()

	for i in news:
		if check == i.token:

			check_token = 1


			your_name = i.username

			your_age = i.age
			your_sex = i.sex                
			your_town = i.town
			your_hobby = i.interest
			context2 = {
				'your_name': your_name,
				'your_age': your_age,
				'your_sex': your_sex,
				'your_town': your_town,
				'your_hobby': your_hobby
			}
			return render(request, 'office/index.html', context = context2)


	return render(request, 'entry/index.html')