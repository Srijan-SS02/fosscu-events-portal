from django.forms import ModelForm
from .models import Event

class RegisterEventform(ModelForm): 
    class Meta:
        model: Event
        fields = '__all__'

