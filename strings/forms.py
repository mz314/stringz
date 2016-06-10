from django import forms
from strings.models import String, StringSet

class StringForm(forms.ModelForm):
    class Meta:
        model = String
        fields = ['gauge_imperial', ]


class StringSetForm(forms.ModelForm):
    class Meta:
        model = StringSet
        fields = ['name']