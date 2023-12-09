from django import forms

class Readers_Data(forms.Form):
    f_name = forms.CharField(label="Please enter your name",  max_length=30, required=True)
    l_name = forms.CharField(label="Your last name here",  max_length=30, required=True)
    mail = forms.EmailField(required=True)

    if not  f_name and not l_name and not mail:
        raise forms.ValidationError("All fields must be filled")