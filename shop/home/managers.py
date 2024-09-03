from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.utils import timezone

class CommentManager(models.Manager):
    def create_comment(self, user, post, body):
        if not body:
            raise ValueError('The comment most have text')
        
        comment = self.model(
            user = user,
            post = post,
            body = body,
            created = timezone.now(),
            
        )
        comment.save(using=self._db)
        return comment
    