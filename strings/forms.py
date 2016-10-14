from django import forms
from strings.models import String, StringStringSet, StringSet

class StringForm(forms.ModelForm):
    class Meta:
        model = String
        fields = ['gauge_imperial', ]


class StringStringsetForm(forms.ModelForm):
    class Meta:
        model = StringStringSet
        fields = [ 'string', 'note']

class StringSetForm(forms.ModelForm):
    class Meta:
        model = StringSet
        fields = ['name']
    
    