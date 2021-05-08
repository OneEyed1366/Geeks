from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, ValidationError
from django.core import validators

from .models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'content__check'

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar', "desc")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'content__check'
            field.help_text = ''

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        first_name = cleaned_data.get("first_name")

        if username and first_name:
            if "А" not in first_name:
                raise ValidationError(
                    "В Вашем имени нет чудесной буквы 'A'!"
                )

        else:
            if username:
                raise ValidationError("Вы не указали Ваше настоящее имя!")

            if first_name:
                raise ValidationError("Вы не указали Ваше имя пользователя!")

        return cleaned_data

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        first_name = cleaned_data.get("first_name")

        if username and first_name:
            # Only do something if both fields are valid so far.
            if "Андрей" not in first_name:
                raise ValidationError(
                    "Вы не Андрей!"
                )
        
        else:
            if username:
                raise ValidationError("Вы не указали Ваше настоящее имя!")
            
            if first_name:
                raise ValidationError("Вы не указали Ваше имя пользователя!")
            
        return cleaned_data

    # def clean_name(self):
    #     data = self.cleaned_data["username"]

        

    #     return data
