import re, urllib
import simplejson as json



class UrlOpener(urllib.FancyURLopener):
    version = "py-gtranslate/1.0"

base_uri = "http://ajax.googleapis.com/ajax/services/language/translate"

def translate(phrase, src="id", to="en"):
    data = urllib.urlencode({'v': '1.0', 'langpair': '%s|%s' % (src, to), 'q': phrase.encode('utf-8')})
    resp = json.load(UrlOpener().open('%s?%s' % (base_uri, data)))
    try:
        return resp['responseData']['translatedText']
    except:
        return ""

def tr(kalimat, request):
    to = request.session.get('lang','id')
    return translate(kalimat, to=to)
