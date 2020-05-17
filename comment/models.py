from django.db import models

class Comment(models.Model):
        email = models.CharField(max_length = 50)
        comment = models.CharField(max_length = 300)
        created_at = models.DateTimeField(auto_now_add = True)
        updated_at = models.DateTimeField(auto_now = True)

        objects = models.Manager()
	
        class Meta:
                db_table = 'comment'
# Create your models here.
