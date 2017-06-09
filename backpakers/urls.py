from django.conf.urls import url

from . import views
app_name = 'backpakers'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^taiwan/$',views.taiwan, name='taiwan'),
    url(r'^indonesia/$',views.indonesia, name='indonesia'),
    url(r'^malaysia/$',views.malaysia, name='malaysia'),
    url(r'^signin/$',views.signin, name='signin'),
    url(r'^signup/$',views.signup, name='signup'),
    url(r'^contact/$',views.contact, name='contact'),
    url(r'^auth_signin/$',views.auth_signin, name='auth_signin'),
    url(r'^auth_signup/$',views.auth_signup, name='auth_signup'),
    url(r'^auth_logout/$',views.auth_logout, name='auth_logout'),
    url(r'^user_message/$',views.addMessageAjax, name='user_message'),
    url(r'^forget_passwd/$',views.forget_passwd, name='forget_passwd'),
    url(r'^reset_passwd/$',views.reset_passwd, name='reset_passwd'),
    url(r'^email_resend/$',views.email_resend, name='email_resend'),
    url(r'^email_cert/$',views.email_cert, name='email_cert'),
    url(r'^active_account/$',views.active_account, name='active_account'),
]