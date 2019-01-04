from django.db import models
from django.contrib.auth.models import User
from app.base.astract import TimeStumpModel, SoftDeletesModel


class Post(SoftDeletesModel):
    title = models.CharField(
        null=False,
        max_length=100,
        verbose_name="Post title"
    )
    body = models.TextField(
        null=False,
        verbose_name="Post content"
    )

    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name="Post author"
    )

    def __str__(self):
        return self.title
