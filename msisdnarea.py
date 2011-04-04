import os
from django.http import HttpResponse
from django.template import Context, loader
from django import get_version
from msisdnprefix import prefix


def wilayah(m):
    if len(m) < 5:
        return ''
    if m[0] == '0':
        return wilayah('+62' + m[1:])
    if prefix.has_key(m):
        return prefix[m]
    return wilayah(m[:-1])


def msisdn(request):
    msisdn = 'msisdn' in request.POST and request.POST['msisdn'] or ''
    t = loader.get_template('msisdnarea.html')
    c = Context({'wilayah': wilayah(msisdn), 'msisdn': msisdn,
        'django_version': get_version()})
    return HttpResponse(t.render(c))
