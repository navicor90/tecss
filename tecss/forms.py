from .models import Customer
from django import forms


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['fullname','email','address','telephone','fax']


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()