from django.conf.urls.defaults import * 
from plag.weblog.models import Weblog
from plag.weblog.views import WeblogList, WeblogDetail

# Create your views here. 
urlpatterns = patterns('',
    (r'^$', WeblogList.as_view()),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', WeblogDetail.as_view()), 
)