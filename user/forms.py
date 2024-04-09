from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        min_length=3,
        required=True,
        label="Username",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Username'
                   }
        )
    )
    password = forms.CharField(
        max_length=150,
        min_length=6,
        required=True,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Password'
            }
        )
    )
    password2 = forms.CharField(
        max_length=150,
        min_length=6,
        required=True,
        label="Repeat Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Repeat Password'
            }
        )
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email'
            }
        )
    )
    first_name = forms.CharField(
        max_length=150,
        required=True,
        label="First Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter First Name'
            }
        )

    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        label="Last Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Last Name'
            }
        )
    )

    def clean(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        min_length=3,
        required=True,
        label="Username",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Username'
            }
        )
    )
    password = forms.CharField(
        max_length=150,
        min_length=6,
        required=True,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Password'
            }
        )
    )
    age = forms.IntegerField(
        required=False,
        label="Age",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your age'
            }
        )
    )
    bio = forms.CharField(
        required=False,
        label="Bio",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Tell about yourself'
            }
        )
    )
    avatar = forms.ImageField(
        required=False,
        label="Avatar",
        widget=forms.FileInput(
            attrs={
                'class': 'form-control-file'
            }
        )
    )

    def clean(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")