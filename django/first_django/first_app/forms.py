from django import forms
from django.core import validators
from .models import User
# Set up Form
class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'

def check_for_z(value):
	if value[0].lower() != 'z':
		raise forms.ValidationError("NAME NEEDS TO START WITH Z")

class FormName(forms.Form):
	name = forms.CharField(validators=[check_for_z])
	email = forms.EmailField()
	verify_email = forms.EmailField(label='enter your email again')
	text = forms.CharField(widget=forms.Textarea)
	#add botcatcher, make it hidden
	botcatcher = forms.CharField(required=False,
	                             widget= forms.HiddenInput,
	                             validators=[validators.MaxLengthValidator(0)])

	def clean(self):
		all_clean_data = super(FormName,self).clean()
		email = all_clean_data['email']
		vmail = all_clean_data['verify_email']

		if email != vmail:
			raise forms.ValidationError('make sure emails match')