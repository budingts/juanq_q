from django.conf.urls import patterns, include, url
from mysns.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
	(r'^index$',index),
	(r'^about_us$',about_us),
        (r'^about_us_history$',about_us_history),
        (r'^about_us_team$',about_us_team),       
       (r'^about_us_mission$',about_us_mission),
       (r'^product_show$',product_show),
       (r'^gallery$',gallery),
        (r'^contact_us$',contact_us),
         (r'^blog$',blog),
         (r'^villa$',villa),
         (r'^bungalows',bungalows),
         (r'^apartments$',apartments),

	
        (r'^form$',form),
        (r'^del_by_id$',del_by_id),
        (r'^update_by_id$',update_by_id),
        (r'^to_edit$',to_edit),
        (r'^acounts/register$',register),
	(r'^acounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'acounts/login.html'}),
	 # Examples:
    # url(r'^$', 'mysns.views.home', name='home'),
    # url(r'^mysns/', include('mysns.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
