from django import forms
# Set up Form
class FormName(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	text = forms.CharField(widget=forms.Textarea)
