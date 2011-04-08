from django.views.generic.simple import direct_to_template
from msisdnprefix import prefix


def wilayah(m):
    if len(m) < 5:
        return ''
    if m[0] == '0':
        return wilayah('+62' + m[1:])
    if prefix.has_key(m):
        return prefix[m]
    return wilayah(m[:-1])

def area(request):
    msisdn = 'msisdn' in request.POST and request.POST['msisdn'] or ''
    return direct_to_template(request, 'area.html', {
        'msisdn': msisdn,
        'wilayah': wilayah(msisdn),
        })
