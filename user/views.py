# http://djangobook.com/en/2.0/chapter14/

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from translate.lang import t

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/sudah-login-%s' % request.user.username)
    if not request.POST:
        return direct_to_template(request, 'login.html', {
            'username': t('Username', request),
            'password': t('Password', request),
            })
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password) # just check
    if user is not None and user.is_active:
        auth.login(request, user) # session
        return HttpResponseRedirect('/')
    return direct_to_template(request, 'login.html', {
        'error': t('Login gagal'),
        't': t,
        })

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
