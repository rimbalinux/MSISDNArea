from django.views.generic.simple import direct_to_template
from authority.decorators import permission_required_or_403
#from django.contrib.auth.decorators import permission_required
from msisdnprefix import prefix



def wilayah(m):
    if len(m) < 5:
        return ''
    if m[0] == '0':
        return wilayah('+62' + m[1:])
    if prefix.has_key(m):
        return prefix[m]
    return wilayah(m[:-1])

#@permission_required_or_403('blog.add_blog')
@permission_required_or_403('msisdn.add_prefix')
def area(request):
    #if not request.user.has_perm('prefix.can_view'):
    #    return direct_to_template(request, 'authority/403.html')
    msisdn = 'msisdn' in request.POST and request.POST['msisdn'] or ''
    return direct_to_template(request, 'area.html', {
        'msisdn': msisdn,
        'wilayah': wilayah(msisdn),
        })
