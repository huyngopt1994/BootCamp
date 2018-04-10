from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage, AccessRecord, User
from . import forms
# Create your views here.

def index(request):
	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records': webpages_list}
	return render(request,'first_app/index.html',context=date_dict)

def form_name_view(request):
	form = forms.FormName()
	if request.method == 'POST':
		form = forms.FormName(request.POST)
		if form.is_valid():
			# DO SOMETHING CODE
			print("VALIDATION SUCCESS!")
			print ("NAME %s" % form.cleaned_data['name'])
			print ("EMAIL %s" % form.cleaned_data['email'])
			print ("TEXT %s" % form.cleaned_data['text'])

	return render(request,'first_app/form_page.html',context={'form':form})

def user(request):

	form = forms.NewUserForm()
	if request.method == "POST":
		# some guy submit
		form = forms.NewUserForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print('ERROR FROM INVALID')

	return render(request,'first_app/user.html',{'form':form})
