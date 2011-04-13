from django.http import HttpResponseRedirect

def lang(request, lang_id):
    request.session['lang'] = lang_id
    request.session.modified = True
    return HttpResponseRedirect('/')
