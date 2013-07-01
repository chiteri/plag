# Create your views here.
from django.views.generic import ListView, DetailView
from plag.weblog.models import Weblog, Category 
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class WeblogList(ListView):
    model = Weblog 
    template = 'post_list.html' 
    paginate_by = 7
    # context_object_name = 'web_log'
    # queryset = Weblog.objects.all() 
	
class WeblogDetail(DetailView):
    model = Weblog 
    template = 'post_detail.html' 
    # context_object_name = 'web_log'
    queryset = Weblog.objects.all()