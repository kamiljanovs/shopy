from django import forms

class ProductForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Product Title'
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Product Description'
            }
        )
    )
    price = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Product Price'
            }
        )
    )
    size = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Product Size'
            }
        )
    )
    image = forms.ImageField(required=False)


    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'python' in title:
            # self.errors['title'] = ['Python в заголовке не допустим']
            raise forms.ValidationError('Python in title isnt allowed')
        return title

    def clean(self):
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        if title==description:
            raise forms.ValidationError('Title and Description shouldnt be similar')

        return self.cleaned_data

class ReviewForm(forms.Form):
    text = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Review Text'
            }
        )
    )