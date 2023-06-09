from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(),
            'start_date': forms.DateInput(),
            'end_date': forms.DateInput()
        }