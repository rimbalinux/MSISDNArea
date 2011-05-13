from ..models import Block
from django.template import Library
from translate.lang import tr

register = Library()

@register.simple_tag
def show_block(name):
    try:
        return Block.objects.get(name=name).content
    except Block.DoesNotExist:
        return ''
    except Block.MultipleObjectsReturned:
        return 'Error: Multiple blocks for "%s"' % name

@register.inclusion_tag('minicms/menu.html', takes_context=True)
def show_menu(context, name='menu'):
    request = context['request']

    menu = []
    try:
        for line in Block.objects.get(name=name).content.splitlines():
            line = line.rstrip()
            try:
                title, url = line.rsplit(' ', 1)
            except:
                continue
            menu.append({'title': tr(title.strip(), request), 'url': url})
    except Block.DoesNotExist:
        pass

    # Mark the best-matching URL as active
    active = None
    active_len = 0
    # Normalize path
    path = request.path.rstrip('/') + '/'
    for item in menu:
        # Normalize path
        url = item['url'].rstrip('/') + '/'
        # Root is only active if you have a "Home" link
        if path != '/' and url == '/':
            continue
        if path.startswith(url) and len(url) > active_len:
            active = item
            active_len = len(url)
    if active is not None:
        active['active'] = True
    return {'menu': menu}

@register.inclusion_tag('minicms/menu.html', takes_context=True)
def show_menu_lang(context, name='menu-lang'):
    request = context['request']

    menu = []
    try:
        for line in Block.objects.get(name=name).content.splitlines():
            line = line.rstrip()
            try:
                title, url = line.rsplit(' ', 1)
            except:
                continue
            url += '?destination=%s' % request.path
            menu.append({'title': tr(title.strip(), request), 'url': url})
    except Block.DoesNotExist:
        pass

    # Mark the best-matching URL as active
    active = None
    active_len = 0
    # Normalize path
    path = request.path.rstrip('/') + '/'
    for item in menu:
        # url = '/lang/en?destination=/hp/memilih-handphone
        if request.session.get('lang','id') == item['url'].split('?')[0].split('/')[-1]:
            active = item
            active_len = len(url)
    if active is not None:
        active['active'] = True
    return {'menu': menu}
