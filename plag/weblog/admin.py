from django.contrib import admin 
from plag.weblog.models import Weblog, Category 

class CategoryAdmin(admin.ModelAdmin): 
    prepopulated_fields = { 'slug': ['title'] } 

    class Media:
        # various admin options are here
        js = (
            '/static/scripts/tiny_mce/tinymce.min.js',
            '/static/scripts/admin/js/textareas.js',
        )
	
class WeblogAdmin(admin.ModelAdmin): 
    prepopulated_fields = { 'slug': ['title'] }
	
admin.site.register(Category, CategoryAdmin)
admin.site.register(Weblog, WeblogAdmin)