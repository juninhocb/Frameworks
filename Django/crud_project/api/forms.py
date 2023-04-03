from django import forms
from dao.models import *

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'isRetired', 'idOffice', 'nationality']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('Name must have at least 3 characters.')
        return name

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age <= 0 or age >= 100:
            raise forms.ValidationError('Age must be at least more than 1 and less than 100.')
        return age
    
    def clean_is_retired(self):
        is_retired = self.cleaned_data.get('is_retired')
        return is_retired
    
    def clean_office_id(self):
        idOffice = self.cleaned_data.get('idOffice')
        if not Office.objects.filter(id=idOffice).exists():
            raise forms.ValidationError('Office with id {} does not exist.'.format(idOffice))
        return idOffice
    
    def clean_nationality(self):
        nationality = self.cleaned_data.get('nationality')
        try:
            Nationality(nationality)
        except ValueError:
            raise forms.ValidationError('Invalid nationality.')
        return nationality

class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('Name must have at least 3 characters.')
        return name