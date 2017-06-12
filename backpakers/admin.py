from django.contrib import admin
from .models import Account , Message , TokenCode
# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'account_email' , 'account_password', 'is_active')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
	list_display = ('sender_name' , 'sender_email' , 'sender_phone' , 'message_text' , 'send_time')

