from django.shortcuts import render, redirect
from .forms import ContactForm, DonateFoodForm, NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages #import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .send import send_simple_message
from .sendc import send_message

# Create your views here.

def homepage(request):
	return render(request=request, template_name='main/index.html')

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Query" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'mobile': form.cleaned_data['mobile_number'], 
			'address':form.cleaned_data['address'], 
			'query':form.cleaned_data['query'], 
			}
			message = "\n".join(body.values())

			try:
				send_message(subject, message) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return render(request, "main/successpagec.html")
      
	form = ContactForm()
	return render(request, "main/contactv2.html", {'form':form})

def aboutus(request):
	return render(request=request, template_name='main/aboutus.html')

def donatefood(request):
	if request.method == 'POST':
		form = DonateFoodForm(request.POST)
		if form.is_valid():
			subject = "Food Donation" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'mobile': form.cleaned_data['mobile_number'], 
			'address':form.cleaned_data['address'], 
			'query':form.cleaned_data['query'], 
			}
			message = "\n".join(body.values())

			try:
				send_simple_message(subject, message) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return render(request, "main/successpage.html")
      
	form = DonateFoodForm()
	return render(request, "main/donatefoodnewv2.html", {'form':form})

###########################  LOGIN AND REGISTRATION SYSTEM  #######################################

def volunteer_registration(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="main/registerv2.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:homepage")

######################################  END  ################################################

def ngo_registration(request):
	return render(request=request, template_name='main/ngo_registration.html')

def donatemoney(request):
	return render(request=request, template_name='main/donatemoney.html')

def successpage(request):
	return render(request=request, template_name='main/successpage.html')