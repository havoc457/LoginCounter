from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name = 'index'),
	url(r'^users/add', views.add, name='add'),
	url(r'^users/login', views.login, name='login'),
	url(r'^TESTAPI/resetFixture', views.reset, name='reset'),
	url(r'^TESTAPI/unitTests', views.unitTests, name='unitTests'),
)