from django import forms

from .models import MyPerson


class HypotenuseFrom(forms.Form):
    first_leg = forms.IntegerField(required=True)
    second_leg = forms.IntegerField(required=True)


class MyPersonModelForm(forms.ModelForm):
    class Meta:
        model = MyPerson
        fields = ["id", "email", "first_name", "last_name"]
