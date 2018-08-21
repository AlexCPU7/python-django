from django import forms
from .models import Ticket


class AddTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ("category", "title", "text")
