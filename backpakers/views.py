from django.shortcuts import render
from backpakers.models import Account , Message
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
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
	if 'email' in request.session:
		return redirect('/')
	if request.POST['email']=='' or request.POST['password']=='':
		return redirect('/signin')
	email = request.POST['email']
	password = request.POST['password']
	user = Account.objects.filter(account_email=email , account_password=password)
	if not user:
		return render(request, 'sign_in.html',{"alert":"wrong password or no account"})
	request.session['email']=user[0].account_email
	return redirect('/')
def auth_signup(request):
	if 'email' in request.session:
		return redirect('/')
	if request.POST['email'] =='' or request.POST['firstName']=='' or request.POST['lastName']=='' or request.POST['password']=='':
		return render(request, 'sign_up.html' , {"alert":"Empty value found"})
	#email check
	email_check = Account.objects.filter(account_email=request.POST['email'])
	if email_check:
		return render(request , 'sign_up.html' , {"alert":"Email has already been registered"})
	user_email = request.POST['email']
	first_name = request.POST['firstName']
	last_name = request.POST['lastName']
	password = request.POST['password']
	user = Account(account_email = user_email, account_firstName=first_name, account_lastName=last_name, account_password=password)
	user.save()
	return redirect('/')
def auth_logout(request):
	del request.session['email']
	return redirect('/')
def addMessage(request):
	if request.POST['email']=='' or request.POST['name'] or request.POST['phone'] or request.POST[''] or request.POST['message']=='':
		return redirect(request.POST['from']+'/')
	message = Message(sender_name=request.POST['name'], sender_email=request.POST['email'], sender_phone = request.POST['phone'], message_text=request.POST['text'])
	message.save()
	return redirect(request.POST['from']+'/')

@csrf_exempt
def addMessageAjax(request):
	if request.POST['email']=='' or request.POST['name'] or request.POST['phone'] or request.POST[''] or request.POST['message']=='':
		return JsonResponse({"status":"error" , "reponseCode":"404"})
	message = Message(sender_name=request.POST['name'], sender_email=request.POST['email'], sender_phone = request.POST['phone'], message_text=request.POST['message'])
	message.save()
	test = {
	"status" : "success",
	"reponseCode" : "200"
	}
	return JsonResponse(test)




