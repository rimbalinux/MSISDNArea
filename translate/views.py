from django.http import HttpResponseRedirect

def lang(request, lang_id):
    request.session['lang'] = lang_id
    request.session.modified = True
    dest = request.META['QUERY_STRING'].lstrip('destination=')
    return HttpResponseRedirect(dest)
