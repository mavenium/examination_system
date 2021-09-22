from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class LoginForm(AuthenticationForm):
    """ Login form class """
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'] = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'autofocus': True,
                    'class': 'form-control',
                    'autocapitalize': 'off',
                    'autocomplete': 'off',
                    'tabindex': '1',
                    'placeholder': _('Username')
                }
            ),
            label=_('Username'),
            required=True,
        )

        self.fields['password'] = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocapitalize': 'off',
                    'autocomplete': 'off',
                    'type': 'password',
                    'tabindex': '2',
                    'placeholder': _('Password')
                }
            ),
            label=_('Password'),
            required=True,
        )
