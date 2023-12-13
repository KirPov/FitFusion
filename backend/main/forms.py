from django.forms import ModelForm, TextInput, EmailInput, FileInput
from .models import Order, Products


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'email', 'adress']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "phone": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Номер телефона"
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Электронная почта'
            }),
            "adress": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес доставки'
            })
        }

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['img']

        widgets = {
            "img": FileInput(attrs={
                'class': 'form-control',
                'type': 'file'
            })
        }
