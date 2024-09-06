from django import forms


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=255, label='Subject')
    body = forms.CharField(widget=forms.Textarea, label='Body')
