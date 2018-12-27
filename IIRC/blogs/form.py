from django import forms
from .models import SignUp


class ContactForm(forms.Form):
	fullname = forms.CharField(required=False)
	email = forms.EmailField(required=True)
	message = forms.CharField(required=True)


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['email', 'fullname']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split('@')
		domain, extension = provider.split('.')
		if not extension == 'gov':
			raise forms.ValidationError('Please use .gov Email')
		return email
