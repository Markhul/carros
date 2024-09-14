from typing import Any
from django import forms
from cars.models import Brand, Car


class CarForm(forms.Form):
    model = forms.CharField(max_length=50)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.DecimalField(decimal_places=2, max_digits=8,)
    photo = forms.ImageField()

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save()
        return car
    

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
      
    def clean_value(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1974:
            self.add_error('factory_year', 'so carro apartir de 1975')
        return factory_year
    
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor minimo do carro deve ser de 20.000')
        return value
