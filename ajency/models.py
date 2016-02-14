from django.db import models

# Create your models here.

from minbase.models import BaseModel
from django.template.defaultfilters import slugify

# Cache
from django.views.decorators.cache import cache_page
from django.core.cache import cache
#

class Categories(BaseModel):
	name = models.CharField(max_length=512, null=True, default=None)
	slug = models.SlugField(max_length=128, default=None, blank=True)

class Languages(BaseModel):
	name = models.CharField(max_length=512, null=True, default=None)
	slug = models.SlugField(max_length=128, default=None, blank=True)


from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver

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
	



@receiver(post_save, sender=Movies)
def after_save_insert_instance_into_redis(sender, instance, **kwargs):
	""" After model save, save this model in redis on its key """
	# Take this instance.pk & cache.hmset("movies", pk, instance.title)
	#Schema name, dbname:tblname <id> value , so, venv18_2:movies 1 value
	redis_key_constant = "movies"
	pk = instance.pk
	title = instance.title
	val = hget(redis_key_constant, pk)
	if val and val != title:
		redis.hset(redis_key_constant, pk, title)
	
