from django.shortcuts import render
from backpakers.models import Account
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
def index(request):
	return render(request, 'index.html')
def taiwan(request):
	return render(request, 'taiwan.html')
def malaysia(request):
	return render(request, 'malaysia.html')
def indonesia(request):
	return render(request, 'indonesia.html')
def signin(request):
	return render(request, 'sign_in.html')
def signup(request):
	return render(request , 'sign_up.html')
def contact(request):
	return render(request, 'contact.html')
def auth_signin(request):
	if request.user.is_authenticated():
		return redirect('/')
	email = request.POST.get('email','')
	password = request.POST.get('password','')
	user = auth.authenticate(email=email , password = password)
	if user is not None and user.is_active:
		auth.login(request,user)
		return redirect('/')
	else:
		return redirect('/signin')
def auth_signup(request):
	if request.POST['email'] =='' or request.POST['firstName']=='' or request.POST['lastName']=='' or request.POST['password']=='':
		return render(request, 'sign_up.html' , {alert:"Empty value found"})
	user_email = request.POST['email']

	first_name = request.POST['firstName']
	last_name = request.POST['lastName']
	password = request.POST['password']
	user = Account(account_email = user_email, account_firstName=first_name, account_lastName=last_name, account_password=password)
	user.save()
	return redirect('/')

