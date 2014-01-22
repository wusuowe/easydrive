from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.conf import settings 
from drive.views import update_coach,register
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^drive/coach/update(?:/(?P<id>[\d]+)/)?',update_coach),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
     url(r'^login/$',  login,{'template_name': 'admin/login.html'}),
     url(r'^logout/$',  logout),
     url(r'^register/$',register),
     url(r'^changepassword/$', 'django.contrib.auth.views.password_change', {
         'template_name': 'registration/password_change_form.html'}, name="password-change"),
     url(r'^changepassworddone/$', 'django.contrib.auth.views.password_change_done', {
         'template_name': 'registration/password_change_done.html'
         }, name="password-change-done"),
)
