from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,
                              widget=forms.TextInput())
    from_email = forms.EmailField(widget=forms.TextInput())
    message = forms.CharField(widget=forms.Textarea())
