from django.db import models

# Create your models here.

class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(default=None) # status: values 0-Deactivated, 1-Active, null-probably untouched yet
	class Meta:
		abstract = True
