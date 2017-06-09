from django.db import models

# Create your models here.
class Message(models.Model):
	sender_name = models.CharField(max_length=200)
	sender_email = models.CharField(max_length=200)
	sender_phone = models.CharField(max_length=200)
	message_text = models.CharField(max_length=500)
	def __str__(self):
		return "From  " +self.sender_email
class Account(models.Model):
	account_email = models.EmailField(max_length=200)
	account_firstName = models.CharField(max_length=200)
	account_lastName = models.CharField(max_length=200)
	account_password = models.CharField(max_length=200)
	is_active = models.BooleanField(default=False)
	def __str__(self):
		return self.account_firstName +" "+self.account_lastName

class TokenCode(models.Model):
	user_email = models.EmailField(max_length=200)
	token = models.CharField(max_length=200)
	def __str__(self):
		return self.user_email