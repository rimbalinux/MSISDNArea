from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from msisdnarea import msisdn 

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    #('^_ah/warmup$', 'djangoappengine.views.warmup'),
    #('^$', 'django.views.generic.simple.direct_to_template',
    # {'template': 'home.html'}),
    ('^$', msisdn),
    ('^admin/', include(admin.site.urls)),
)
