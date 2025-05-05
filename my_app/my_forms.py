from django import forms

from my_app.models import Customer


class CustomerForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput)
    gender= forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')],
                              widget=forms.RadioSelect)
    dob= forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone','password','weight' ,'height'  ,'gender','dob']


# pip install django-crispy forms
# pip install crispy-bootstrap

# pip freeze > requirements.txt
