from django import forms
from App.models import Candidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__"
