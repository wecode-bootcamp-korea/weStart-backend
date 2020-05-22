from django.db import models
from account.models import Users

class Comment(models.Model):
        username = models.ForeignKey(Users, on_delete = models.SET_NULL, null=True)
        comment = models.TextField()
        created_at = models.DateTimeField(auto_now_add = True)
        updated_at = models.DateTimeField(auto_now = True)

	
        class Meta:
                db_table = 'comment'
# Create your models here.
