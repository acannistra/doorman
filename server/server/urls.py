from django.conf.urls import patterns, include, url
from django.contrib import admin
from doorman import views 

admin.autodiscover()

urlpatterns = patterns('',
    # main information page 
    url(r'^$', views.mainpage_view, name='mainpage'),
    # user page:
    url(r'^user/(?P<user_id>\S+)/$', views.userinfo, name='userinfo'),
    # django admin page [default]
    url(r'^admin/', include(admin.site.urls)),
    # login endpoint, Django default
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    # logout endpoint, Django default
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    # checkin POST endpoint
    url(r'^checkin/$', views.checkin_view, name='checkin')
)
