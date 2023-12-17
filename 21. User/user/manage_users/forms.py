from django import forms
from .models import Users

class UsersForm(forms.ModelForm):
    f_name = forms.CharField(label="First Name", max_length=20)
    l_name = forms.CharField(label="Last Name", max_length=20)
    mail = forms.EmailField(label="Mail", max_length=30)

    """if not  f_name and not l_name and not mail:
        raise forms.ValidationError("All fields must be filled")"""

    class Meta:
        model = Users
        fields = ['f_name', 'l_name', 'mail']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['f_name', 'l_name', 'mail']


class DeleteForm(forms.Form):
    user_id = forms.IntegerField(label='User ID')

    def clean_user_id(self):
        user_id = self.cleaned_data['user_id']
        if not Users.objects.filter(pk=user_id).exists():
            raise forms.ValidationError(f"There is no user with id - {user_id}")
        return user_id
