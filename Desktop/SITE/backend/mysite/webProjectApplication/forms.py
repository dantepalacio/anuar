from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class AuthUserForm(AuthenticationForm,forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        return user


class MessageForm(forms.Form):
    sender = forms.CharField(max_length=255)
    recipient = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)