from django import forms

from management.models import CustomUser


class sandtform(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields="__all__"