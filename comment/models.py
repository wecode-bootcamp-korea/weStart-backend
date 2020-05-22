from django.db import models
from account.models import Account

class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete = models.SET_NULL, null=True)
    user_comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
