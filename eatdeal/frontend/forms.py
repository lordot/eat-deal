from django import forms

from api.models import Promo, Cafe, City


class PromoRequestForm(forms.ModelForm):
    cafe = forms.ModelChoiceField(
        queryset=Cafe.objects.all(),
        to_field_name=None,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    new_cafe_name = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Название нового кафе',
    )
    new_cafe_city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        required=False,
        label='Город нового кафе'
    )

    class Meta:
        model = Promo
        exclude = ['is_active', 'favorited', 'author', 'is_approved']

    def clean(self):
        cleaned_data = super().clean()
        cafe = cleaned_data.get('cafe')
        new_cafe_name = cleaned_data.get('new_cafe_name')
        new_cafe_city = cleaned_data.get('new_cafe_city')

        if not cafe and not new_cafe_name:
            raise forms.ValidationError('Укажите кафе или введите название нового кафе')

        if new_cafe_name:
            if not new_cafe_city:
                raise forms.ValidationError('Выберите город нового кафе')
            cafe = Cafe.objects.create(name=new_cafe_name, city=new_cafe_city)
            self.fields['cafe'].queryset = Cafe.objects.all()

        cleaned_data['cafe'] = cafe
        return cleaned_data
