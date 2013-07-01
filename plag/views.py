from django.shortcuts import render_to_response  
from plag.weblog.models import Weblog

def home(request): 
    return render_to_response('base.html', {'web_logs': Weblog.objects.filter(featured=True)})