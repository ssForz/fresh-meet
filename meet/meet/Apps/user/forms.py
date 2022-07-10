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

class TelegramForm(forms.Form):
    your_telegram = forms.CharField(label='your_telegram', max_length = 30)