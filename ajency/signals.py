
from ajency.models import Movies

from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=Movies, dispatch_uid="movies_save")
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
	

