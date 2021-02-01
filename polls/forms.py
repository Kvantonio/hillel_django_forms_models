from django import forms
from django.core.exceptions import ValidationError

from .models import MyPerson


def validate_num(value):
    if value <= 0:
        raise ValidationError('Invalid data')


def validate_date(value):
    if value <= 0:
        raise ValidationError('Invalid data')


class HypotenuseFrom(forms.Form):
    first_leg = forms.IntegerField(required=True, validators=[validate_num])
    second_leg = forms.IntegerField(required=True, validators=[validate_num])


class ReminderForm(forms.Form):
    email = forms.EmailField(required=True)
    text = forms.CharField(required=False)
    date = forms.DateTimeField(
        input_formats=["%H:%M:%S %d-%m-%Y"],
        validators=[validate_num]
    )


class MyPersonModelForm(forms.ModelForm):
    class Meta:
        model = MyPerson
        fields = ["id", "email", "first_name", "last_name"]
