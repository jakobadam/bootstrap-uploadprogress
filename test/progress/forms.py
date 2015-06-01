from django import forms

from models import Package

def _get_widget(placeholder):
    return forms.TextInput(attrs={'placeholder':placeholder})

class PackageForm(forms.ModelForm):

    class Meta:
        model = Package
        widgets = {
            'name': _get_widget('Enter package name')
            }


