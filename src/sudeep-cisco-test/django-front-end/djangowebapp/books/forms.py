from django import forms

class BookForm(forms.Form):
    name = forms.CharField(max_length=200)
    isbn = forms.CharField(max_length=20)
    price = forms.DecimalField()
    