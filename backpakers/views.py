from django.shortcuts import render
from backpakers.models import Account , Message , TokenCode
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
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
def email_resend(request):
	return render(request , 'email_cert.html')
def auth_signin(request):
	if 'email' in request.session:
		return redirect('/')
	if request.POST['email']=='' or request.POST['password']=='':
		return redirect('/signin')
	email = request.POST['email']
	password = request.POST['password']
	user = Account.objects.filter(account_email=email)
	if not user or not check_password(request.POST['password'], user[0].account_password):
		return render(request, 'sign_in.html',{"alert":"Password wrong or Email has not been registered"})
	request.session['email']=user[0].account_email
	return redirect('/')
def auth_signup(request):
	if 'email' in request.session:
		return redirect('/')
	if request.POST['email'] =='' or request.POST['firstName']=='' or request.POST['lastName']=='' or request.POST['password']=='':
		return render(request, 'sign_up.html' , {"alert":"Empty value found"})
	email_check = Account.objects.filter(account_email=request.POST['email'])
	if email_check:
		return render(request , 'sign_up.html' , {"alert":"Email has already been registered"})
	user_email = request.POST['email']
	first_name = request.POST['firstName']
	last_name = request.POST['lastName']
	password = make_password(request.POST['password'],None, 'pbkdf2_sha256')
	user = Account(account_email = user_email, account_firstName=first_name, account_lastName=last_name, account_password=password)
	user.save()
	request.session['email']=user_email
	token = make_password(user_email , "backpakers","md5")
	addToken =TokenCode(user_email=user_email , token=token)
	addToken.save()
	subject = "backpakers.tk"
	link = "http://127.0.0.1:8000/active_account/?token="+token
	message = "Hi ,This is backpakers , click the following link to active your account "+link
	from_email  = settings.EMAIL_HOST_USER
	send_mail(subject , message , from_email ,[user_email] , fail_silently =True)
	return redirect('/')
def email_cert(request):
	if 'email' not in request.POST:
		return render(request , 'email_cert.html')
	if not Account.objects.filter(account_email=request.POST['email']):
		return render(request , 'email_cert.html' , {"pop":"Email not register"})
	if Account.objects.filter(account_email=request.POST['email'])[0].is_active ==True:
		return render(request , 'email_cert.html' , {"pop":"The account is active"})
	token = make_password(request.POST['email'] ,"backpakers" , "md5")
	addToken =TokenCode(user_email=request.POST['email'] , token=token)
	addToken.save()
	subject = "backpakers.tk"
	link = "http://127.0.0.1:8000/active_account/?token="+token
	message = "Hi , This is backpakers , click the following link to active your account "+link
	from_email  = settings.EMAIL_HOST_USER
	send_mail(subject , message , from_email ,[request.POST['email']] , fail_silently =True)
	return render(request ,'email_cert.html', {"pop":'We have send you a link to active your account, Please check your email !!'})
def active_account(request):
	if 'token' not in request.GET:
		return redirect('/email_cert')
	token =request.GET['token']
	email = TokenCode.objects.filter(token=token)[0].user_email
	if not email:
		return redirect('/email_cert')
	Account.objects.filter(account_email=email).update(is_active=True)
	return redirect('/')
def auth_logout(request):
	del request.session['email']
	return redirect(reverse('backpakers:index') , {"pop":"success"})
@csrf_exempt
def addMessageAjax(request):
	if request.POST['email']=='' or request.POST['name']=='' or request.POST['phone']==''  or request.POST['message']=='':
		return JsonResponse({"status":"error" , "reponseCode":"404"})
	message = Message(sender_name=request.POST['name'], sender_email=request.POST['email'], sender_phone = request.POST['phone'], message_text=request.POST['message'])
	message.save()
	test = {
	"status" : "success",
	"reponseCode" : "200"
	}
	return JsonResponse(test)
def forget_passwd(request):
	if 'email' not in request.POST:
		return render(request , 'forget_passwd.html')
	token = make_password(request.POST['email'] ,"backpakers" , "md5")
	TokenCode.objects.filter(user_email=request.POST['email']).delete()
	addToken =TokenCode(user_email=request.POST['email'] , token=token)
	addToken.save()
	subject = "backpakers.tk"
	link = "http://127.0.0.1:8000/reset_passwd/?token="+token
	message = "This is backpakers , click the following link to reset password  "+link
	from_email  = settings.EMAIL_HOST_USER
	send_mail(subject , message , from_email ,[request.POST['email']] , fail_silently =True)
	return render(request ,'forget_passwd.html', {"pop":'We have send you a link to reset password, Please check your email !!'})
def reset_passwd(request):
	if 'token' not  in request.GET:
		if 'newpasswd' not in request.POST:
			return redirect('/')
	if 'token' in request.GET:
		token = request.GET['token']
		request.session ['token'] =token 
	memail = TokenCode.objects.filter(token=request.session['token'])[0].user_email
	if not memail:
		del request.session['token']
		return redirect('/forget_passwd')
	if 'newpasswd' not in request.POST:
		return render(request , 'reset_passwd.html')
	password = make_password(request.POST['newpasswd'] , None ,'pbkdf2_sha256')
	Account.objects.filter(account_email=memail).update(account_password=password)
	del request.session['token']
	TokenCode.objects.filter(user_email=memail).delete()
	return redirect('/signin')



	




