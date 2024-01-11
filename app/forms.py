from django import forms
from app.models import *

class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = "__all__"
    bot = forms.CharField(max_length = 10, widget = forms.HiddenInput(), required=False)

    def clean_bot(self):
        bt = self.cleaned_data['bot']
        if len(bt)> 0:
            raise forms.ValidationError("Invalid")