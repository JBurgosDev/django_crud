from django import forms
from crud.models import PersonasDatos


class PersonasForm(forms.ModelForm):
    class Meta:
        model = PersonasDatos
        fields = "__all__"
