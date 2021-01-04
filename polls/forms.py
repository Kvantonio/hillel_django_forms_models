from django import forms


class HypotenuseFrom(forms.Form):
    first_leg = forms.IntegerField(required=True)
    second_leg = forms.IntegerField(required=True)
