from django.forms import ModelForm, DateTimeInput
from .models import ReservedPlace


class FormBooking(ModelForm):
    class Meta:
        model = ReservedPlace
        fields = ['parking_space',
                  'date_start_parking',
                  'date_finish_parking',
                  ]
        widgets = {
            'date_start_parking': DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_finish_parking': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
