from django import forms

from .models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl border'})
        }
