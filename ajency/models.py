from django.db import models

# Create your models here.

from minbase.models import BaseModel
from django.template.defaultfilters import slugify

class Categories(BaseModel):
	name = models.CharField(max_length=512, null=True, default=None)
	slug = models.SlugField(max_length=128, default=None, blank=True)

class Languages(BaseModel):
	name = models.CharField(max_length=512, null=True, default=None)
	slug = models.SlugField(max_length=128, default=None, blank=True)

class Movies(BaseModel):
	title = models.CharField(max_length=512, null=True, default=None)
	description = models.TextField(default=None, blank=True)
	image = models.ImageField(upload_to="uploads/", default=None, blank=True)
	length = models.IntegerField(default=None, null=True, blank=True) # Comments="Length In Minutes"
	release_date = models.DateTimeField()
	slug = models.SlugField(max_length=128, default=None, blank=True)
	categories = models.ManyToManyField(Categories)
	languages = models.ManyToManyField(Languages)
	
	def __repr__(self):
		return self.title
	
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)[:128]
		super(Movies, self).save(*args, **kwargs)

