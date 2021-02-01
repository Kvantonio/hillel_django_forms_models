from datetime import datetime, timedelta

from django import forms
from django.core.exceptions import ValidationError

import pytz

from .models import MyPerson


def validate_num(value):
    if value <= 0:
        raise ValidationError('Invalid data')


def validate_date(value):
    err = datetime.now() + timedelta(days=2)
    utc = pytz.utc
    if value > utc.localize(err) or value < utc.localize(datetime.now()):
        raise ValidationError('Invalid data')


class HypotenuseFrom(forms.Form):
    first_leg = forms.IntegerField(required=True, validators=[validate_num])
    second_leg = forms.IntegerField(required=True, validators=[validate_num])


class ReminderForm(forms.Form):
    email = forms.EmailField(required=True)
    text = forms.CharField(required=False)
    date = forms.DateTimeField(
        input_formats=["%M:%H %d-%m-%Y"],
        validators=[validate_date]
    )


class MyPersonModelForm(forms.ModelForm):
    class Meta:
        model = MyPerson
        fields = ["id", "email", "first_name", "last_name"]
