# http://docs.djangoproject.com/en/1.3/howto/custom-template-tags/#passing-template-variables-to-the-tag

from django import template
from django.template.base import Node, TemplateSyntaxError
from translate.lang import translate

register = template.Library()

class TranslateNode(Node):
    def __init__(self, text):
        self.request = template.Variable('request')
        self.text = text

    def render(self, context):
        try:
            request = self.request.resolve(context)
            return translate(self.text, to=request.session.get('lang','id'))
        except template.VariableDoesNotExist:
            return 'Variabel tidak ada'

@register.tag
def t(parser, token):
    try:
        tag, text = token.split_contents()
    except ValueError:
        raise TemplateSyntaxError("Tag %r butuh satu parameter" % token.contents.split()[0])
    if not (text[0] == text[-1] and text[0] in ('"', "'")):
        raise template.TemplateSyntaxError("Parameter tag %r harus menggunakan kutip" % tag_name)
    return TranslateNode(text[1:-1]) # hapus kutip
