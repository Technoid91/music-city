from django import forms

class SubscriptionForm(forms.Form):
    stripe_token = forms.CharField(widget=forms.HiddenInput())