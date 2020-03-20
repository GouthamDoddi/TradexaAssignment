from django.db import models
# from django.contrib.auth import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s on {self.created_at}"

    def __unicode__(self):
        return "%s (%s : %s)" % (self.user, self.created_at.strftime('%Y-%m-%d %H:%M:%S'), self.updated_at)
