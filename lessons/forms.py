from django import forms
from .models import Subscription, Playlist, Lesson

class SubscriptionForm(forms.Form):
    stripe_token = forms.CharField(widget=forms.HiddenInput())


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        playlists = Playlist.objects.all()
        friendly_names = [(p.id, p.get_friendly_name()) for p in playlists]

        self.fields['playlist'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded'


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = '__all__'





