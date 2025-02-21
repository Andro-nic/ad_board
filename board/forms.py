from django import forms
from .models import Announcement, Response
from tinymce.widgets import TinyMCE


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'category']
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 15}),
        }

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['content']

