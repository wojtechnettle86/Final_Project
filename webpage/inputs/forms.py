from django import forms
from .models import Input


class InputForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = "__all__"
        exclude = ["doctor", "answer"]
        labels = {
            "firstname": "Jméno",
            "lastname": "Příjmení",
            "phone": "Telefon",
            "email": "Email",
            "question_name": "Název otázky",
            "question_text": "Text otázky",
        }
        widgets = {
            "firstname": forms.TextInput(attrs={'class':'form-control'}),
            "lastname": forms.TextInput(attrs={'class':'form-control'}),
            "phone": forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.TextInput(attrs={'class':'form-control'}),
            "question_name": forms.TextInput(attrs={'class':'form-control'}),
            "question_text": forms.Textarea(attrs={'class':'form-control'}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = "__all__"
        labels = {
            "firstname": "Jméno",
            "lastname": "Příjmení",
            "phone": "Telefon",
            "email": "Email",
            "question_name": "Název otázky",
            "question_text": "Text otázky",
            "doctor": "Jméno a Příjmení lékaře",
            "answer": "Odpověď na otázku",
        }
        widgets = {
            "firstname": forms.TextInput(attrs={'class':'form-control'}),
            "lastname": forms.TextInput(attrs={'class':'form-control'}),
            "phone": forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.TextInput(attrs={'class':'form-control'}),
            "question_name": forms.TextInput(attrs={'class':'form-control'}),
            "question_text": forms.Textarea(attrs={'class':'form-control'}),
            "doctor": forms.TextInput(attrs={'class':'form-control'}),
            "answer": forms.Textarea(attrs={'class':'form-control'}),
        }