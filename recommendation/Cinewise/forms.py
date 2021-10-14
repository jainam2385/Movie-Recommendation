from dal import autocomplete
from django import forms
from .models import Node, UserInput
from itertools import chain
from django.utils.safestring import mark_safe


class UserInputForm(forms.ModelForm):
    qs = Node.objects.all()
    print(qs)
    nodes = forms.ModelChoiceField(
        queryset=qs,
        widget=autocomplete.ModelSelect2Multiple(url='autocomplete'),
        label=mark_safe('Enter your interests:   ')
    )

    class Meta:
        model = UserInput
        fields = '__all__'
        attrs = {'data-html': True}
