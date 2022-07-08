from django.shortcuts import render
from django.http import HttpResponseNotFound
from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='your_name', max_length=20)

class AgeForm(forms.Form):
    your_age = forms.CharField(label='your_age', max_length = 2)

class SexForm(forms.Form):
    your_sex = forms.CharField(label='your_sex', max_length = 7)

class TownForm(forms.Form):
    your_town = forms.CharField(label='your_town', max_length = 30)

class HobbyForm(forms.Form):
    your_hobby = forms.CharField(label='your_hobby', max_length = 35)

class MailForm(forms.Form):
    your_mail = forms.CharField(label='your_mail', max_length = 30)

class PasswordForm(forms.Form):
    your_password = forms.CharField(label='your_password', max_length = 15)

class PasswordCheckForm(forms.Form):
    your_password2 = forms.CharField(label='your_password2', max_length = 15)

def index(request):
    return render(request, 'start_page/index.html') 

def reg_success(request):
    if request.method == 'POST':
        form_name = NameForm(request.POST)
        form_age = AgeForm(request.POST)
        form_sex = SexForm(request.POST)
        form_town = TownForm(request.POST)
        form_hobby = HobbyForm(request.POST)
        form_mail = MailForm(request.POST)
        form_password = PasswordForm(request.POST)
        form_password2 = PasswordCheckForm(request.POST)

        if form_name.is_valid() and form_age.is_valid() and form_sex.is_valid() and form_town.is_valid() and form_hobby.is_valid() and form_mail.is_valid() and form_password.is_valid() and form_password2.is_valid():
            from user.models import Person

            your_name = form_name.cleaned_data.get("your_name")

            your_age = form_age.cleaned_data.get('your_age')

            your_sex = form_sex.cleaned_data.get("your_sex")

            your_town = form_town.cleaned_data.get("your_town")

            your_hobby = form_hobby.cleaned_data.get("your_hobby")

            your_mail = form_mail.cleaned_data.get("your_mail")

            your_password = form_password.cleaned_data.get("your_password")

            b = Person(username = your_name, sex=your_sex, age = your_age, town = your_town, interest = your_hobby, rating = 0, email = your_mail, password = your_password)
            b.save()
            return render(request, 'start_page/index.html')

    return HttpResponseNotFound("hello")
