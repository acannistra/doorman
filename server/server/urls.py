from django.conf.urls import patterns, include, url
from django.contrib import admin
from doorman import views 

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #
    # base page 
    url(r'^$', views.mainpage_view, name='mainpage'),
    # user page:
    url(r'^user/(?P<user_id>\S+)/$', views.userinfo, name='userinfo'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^checkin/$', views.checkin_view, name='checkin')
)
