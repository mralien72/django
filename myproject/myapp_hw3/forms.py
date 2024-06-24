from django import forms
import datetime


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity_products = forms.IntegerField()
    date_created = forms.DateField(initial=datetime.date.today)
    image = forms.ImageField()
