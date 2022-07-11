from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse

from user.forms import NameForm, AgeForm, SexForm, TownForm, HobbyForm, MailForm, PasswordForm, PasswordCheckForm
from user.models import Person, Log_Person, Search
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

            if your_sex != 'Мужской' and your_sex != 'Женский':
                return render(request, 'registration/index.html')
                
            your_town = form_town.cleaned_data.get("your_town")

            your_hobby = form_hobby.cleaned_data.get("your_hobby")

            your_mail = form_mail.cleaned_data.get("your_mail")

            news = Person.objects.all()
            for i in news:
                if i.email == your_mail:
                    return render(request, 'registration/index.html')
            your_password = form_password.cleaned_data.get("your_password")

            your_password2 = form_password2.cleaned_data.get("your_password2")

            if your_password != your_password2: 
                return render(request, 'registration/index.html')

            b = Person(username = your_name, sex=your_sex, age = your_age, town = your_town, interest = your_hobby, rating = 0, email = your_mail, password = your_password, online = False, token = '')
            b.save()
            return render(request, 'start_page/index.html')

    return HttpResponseNotFound("Error")


def log_success(request):
    if request.method == 'POST':
        form_log_mail = MailForm(request.POST)
        form_log_password = PasswordForm(request.POST)
        if form_log_mail.is_valid() and form_log_password.is_valid():
            from user.models import Log_Person
            log_mail = form_log_mail.cleaned_data.get("your_mail")
            log_password = form_log_password.cleaned_data.get('your_password')
            news = Person.objects.all()
            for i in news:
                if i.email == log_mail and i.password == log_password:
                    i.token = request.COOKIES.get('csrftoken')
                    for check in news:
                        if check.token == i.token and i.email != check.email:
                            return HttpResponseNotFound("Сиди с одного аккаунта, мерзавец))))")
                    i.online = True;
                    i.save()
                    return render(request, 'start_page/index.html')
            return render(request, 'entry/index.html')
            

    return HttpResponseNotFound("Error")


def search_success(request):
    if request.method == 'POST':
        my_token = request.COOKIES.get('csrftoken')
        news = Person.objects.all()
        base_search = Search.objects.all()
        my_token = ''
        my_id = 0
        my_interest = ''
        my_town = ''
        for i in Person:
            if str(my_token) == str(i.token):
                my_id = int(i.id)
                my_interest = str(i.interest)
                my_town = str(i.town)
        already_in_search = 0
        for i in base_search:
            if int(user_id) == int(i.user_id):
                already_in_search = 1
        q = Search(user_id = my_id, interest = my_interest,town = my_town)
        if already_in_search == 0:
            q.save()
        base_search = Search.objects.all()
        success = 0
        answer_id = 0
        your_telegram = ''
        while(true):
            for compain in base_search():
                if str(my_town) == str(compain.town) and str(my_interest) == str(compain.interest) and int(my_id) != int(compain.user_id):
                    success = 1
                    answer_id = int(companion_user_id)
                    for i in search:
                        if i.id == answer_id:
                            your_telegram = i.username
                    break
            if (success == 1):
                q.delete()
                break       

    context2 = {
        'your_telegram': your_telegram,
    }   
    return render(request, 'found/index.html', context = context2)


def off_success(request):
    check_token = request.COOKIES.get('csrftoken')

    base_out = Person.objects.all()

    for i in base_out:
        if i.token == check_token:
            i.online = False
            i.token = ''
            i.save()
            return render(request, 'start_page/index.html')
    return HttpResponseNotFound('help')
