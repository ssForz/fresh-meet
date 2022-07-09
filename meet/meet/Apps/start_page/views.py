from django.shortcuts import render
from django.http import HttpResponseNotFound

from user.forms import NameForm, AgeForm, SexForm, TownForm, HobbyForm, MailForm, PasswordForm, PasswordCheckForm, LogMailForm, LogPasswordForm

from user.models import Person
from user.models import Log_Person

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

def log_success(request):
    if request.method == 'POST':
        form_log_mail = MailForm(request.POST)
        form_log_password = PasswordForm(request.POST)
        if form_log_mail.is_valid() and form_log_password.is_valid():
            from user.models import Log_Person
            log_mail = form_log_mail.cleaned_data.get("your_mail")
            log_password = form_log_password.cleaned_data.get('your_password')
            #log_user = Log_Person(l_email=log_mail, l_p)
            #log_user.save()
            news = Person.objects.all()
            for i in news:
                if i.email == log_mail and i.password == log_password:
                    #return HttpResponseNotFound(i.id)
                    #log_user = Log_Person(l_password=i.id)
                    #log_user.save()
                    return HttpResponseNotFound("OKK!!!")
            return render(request, 'entry/index.html')
            return render(request, 'start_page/index.html')

    return HttpResponseNotFound("hello")


