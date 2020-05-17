from django.db import models

class Users(models.Model):
	email = models.CharField(max_length = 50, unique=True)
	password = models.CharField(max_length = 300, unique=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	class Meta:
		db_table = 'account'

# Create your models here.
