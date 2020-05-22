from django.db import models

class Users(models.Model):
	username = models.CharField(max_length = 50, unique = True, null=True)
	email = models.CharField(max_length = 50, unique=True)
	password = models.CharField(max_length = 200, unique=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	class Meta:
		db_table = 'account'

# Create your models here.
