from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from msisdnarea import msisdn
from member import go_login, go_member, go_logout

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    #('^_ah/warmup$', 'djangoappengine.views.warmup'),
    #('^$', 'django.views.generic.simple.direct_to_template',
    # {'template': 'home.html'}),
    ('^$', msisdn),
    ('^admin/', include(admin.site.urls)),
    ('^login/', go_login),
    ('^member/', go_member),
    ('^logout/', go_logout),
)
