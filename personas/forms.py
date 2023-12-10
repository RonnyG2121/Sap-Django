from django.forms import ModelForm, EmailInput
from .models import Persona


class Form_persona(ModelForm):

    class Meta:
        model = Persona
        fields = '__all__'

        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }
