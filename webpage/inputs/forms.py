from django import forms
from .models import Input


class InputForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = "__all__"
        exclude = ["doctor", "answer"]

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = "__all__"