from django import forms


class ReaderForm(forms.Form):
    username = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    picture = forms.ImageField()
    phone = forms.CharField(max_length=12)
    profession = forms.CharField(max_length=200)
    card = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput())
    re_password = forms.CharField(widget=forms.PasswordInput())


class EmployeeForm(forms.Form):
    username = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    picture = forms.ImageField()
    phone = forms.CharField(max_length=12)
    password = forms.CharField(widget=forms.PasswordInput())
    re_password = forms.CharField(widget=forms.PasswordInput())
