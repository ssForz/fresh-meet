from django.shortcuts import render
from django.http import HttpResponseNotFound
from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

def index(request):
    return render(request, 'start_page/index.html') 

def test(request):
    #if request.method == 'POST':
    #    form = NameForm(request.POST)
    #    if form.is_valid():
    #        from user.models import User
     #       b = User(name = 'Beatles Blog', tagline='All the latest Beatles news.')
     #       b.save()
     #       return render(request, 'registration/index.html', {'current_name': form.cleaned_data['your_name']})

    return HttpResponseNotFound("hello")
