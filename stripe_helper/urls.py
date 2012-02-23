from django.conf.urls.defaults import *

from stripe_helpers import views

urlpatterns = patterns('',
    url(r'webhooks/$',     views.webhooks,          name='webhooks'),
)
