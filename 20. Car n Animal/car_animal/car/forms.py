from django import forms

class Cars_Data(forms.Form):
    brand = forms.CharField(label="Please enter car brand",  max_length=30, required=True)
    model = forms.CharField(label="Model",  max_length=30, required=True)
    car_type = forms.CharField(label="Car Type", required=True)

    if not  brand and not model and not car_type:
        raise forms.ValidationError("All fields must be filled")