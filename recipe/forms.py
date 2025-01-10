from django import forms
from recipe.models import ContactModel , AboutModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
    
class AboutFrom(forms.ModelForm):
    class Meta:
        model = AboutModel
        fields = '__all__'