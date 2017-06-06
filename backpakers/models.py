from django.db import models

# Create your models here.
class Account(models.Model):
	account_email = models.CharField(max_length=200)
	account_firstName = models.CharField(max_length=200)
	account_lastName = models.CharField(max_length=200)
	account_password = models.CharField(max_length=200)

	def __str__(self):
		return self.account_firstName +" "+self.account_lastName