from django.db import models 
from django.contrib.auth.models import User 
# from tagging.fields import TagField 
from markdown import markdown 
import datetime 
from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model): 
    title = models.CharField(max_length=250, help_text="Maximum 250 characters.") 
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.") 
    description = HTMLField() # models.TextField()

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"
	
    def __unicode__(self): 
        return self.title 

    def get_absolute_url(self): 
        return "/categories/%s/" % self.slug
		
		
class Weblog(models.Model):
    LIVE_STATUS = 1 
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3   	
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'), 
        (DRAFT_STATUS, 'Draft'), 
        (HIDDEN_STATUS, 'Hidden'),
	) 
	
    GENERAL = 1 
    PHYSICS = 2
    CODING = 3 
    OPEN_STACK = 4	
    CATEGORY_CHOICES = (
        (GENERAL, 'General'), 
        (PHYSICS, 'Physics'), 
        (CODING, 'Computer programming'),
        (OPEN_STACK, 'Openstack'), 
	)
	
    # Core Fields 
    title = models.CharField(max_length=250) 
    excerpt = HTMLField() # models.TextField(blank=True) 
    body = HTMLField() # models.TextField() 
    pub_date = models.DateTimeField(default=datetime.datetime.now) 
	
    # Fields to store the generated html 
    excerpt_html = HTMLField() # models.TextField(editable=False, blank=True) 
    body_html = HTMLField() # models.TextField(editable=False, blank=True)
	
    # Meta Info 
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS) 
    slug = models.SlugField(unique_for_date='pub_date') 
	
    # Categorization 
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=GENERAL)  
    # tags = TagField(help_text="Separate tags with spaces") 

    class Meta: 
        ordering = ['-pub_date']	

    def __unicode__(self): 
        return self.title 
		
    def save(self, force_insert=False, force_update=False): 
        self.body_html = markdown(self.body) 
        if self.excerpt: 
            self.excerpt_html = markdown(self.excerpt) 
        super(Weblog, self).save(force_insert, force_update)
		
    def get_absolute_url(self):  
        return "/weblog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug )
