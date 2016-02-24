from django.db import models

# Create your models here.
from minbase.models import BaseModel
from django.template.defaultfilters import slugify
from django.contrib.auth.models import *

app_label_vahan = "vahan"

class Query(BaseModel):
	class Meta:
		app_label = app_label_vahan
	
	title = models.CharField(max_length=128, default=None, blank=True)
	content = models.TextField() # Content of the question or command given by the user to the speech api
	user = models.ForeignKey(User, null=False) # Who asked the question
	slug = models.SlugField(max_length=128, default=None, blank=True)
	
	def __repr__(self):
		return self.title
	
	def save(self, *args, **kwargs):
		if not self.slug:
			self.title = self.content[:128]
			self.slug = slugify(self.title)
			
		super(Query, self).save(*args, **kwargs)
	
