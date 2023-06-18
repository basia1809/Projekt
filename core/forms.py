from django import forms
from .models import Zamowienie

class ZamownienieForm(forms.ModelForm):
    
    class Meta:
        model = Zamowienie
        exclude = ['data']
        widgets = {
            'data_usługi': forms.SelectDateWidget(),
            'komentarz': forms.Textarea()
        }