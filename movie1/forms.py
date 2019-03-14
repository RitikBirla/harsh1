from django import forms
from .models import Matrix


class MatrixForm(forms.ModelForm):
    class Meta:
        model = Matrix
        fields = ['Row', 'Column', 'Select_Dimension', 'Data']
