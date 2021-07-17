from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class DonateFoodForm(forms.Form):
	first_name = forms.CharField(
		max_length = 50,
		label="First Name"		
		)
	last_name = forms.CharField(
		max_length = 50,
		label="Last Name"
		)
	mobile_number = forms.CharField(
		min_length=10,
		max_length= 10,
		label="Mobile Number",
		error_messages={'required': 'Please enter correct 10 digit mobile number'}
		)
	address = forms.CharField(
		widget = forms.Textarea,
		max_length = 2000,
		label="Address"
		)
	query = forms.CharField(
		widget = forms.Textarea,
		max_length = 2000,
		label="Any other query/request?",
		required=False
		)

class ContactForm(forms.Form):
	first_name = forms.CharField(
		max_length = 50,
		label="First Name"		
		)
	last_name = forms.CharField(
		max_length = 50,
		label="Last Name"
		)
	mobile_number = forms.CharField(
		min_length=10,
		max_length= 10,
		label="Mobile Number",
		error_messages={'required': 'Please enter correct 10 digit mobile number'}
		)
	address = forms.CharField(
		max_length = 30,
		label="Email Address",
		required=False
		)
	query = forms.CharField(
		widget = forms.Textarea,
		max_length = 2000,
		label="Ask your questions here!",
		required=True
		)