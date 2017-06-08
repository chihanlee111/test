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
]